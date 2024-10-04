# -*- coding:utf-8 -*-

import sys


from open_source.eventbus.eventbus_souce import bus, Subscribe


class QuoteEvent:

    def __init__(self, data):
        self.open = data['open']
        self.high = data['high']
        self.low = data['low']
        self.close = data['close']


class OrderEvent:

    def __init__(self, symbol, price, amount):
        self.symbol = symbol
        self.price = price
        self.amount = amount


class TradeEvent:

    def __init__(self, symbol, price, amount):
        self.symbol = symbol
        self.price = price
        self.amount = amount


class TestSubscriber:

    def __init__(self):
        bus.get().register(self)

    @Subscribe()
    def on_event(self, event: QuoteEvent):
        print("开盘价: ", event.open)
        bus.get().post(OrderEvent('HUOBI.ETHUSDT', event.close, 200))


class StickyConfigEvent:

    def __init__(self, config):
        self.config = config


class StickySubscriber:

    def __init__(self):
        print('StickySubscriber will be registered')
        bus.get().register(self)

    @Subscribe(sticky=True)
    def call_by_sticky_event(self, event: StickyConfigEvent):
        print("粘滞事件配置: ", event.config)
        bus.get().remove_sticky_event(event)
        print('已移除粘滞事件')

    @Subscribe()
    def call_by_default_event(self, event: QuoteEvent):
        print("接受到行情数据，准备存入数据库: ", event.open)


class StickyNewSubscriber:

    def __init__(self):
        print('StickyNewSubscriber will be registered ')
        bus.get().register(self)

    @Subscribe(sticky=True)
    def call_by_sticky_event(self, event: StickyConfigEvent):
        print("若未移除则会有此条输出: ", event.config)

    @Subscribe()
    def call_by_default_event(self, event: QuoteEvent):
        print("接受到行情数据，准备存入数据库: ", event.open)


class SubscriberA:

    def __init__(self):
        bus.get().register(self)

    @Subscribe(priority=10)
    def on_event(self, event: OrderEvent):
        print(f'以价格{event.price}购买{event.symbol}共计{event.amount}')
        print(bus.get().subscriptions_by_event_type.get(OrderEvent, []))
        if len(bus.get().subscriptions_by_event_type.get(OrderEvent, [])) == 1:
                bus.get().stop()


class SubscriberB:

    def __init__(self):
        bus.get().register(self)

    @Subscribe(priority=100)
    def on_event(self, order: OrderEvent):
        print(f'已将{order.symbol}计入到资产组合')
        trade = TradeEvent(order.symbol, order.price, order.amount)

        print('还可以继续执行')
        bus.get().cancel_delivery(order)
        bus.get().post(trade)
        bus.get().unregister(self)


class SubscriberC:

    def __init__(self):
        # print(f'in subscriber c: {bus.get()}')
        bus.get().register(self)

    @Subscribe(priority=1)
    def on_event(self, event: TradeEvent):
        print(f"已撮合该交易: {event.symbol}-{event.price}-{event.amount}")
        order = OrderEvent(event.symbol, event.price, event.amount)
        bus.get().post(order)


def run():
    import random
    import string
    # bus.get() 其实就是通过单例模式返回 EventBus 的实例
    current_bus = bus.get()
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    setattr(current_bus, 'context_str', f'random_{salt}')
    """
    普通事件：是指已有的事件订阅者能够收到事件发送者发送的事件，在事件发送之后注册的事件接收者将无法收到事件。
    发送普通事件可以调用EventBus.getDefault().post()方法进行发送。
    """
    TestSubscriber()
    SubscriberA()
    SubscriberB()
    SubscriberC()
    # 我先发送粘性事件，然后再去注册订阅，这时执行post方法去发送事件，根本就没有对应的订阅者啊，肯定是发送失败的。
    # 所以，细想一下，想达到这样效果，订阅者注册订阅后应该再将这个存入下来的事件发送一下。
    # 比如StickySubscriber()注册时，init方法会自己进行注册，执行粘性事件方法
    current_bus.post_sticky(StickyConfigEvent('模拟配置数据'))

    """
    粘性事件：是指不管是在事件发送之前注册的事件接收者还是在事件发送之后注册的事件接收者都能够收到事件。
    这里于普通事件的区别之处在于事件接收处需要定义事件接收类型，它可以通过@Subscribe(threadMode = xxx, sticky = true)的方式进行声明；
    在事件发送时需要调用EventBus.getDefault().postSticky()方法进行发送。事件类型默认为普通事件。
    """
    StickySubscriber()
    StickyNewSubscriber()
    current_bus.post(QuoteEvent({'open': 10, 'high': 100, 'low': 3, 'close': 60}))
    # return test


if __name__ == '__main__':
    # from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
    # futures = []
    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     for i in range(10):
    #         futures.append(executor.submit(run))
    #
    # print([future.result() for future in futures])
    run()
    """
    StickySubscriber will be registered
    粘滞事件配置:  模拟配置数据
    已移除粘滞事件
    StickyNewSubscriber will be registered 
    正在发布事件<__main__.QuoteEvent object at 0x109e934c0>
    开盘价:  10
    正在发布事件<__main__.OrderEvent object at 0x109e92f20>
    以价格60购买HUOBI.ETHUSDT共计200
    [<open_source.eventbus.eventbus_souce.subscription.Subscription object at 0x109e93ac0>, 
        <open_source.eventbus.eventbus_souce.subscription.Subscription object at 0x109e93280>]
    已将HUOBI.ETHUSDT计入到资产组合
    还可以继续执行
    正在发布事件<__main__.TradeEvent object at 0x109ae37f0>
    已撮合该交易: HUOBI.ETHUSDT-60-200
    正在发布事件<__main__.OrderEvent object at 0x109ec5540>

    """
