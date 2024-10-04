# -*- coding: utf-8 -*-

# Python原生默认不支持接口，默认多继承，所有的方法都必须不能实现
from abc import abstractmethod, ABCMeta


# 创建一个接口Shape
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 创建Shape的实体类
class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangel:draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square:draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle:draw() method.")


# 创建一个接口Color
class Color(metaclass=ABCMeta):
    @abstractmethod
    def fill(self):
        pass


# 创建Color的实体类
class Red(Color):
    def fill(self):
        print("Inside Red.fill() method.")


class Green(Color):
    def fill(self):
        print("Inside Green.fill() method.")


class Blue(Color):
    def fill(self):
        print("Inside Blue.fill() method.")


# 创建抽象工厂
class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def getColor(self, color):
        pass

    @abstractmethod
    def getShape(self, shape):
        pass


# 创建抽象工厂实例 ShapeFactory,ColorFactory
class ShapeFactory(AbstractFactory):
    def getShape(self, shapeType):
        if shapeType == None:
            return None
        elif shapeType.upper() == "CIRCLE":
            return Circle()
        elif shapeType.upper() == "RECTANGLE":
            return Rectangle()
        elif shapeType.upper() == "SQUARE":
            return Square()
        return None

    def getColor(self, colorType):
        pass


class ColorFactory(AbstractFactory):
    def getShape(self, shapeType):
        pass

    def getColor(self, colorType):
        if colorType == None:
            return None
        elif colorType.upper() == "RED":
            return Red()
        elif colorType.upper() == "GREEN":
            return Green()
        elif colorType.upper() == "BLUE":
            return Blue()
        return None


# 创建工厂创造器/生产器类
class FactoryProducer():
    @staticmethod
    # 这里不能写成 def getFactory(self,choiceType): 否则会报错
    # 因为是静态方法，被直接调用，所以不能带self参数
    # 如果不是静态方法，必须加self参数，且需要先实例化对象，再用实例化的对象调用方法
    def getFactory(choiceType):
        if choiceType.upper() == "SHAPE":
            return ShapeFactory()
        elif choiceType.upper() == "COLOR":
            return ColorFactory()
        return None


# 调用输出
if __name__ == '__main__':
    shapeFactory = FactoryProducer.getFactory('SHAPE')
    shape1 = shapeFactory.getShape("CIRCLE")
    shape1.draw()
    shape2 = shapeFactory.getShape("RECTANGLE")
    shape2.draw()
    shape3 = shapeFactory.getShape("SQUARE")
    shape3.draw()

    colorFactory = FactoryProducer.getFactory("COLOR")
    color1 = colorFactory.getColor("RED")
    color1.fill()
    color2 = colorFactory.getColor("Green")
    color2.fill()
    color3 = colorFactory.getColor("BLUE")
    color3.fill()
