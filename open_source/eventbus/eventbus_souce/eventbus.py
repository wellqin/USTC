import logging
import typing

from .executor import MainOrderExecutor
from .finder import Finder
from .logger import Logger
from .subscription import Subscription
from .utils import SupportError


def get_default_logger(identifier):
    logger = logging.getLogger(f'EventBus[{identifier}]')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger


class EventBus:
    """
    Observer 注册表，是最复杂的一个类，框架中几乎所有的核心逻辑都在这个类中。这个类大量使用了反射语法。

    1、准备订阅者这一步骤，分为注册 注销以及准备订阅方法两步。
        1.1 准备订阅方法: 订阅方法是通过注解@Subscribe的方式来实现的
        1.2 注册:只需要一行即可完成订阅者的注册,EventBus.getDefault().register(this);
                EventBus.getDefault()方法其实就是通过单例模式返回EventBus的实例

        1.3 注销：EventBus.getDefault().unregister(this);
    2、发送事件
    """

    def __init__(self, logger: Logger = None):
        self.finder = Finder()
        # 事件订阅者
        self.subscriptions_by_event_type: typing.Dict[type, typing.List[Subscription]] = {}
        self.event_types_by_subscriber: typing.Dict[object, typing.List[type]] = {}
        self.sticky_events: typing.Dict[type, object] = {}
        self.logger = logger if logger is not None else get_default_logger(id(self))
        self.executor = MainOrderExecutor(self)  # 订阅事件线程处理方式，可以在此进行切换，存在五种执行模式，BACKGROUND模式最优
        # self.executor = MainExecutor(self)

    def register(self, subscriber):
        """
        注册：我们通过获取订阅者的类对象，然后找到其订阅方法，调用subscribe订阅方法进行订阅
        方法中的参数subscriber就是我们调用方法是传入的this，所以也就是表示Activity、Fragment。

        简单概括一下就是：先根据订阅者类去METHOD_CACHE中查找，找到则直接返回订阅者方法列表，
        找不到则根据是否使用subscriber index 来决定是否使用
        findUsingInfo(EventBus 推荐你使用注解处理器，避免在运行时使用反射来查找订阅方法，而是在编译的时候查找)还是findUsingReflection(即直接使用反射)方法。
        找到订阅方法列表，加入到METHOD_CACHE中方便下次使用，反之，找不到订阅方法，抛出异常。

        """
        if subscriber in self.event_types_by_subscriber:
            self.logger.warning(f"{subscriber}已经注册过")
            return
        # 反射找到@Subscribe注解的全部订阅方法
        subscriber_methods = self.finder.find(subscriber)
        for subscriber_method in subscriber_methods:
            # 依次注册订阅者的每个订阅方法：1个订阅者 -> N个订阅方法
            self.subscribe(subscriber, subscriber_method)
            self.logger.debug(f'{subscriber} has registered the method {subscriber_method}')

    def subscribe(self, subscriber, subscriber_method):
        """
        @param: subscriber：订阅者
        @param: subscriber_method：标记是否为粘性事件
        """
        event_type = subscriber_method.event_type
        subscription = Subscription(subscriber, subscriber_method)
        subscriptions = self.subscriptions_by_event_type.get(event_type, [])
        if subscription in subscriptions:
            raise SupportError(f'订阅类{subscriber.__class__.__name__}已经注册了{event_type.__name__}事件')
        subscriptions.append(subscription)
        # 订阅方法重排序
        subscriptions.sort(key=lambda _subscription: _subscription.subscriber_method.priority)
        self.subscriptions_by_event_type.update({event_type: subscriptions})
        # 按照订阅者绑定事件类型
        subscriber_events = self.event_types_by_subscriber.get(subscriber, [])
        subscriber_events.append(event_type)
        self.event_types_by_subscriber.update({subscriber: subscriber_events})
        # 支持发送粘性事件
        """
        如果你在发送普通事件前没有注册过订阅者，那么这时你发送的事件是不会被接收执行的，这个事件也就被回收了。 
        而粘性事件就不一样了，你可以在发送粘性事件后，再去注册订阅者，一旦完成订阅，这个订阅者就会接收到这个粘性事件。 
        用了一个sticky_events集合来保存粘性事件，存入后，与普通事件一样同样调用post()方法。 ？？ 嗯 ？？，这时我就有疑问了，
        针对上面的使用场景，我先发送粘性事件，然后再去注册订阅，这时执行post方法去发送事件，根本就没有对应的订阅者啊，肯定是发送失败的。
        所以，细想一下，想达到这样效果，订阅者注册订阅后应该再将这个存入下来的事件发送一下。 
        """
        if subscriber_method.sticky:
            # 订阅者在注册订阅方法中，如果当前订阅方法支持粘性事件，则会去stickyEvents集合中查件是否有对应的粘性事件，如果找到粘性事件，则发送该事件。
            sticky_event = self.sticky_events.get(event_type, None)
            if sticky_event is not None:  # check_post_sticky_event_to_subscription
                self.invoke_subscriber(subscription, sticky_event)

    def invoke_subscriber(self, subscription, event):
        if subscription.active and not getattr(event, '__cancelled__', False):
            try:
                subscription.subscriber_method(subscription.subscriber, event)
            except Exception as exception:
                self.logger.warning(f'在为{subscription}发送{event}时出现错误:{exception}')

    def unregister(self, subscriber):
        subscribed_types = self.event_types_by_subscriber.get(subscriber)
        if subscribed_types is None:
            self.logger.warning(f"订阅者{subscriber}没有被正常注册故无需注销")
        else:
            for event_type in subscribed_types:
                self.unsubscribe_by_event_type(subscriber, event_type)

    def unsubscribe_by_event_type(self, subscriber, event_type):
        """
        按照事件类型取消订阅

        仅更新subscriptions_by_event_type,不更新types_by_subscriber，
        所以在调用该方法时必须提前调用更新types_by_subscriber
        :param subscriber:
        :param event_type:
        :return:
        """
        # 获取事件对应的subscription列表
        subscriptions = self.subscriptions_by_event_type.get(event_type, None)
        if subscriptions is None:
            return
        # 获取subscription列表中包含subscriber的元素
        for subscription in subscriptions:
            if subscription.subscriber == subscriber:
                # 失活状态
                subscription.active = False
                # 删除
                subscriptions.remove(subscription)

    def post(self, event):
        self.logger.info(f"正在发布事件{event}")
        print(f"正在发布事件{event}")
        subscriptions = self.subscriptions_by_event_type.get(event.__class__, [])
        for subscription in subscriptions:
            self.executor.enqueue(subscription, event)

    def post_sticky(self, event):
        self.sticky_events.update({event.__class__: event})
        self.post(event)

    def get_sticky_event(self, event_type):
        return self.sticky_events.get(event_type, None)

    def cancel_delivery(self, event):
        setattr(event, '__cancelled__', True)
        if self.sticky_events.get(event.__class__) == event:
            self.remove_sticky_event(event)

    def remove_sticky_event(self, event):
        """
        支持对事件类、事件实例进行解析并移除
        :param event: 事件类或事件实例
        :return:
        """
        if isinstance(event, type):
            del self.sticky_events[event]
        elif self.sticky_events.get(event.__class__) == event:
            del self.sticky_events[event.__class__]

    def stop(self):
        self.executor.stop()

    # def is_registered(self, subscriber) -> bool:
    #     return subscriber in self.event_types_by_subscriber

    # def check_post_sticky_event_to_subscription(self, subscription: Subscription, event):
    #     if event is not None:
    #         self.invoke_subscriber(subscription, event)
