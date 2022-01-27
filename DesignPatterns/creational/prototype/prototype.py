# -*- coding:utf-8 -*-

# 原型模式 with Python
"""
当我们已经存在一个对象，这个对象有其属性和方法，若我们还想去获得另外一个同类型对象，此时有两种选择：
重新去创建一个新的对象，或者 根据已有的对象复制一个副本，而在很多时候我们不需要完全去重新构建一个对象，
只需要在原有对象存在的基础上（保留原对象），去修改其属性和方法得到一个新的对象。
"""
from abc import abstractmethod, ABCMeta
import copy

# 用copy包实现深拷贝(copy.deepcopy())和浅拷贝(copy.copy())
"""
深拷贝 copy.deepcopy() 函数，会递归复制并创建新对象；而浅拷贝 copy () 函数会利用引用指向同一个对象。
深拷贝的优点是对象之间互不影响，但是会耗费资源，创建比较耗时；如果不会修改对象可以使用浅拷贝，更加节省资源和创建时间。
"""


# 创建 一 接口
class Shape(metaclass=ABCMeta):
    _id = ""
    in_type = ""

    @abstractmethod
    def draw(self):
        pass

    def getType(self):
        return self.in_type

    def getID(self):
        return self._id

    def setID(self, in_id):
        self._id = in_id

    # 1、原型角色：定义用于复制现有实例来生成新实例的方法；
    # 2、具体原型角色：实现用于复制现有实例来生成新实例的方法
    # Python中无接口概念，定义与实现全部由抽象类完成
    def clone(self):
        # 深拷贝
        my_clone = copy.deepcopy(self)
        return my_clone


# 创建实体类
class Rectangle(Shape):
    def __init__(self):
        self.in_type = "Rectangel"

    def draw(self):
        print("Inside Rectangle.draw() method.")


class Square(Shape):
    def __init__(self):
        self.in_type = "Square"

    def draw(self):
        print("Inside Square.draw() method.")


class Circle(Shape):
    def __init__(self):
        self.in_type = "Circle"

    def draw(self):
        print("Inside Circle.draw() method.")


# 获取数据实体类
class ShapeCache:
    # Python 无静态变量，用开放类变量
    # 3、使用者角色：维护一个注册表，并提供一个找出正确实例原型的方法load_cache。
    #    最后，提供一个获取新实例的方法get_shape，用来委托复制实例的方法生成新实例。
    shape_map = {}

    def get_shape(self, shape_id):  # 提供一个获取新实例的方法
        cached_shape = self.shape_map[shape_id]  # 提供一个找出正确实例原型的方法
        return cached_shape.clone()  # 委托复制实例的方法生成新实例

    # 静态方法
    @staticmethod
    def load_cache():
        circle1 = Circle()
        circle1.setID("1")
        ShapeCache.shape_map[circle1.getID()] = circle1

        square1 = Square()
        square1.setID("2")
        ShapeCache.shape_map[square1.getID()] = square1

        rectangle1 = Rectangle()
        rectangle1.setID("3")
        ShapeCache.shape_map[rectangle1.getID()] = rectangle1


# 调用输出
if __name__ == '__main__':
    ShapeCache.load_cache()
    myShape = ShapeCache()

    cloneShape1 = myShape.get_shape("1")
    print("Shape : %s" % cloneShape1.getType())
    cloneShape1.draw()

    cloneShape2 = myShape.get_shape("2")
    print("Shape : %s" % cloneShape2.getType())
    cloneShape2.draw()

    cloneShape3 = myShape.get_shape("3")
    print("Shape : %s" % cloneShape3.getType())
    cloneShape3.draw()
