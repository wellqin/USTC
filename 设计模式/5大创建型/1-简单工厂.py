# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        工厂方法
Description :   
Author :          wellqin
date:             2019/9/13
Change Activity:  2019/9/13
-------------------------------------------------
"""

"""
意图：
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。
"""


class ShapeFactory(object):
    '''工厂类'''

    def getShape(self):
        return self.shape_name


class Circle(ShapeFactory):

    def __init__(self):
        self.shape_name = "Circle"
    def draw(self):
        print('draw circle')


class Rectangle(ShapeFactory):

    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print('draw Rectangle')

# 一般就是这么设计的，但是对象shapeCircle/shapeRectangle这样处理很麻烦，产生了多个不同对象
# shapeCircle = Circle()
# shapeRectangle = Rectangle()
# shapeCircle.draw()
# shapeRectangle.draw()


class Shape(object):
    '''
    接口类，负责决定创建哪个ShapeFactory的子类
    使一个类的实例化延迟到其子类。
    '''

    def create(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None


fac = Shape()
obj = fac.create('Rectangle')
obj.draw()
obj.getShape()

"""
优点：客户端不需要修改代码。
缺点：当需要增加新的运算类的时候，不仅需新加运算类，还要修改工厂类，违反了开闭原则。
"""