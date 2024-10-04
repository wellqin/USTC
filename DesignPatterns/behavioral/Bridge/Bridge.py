# -*- coding:utf-8 -*-

# Bridge Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 创建桥接实现接口
class DrawAPI(metaclass=ABCMeta):
    """
    桥接模式中，具体的实现类放在作为“桥梁”的接口中实现，而“桥梁”接口中只有实现功能的抽象方法；
    具体实现类是继承“桥梁”，而不直接继承实现类的抽象类(Shape)，抽象类与具体的实现类在结构上是相互独立的，
    两者的相互变化并不会影响到彼此，只要“桥梁”没变，两者的变化并不会影响到彼此。
    """
    @abstractmethod
    def drawCircle(self, inRadius, inX, inY):
        pass


# 创建实现了DrawAPI接口的实体桥接实现类
class RedCircle(DrawAPI):
    def drawCircle(self, inRadius, inX, inY):
        print("Drawing Circle [ color: red , radius: {0} , x : {1} , y : {2}]".format(inRadius, inX, inY))


class GreenCircle(DrawAPI):
    def drawCircle(self, inRadius, inX, inY):
        print("Drawing Circle [ color: green , radius: {0} , x : {1} , y : {2}]".format(inRadius, inX, inY))


# 使用DrawAPI接口创建抽象类Shape
class Shape(metaclass=ABCMeta):
    """
    按一般逻辑来说，我们是直接继承Shape来创建不同的具体对象，
    但桥接模式中是通过“桥梁”DrawAPI建立抽象与具体实现之间的联系，调用DrawAPI中的方法来具体实现。
    """
    _drawAPI = None

    def __init__(self, inDrawAPI):
        self._drawAPI = inDrawAPI


# 创建实现了Shape接口的实体类
class Circle(Shape):
    _intX = 0
    _intY = 0
    _intRadius = 0

    def __init__(self, inX, inY, inRadius, inDrawAPI):
        Shape.__init__(self, inDrawAPI)
        self._intX = inX
        self._intY = inY
        self._intRadius = inRadius

    def draw(self):
        self._drawAPI.drawCircle(self._intRadius, self._intX, self._intY)


class Square(Shape):
    _intX = 0
    _intY = 0
    _intRadius = 0

    def __init__(self, inX, inY, inDrawAPI):
        Shape.__init__(self, inDrawAPI)
        self._intX = inX
        self._intY = inY

    def draw(self):
        self._drawAPI.drawCircle("", self._intX, self._intY)


# 调用输出
if __name__ == '__main__':
    redCircle = Circle(100, 100, 10, RedCircle())
    greenCircle = Circle(100, 100, 10, GreenCircle())

    redCircle.draw()
    greenCircle.draw()

    redSquare = Square(100, 10, RedCircle())
    redSquare.draw()

