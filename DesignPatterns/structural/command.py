# # Command Pattern with Python Code
# from abc import abstractmethod, ABCMeta
#
#
# # 创建一个命令接口Order
# class Order(metaclass=ABCMeta):
#     @abstractmethod
#     def execute(self):
#         pass
#
#
# # 创建实现了Order接口的实体类
# class BuyStock(Order):
#     _abcStock = None
#
#     def __init__(self, inStock):
#         self._abcStock = inStock
#
#     def execute(self):
#         self._abcStock.buy()
#
#
# class SellStock(Order):
#     _abcStock = None
#
#     def __init__(self, inStock):
#         self._abcStock = inStock
#
#     def execute(self):
#         self._abcStock.sell()
#
#
# # 创建一个请求类
# class Stock:
#     _name = "ABC"
#     _quantity = 10
#
#     def buy(self):
#         print("Stock [Name : {0}, Quantity: {1}] bought.".format(self._name, self._quantity))
#
#     def sell(self):
#         print("Stock [Name : {0}, Quantity: {1}] sold.".format(self._name, self._quantity))
#
#
# # 创建命令调用类
# class Broker:
#     _orderList = []
#
#     def takeOrder(self, inOrder):
#         self._orderList.append(inOrder)
#
#     def placeOrders(self):
#         for aOrder in self._orderList:
#             aOrder.execute()
#         self._orderList.clear()
#
#
# # 调用输出
# if __name__ == '__main__':
#     abcStock = Stock()
#     buyStockOrder = BuyStock(abcStock)
#     sellStockOrder = SellStock(abcStock)
#
#     broker = Broker()
#     broker.takeOrder(buyStockOrder)
#     broker.takeOrder(sellStockOrder)
#
#     broker.placeOrders()


# 抽象命令接口，声明接口Execute，具体命令都继承这个接口
class Command:
    def execute(self):
        pass


# 具体命令,coding,testing,,把[小喽喽]和[干活]绑定在一起
# 定义一个接收者对象与动作之间的请求绑定，然后调用Receiver的操作，实现Execute方法
class ConcreteCommand1(Command):  # 写代码命令
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.coding()


class ConcreteCommand2(Command):  # 进行测试命令
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.testing()


# 命令接受者，负责执行具体命令，是真正做事的人，定义小喽喽
# 命令的接收者，知道如何实施与执行一个请求相关的操作
class Receiver:
    @staticmethod
    def coding():
        print('我是小喽啰，苦活累活都是我的')
        print('...小领导传来命令了，正在coding，请勿打扰...')

    @staticmethod
    def testing():
        print('我是小喽啰，苦活累活都是我的')
        print('...小领导传来命令了，正在testing，请勿打扰...')


# 命令调用者，相当于小领导，负责传达大领导的命令，让小喽啰去执行
# 命令的接收者，将命令请求传递给相应的命令对象，每个ConcreteCommand都是一个Invoker的成员
class Invoker:
    @staticmethod
    def execute(cmd):
        print('李工，上级下达了命令，这周要把代码码完，测试做完，你去做吧')
        cmd.execute()


# 模仿client,是大领导，负责下达命令
# 客户端程序，创建一个具体命令对象并设定它的接收者
if __name__ == '__main__':
    receiver = Receiver()

    # 大领导下达了俩命令
    code = ConcreteCommand1(receiver)
    test = ConcreteCommand2(receiver)

    invoker = Invoker()
    # 小领导传达大领导的命令，让小喽啰去执行
    invoker.execute(code)
    print('======================')
    invoker.execute(test)

