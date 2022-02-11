# -*- coding:utf-8 -*-

# Decorator Pattern with Python Code
from abc import abstractmethod, ABCMeta


# 创建Shape接口
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 实现Shape的实体类：Rectangle、Circle
class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")


class Circle(Shape):
    def draw(self):
        print("Shape: Circle")


# 创建实现了Shape接口的抽象装饰类ShapeDecorator类
class ShapeDecorator(Shape):
    _decoratedShape = None

    def __init__(self, inDecoratedShape):
        self._decoratedShape = inDecoratedShape

    def draw(self):
        self._decoratedShape.draw()


# 创建扩展了ShapeDecorator类的实体装饰类对象
class RedShapeDecorator(ShapeDecorator):
    def __init__(self, inDecoratedShape):
        ShapeDecorator.__init__(self, inDecoratedShape)

    def draw(self):
        self._decoratedShape.draw()
        self.setRedBorder(self._decoratedShape)

    def setRedBorder(self, inDecoratedShape):
        print("Border Color: Red")


# 调用输出
if __name__ == '__main__':
    aCircle = Circle()
    aRedCircle = RedShapeDecorator(Circle())
    aRedRectangle = RedShapeDecorator(Rectangle())

    print("Circle with normal border")
    aCircle.draw()
    print("\nCircle of red border")
    aRedCircle.draw()
    print("\nRectangle of red border")
    aRedRectangle.draw()
