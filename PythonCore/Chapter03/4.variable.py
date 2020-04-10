# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.variable
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------

1.4、类变量和实例变量
"""


class A:
    a = 1  # a是类变量

    def __init__(self, x, y):  # self是类的实例 x与y已经绑定到实例上的属性上了
        self.x = x
        self.y = y


num = A(2, 3)
# A.a = 11   # 如果修改类属性，那么实例的值也会跟着变
# num.a = 100  # 如果修改实例属性，那么类属性的值不变，会在对象中新建一个实例属性的值，寻找的时候直接对象属性中寻找。

print(num.x, num.y, num.a)  # 2 3 1  为什么实例num能够找到A的类属性呢?

# 首先实例num先在实例属性种寻找，如果没有找到的话就会向上寻找，找到类属性
# print(A.a)  # 1 类属性
# print(A.x)  # AttributeError: type object 'A' has no attribute 'x'
# # 类找实例属性找不到是因为类首先到自己的属性中找，如果没有找到的话，就不会向下寻找
