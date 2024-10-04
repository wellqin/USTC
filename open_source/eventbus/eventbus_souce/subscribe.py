import inspect

from open_source.eventbus.eventbus_souce.utils import SupportError

subscribe_annotation_property = '__subscribe_annotation__'


class SubscribeAnnotation:

    def __init__(self, priority=0, sticky=False, thread_mode="Default"):
        self._priority = priority
        self._sticky = sticky
        self._thread_mode = thread_mode

    @property
    def priority(self):
        return self._priority

    @property
    def sticky(self):
        return self._sticky


class Subscribe:
    """
    1、Subscribe 是一个注解，用于标明观察者中的哪个函数可以接收消息。
    订阅装饰器，给被订阅的方法添加元信息

    订阅装饰器将会为方法添加方法元信息，用来在EventBus对类进行注册时使用。
    注意，为了降低可能产生Bug的情况，这里限制仅允许为类方法进行装饰，但并
    非不能对其他可调用类进行装饰。

    :arg priority 优先级，该方法在同一队列内处理事件的优先级
    :arg sticky 粘滞事件处理标志，在该方法被初始化时是否处理对应事件的粘滞事件
    """

    def __init__(self, priority: int = 100, sticky: bool = False, thread_mode: str = "Default"):
        # 订阅者优先级以影响事件传递顺序。在同一传递线程ThreadMode中，优先级较高的订阅者将在优先级较低的其他订阅者之前接收事件
        # 注意：优先级不影响具有不同ThreadMode的订阅服务器之间的传递顺序！
        self.priority = priority
        self.sticky = sticky
        # 支持指定线程模式，最好使用枚举类型Enum表示各个类型
        self.thread_mode = thread_mode

    def __call__(self, callable_method):
        """
        调用Subscribe装饰器对可调用对象的修改

        该方法将限制被装饰对象为类方法，由于装饰时均不以对象绑定类方法的形式进行调用，故在装饰时需要进行特殊判断。
        :param callable_method: 被装饰类方法
        :return:
        """
        self._check_method_valid(callable_method)
        setattr(callable_method, subscribe_annotation_property, SubscribeAnnotation(
            priority=self.priority, sticky=self.sticky, thread_mode=self.thread_mode))
        return callable_method

    @staticmethod
    def _check_method_valid(callable_method):
        # 判断方法签名是否为Class.Method(self, event: EventType)
        # 注意此处不检查classmethod/staticmethod/instancemethod,正确使用时应使用instancemethod
        # __qualname__方法：https://segmentfault.com/a/1190000023637227
        qualname_splited = callable_method.__qualname__.split('.')
        arg_spec = inspect.getfullargspec(callable_method)
        if len(qualname_splited) != 2:
            raise SupportError(f'当前方法{callable_method.__qualname__}不是类方法')
        if (len(arg_spec.args) != 2 or arg_spec.varargs is not None
                or arg_spec.varkw is not None or arg_spec.defaults is not None
                or len(arg_spec.kwonlyargs) != 0 or arg_spec.kwonlydefaults is not None
                or arg_spec.annotations.get(arg_spec.args[1]) is None):
            raise SupportError(f'请检查订阅方法，当前方法{callable_method.__qualname__}应为Class.Method(self, event: EventType)形式')