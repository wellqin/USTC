# -*- coding:utf-8 -*-

# Strategy Pattern with Python Code
from abc import abstractmethod, ABCMeta


"""
策略模式定义了一组算法，将每个算法都封装起来，并使他们之间可以互相替换。策略模式使得每个算法和调用他们的实体彼此独立，减少了代码的冗余。
一般当算法策略需要经常被替换时，可以考虑策略模式。比如下面在电商场景里会经常碰到的订单价格计算的例子，计算价格时会用到满减、打折、优惠券等方式。
"""


# 创建一个接口
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def do_operation(self, in_num1, in_num2):
        print(self.__class__.__name__)


# 创建实现接口的实体类
class OperationAdd(Strategy):
    def do_operation(self, in_num1, in_num2):
        return in_num1 + in_num2


class OperationSubtract(Strategy):
    def do_operation(self, in_num1, in_num2):
        return in_num1 - in_num2


class OperationMultiply(Strategy):
    def do_operation(self, in_num1, in_num2):
        return in_num1 * in_num2


# 创建Context类
class Context:
    _strategy = None

    def __init__(self, in_strategy):
        self._strategy = in_strategy

    def execute_strategy(self, in_num1, in_num2):
        return self._strategy.do_operation(in_num1, in_num2)


# 调用输出
if __name__ == '__main__':
    """这里策略的选取： 可使用简单工厂模式，做到二种设计模式结合"""
    aContext = Context(in_strategy=OperationAdd())
    print("10 + 5 = {0}".format(aContext.execute_strategy(10, 5)))

    aContext = Context(in_strategy=OperationSubtract())
    print("10 - 5 = {0}".format(aContext.execute_strategy(10, 5)))

    aContext = Context(in_strategy=OperationMultiply())
    print("10 * 5 = {0}".format(aContext.execute_strategy(10, 5)))
