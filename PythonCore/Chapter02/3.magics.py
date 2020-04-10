# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.magics
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------
1.3、魔法函数一览


1.3.1、非数学运算

字符串表示：
__repr__  #在开发环境下调用，例如python解释器下，以及jupyter notebook下调用返回对象的地址（开发人员才用到的）
__str__   #对我们的对象进行字符串格式化的时候进行调用

集合序列相关：
__len__
__getitem__
__setitem__
__delitem__
__contains__

迭代相关：
__iter__
__next__

可调用：
__call__

with上下文管理器：
__enter__
__exit__

数值转换：
__abs__
__bool__
__int__
__float__
__hash__
__index__

元类相关：
__new__
__init__

属性相关：
__getattr__、__setattr__
__getattribute__、__setattribute__
__dir__

属性描述符：
__get__、__set__、__delete__

协程：
__await__、__aiter__、__anext__、__aenter__、__aexit__


1.3.2、数学运算

一元运算符：
__neg__(-)、__pos__(+)、__abs__

二元运算符：
__lt__(<)、__le__(<=)、__eq__(==)、__ne__(!=)、__gt__(>)、__ge__(>=)

算术运算符：
__add__(+)、__sub__(-)、__mul__(*)、__truediv__(/)、__floordiv(//)、__mod__(%)、__divmod__(divmod())、__pow__(**或pow())、__round__(round())

反向算数运算符：
__radd__、__rsub__、__rmul__、__rtruediv__、__rfloordiv、__rmod__、__rdivmod__、__rpow__、

增量赋值算数运算符：
__iadd__、__isub__、__imul__、__itruediv__、__ifloordiv、__imod__、__ipow__

位运算符：
__invert__(~)、__lshift__(<<)、__rshift__(>>)、__and__(&)、__or__(|)、__xor__(^)

反向位运算符：
__rlshift__、__rrshift__、__rand__、__ror__、__rxor__

增量赋值算数运算符：
__ilshift__、__irshift__、__iand__、__ior__、__ixor__
"""


# 以字符串表示为例
# __repr__  # 在开发环境下调用，例如python解释器下，以及jupyter notebook下调用返回对象的地址（开发人员才用到的）
# __str__   # 对我们的对象进行字符串格式化的时候进行调用
class Students(object):
    def __init__(self, student_list):
        self.student = student_list

    def __str__(self):
        return ",".join(self.student)

    def __repr__(self):
        return ",".join(self.student)


students = Students(["lisha", "wang", "li"])
print(students)  # lisha,wang,li

students  # 此时是输出为空的，但在交互式下，会调用__repr__
# 此时我们重写__repr__，就有输出了

students.__repr__()


# 以__abs__为例
class MyNum:
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num) + 1


num = MyNum(-1)
print(abs(num))  # 2  即在abs时会隐藏调用__abs__


# 以__add__为例
class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        re_vector = MyVector(self.x + other.x, self.y + other.y)
        return re_vector

    def __str__(self):
        return "x:{x}, y:{y}".format(x=self.x, y=self.y)


vec1 = MyVector(1, 2)
vec2 = MyVector(2, 3)
print(vec1 + vec2)  # x:3, y:5
