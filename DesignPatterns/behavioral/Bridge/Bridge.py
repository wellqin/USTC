# -*- coding:utf-8 -*-

# Bridge Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 创建桥接实现接口
class DrawAPI(metaclass=ABCMeta):
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


# 调用输出
if __name__ == '__main__':
    redCircle = Circle(100, 100, 10, RedCircle())
    greenCircle = Circle(100, 100, 10, GreenCircle())

    redCircle.draw()
    greenCircle.draw()
