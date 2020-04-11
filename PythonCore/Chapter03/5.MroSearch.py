# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        MroSearch
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------
1.5:类和实例属性的查找顺序----mro查找
    类查找属性的查找顺序有深度优先查找和广度优先查找。

    1. 广度优先查找：“存在同名方法覆盖”弊端
    2. 深度优先查找：“菱形结构”存在弊端

    3. 但在python3中为了避免深度优先算法与广度优先算法混乱，出现了C3算法避免了两种算法出现的问题，
    例如菱形搜索应用深度优先算法，从A找B再到D找到方法，可能C中重写了D的方法，因此深度优先算法不能解决菱形搜索的情况，
    然而C3算法解决了以上出现的两种情况。
"""


# 单继承: 类属性查找顺序
class A:
    name = "A"

    def __init__(self):
        self.name = "obj"


a = A()
print(a.name)  # 输出 obj or A ?  ==> obj, 即先找自己的，找不到再去找类属性，再找不到报错
print(A.name)  # A

# 多继承: 类属性查找顺序
# 1. 先看深度优先查找: A-B-D-C-E
#    D    E
#    |    |
#    B    C
#      \ /
#       A
# 经典类: 不继承object类. 多继承遵循深度优先
# python3以后称为新式类，全部都继承object,不写成class A(object) 而是class A
# 在经典类中不写object就认为不继承object，py3新式类中写不写都继承object

# BFS弊端分析: C类中存在与D类中的同名属性或方法，A去查找时A(B, C)，B写在C前面，且D、B可看做一个整体。
#             所以B先找到，然后在BFS会继续找C，发现同名，则C会覆盖B。这是不符合预期的。
#             C3中找到即返回，不会覆盖

"""
class E:
    pass


class D:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)  # __mro__魔法方法直接显示出类查找属性的顺序

(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, 
<class '__main__.C'>, <class '__main__.E'>, <class 'object'>)

"""


# 2. 广度优先查找: A-B-C-D
#       D
#      / \
#     B   C
#      \ /
#       A
# DFS弊端分析: C类中覆盖重写了D中属性或方法，但是A在查找时按照DFS，结果是D的，但是C是A的直接父类，结果不符合预期，即C。
#             可见C没有达到覆盖效果，所以DFS对类似"菱形"结构存在问题，故改进出现了BFS
class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)

# 当子类A调用echo方法时：
# A().echo()
# python 先搜索 A 本地类，再搜索Ｂ，有则返回，无则继续搜索Ｃ，以此类推。


"""
为了避免深度优先算法与广度优先算法混乱，出现了C3算法避免了两种算法出现的问题，从2.3版本，采用了新算法C3
    例如菱形搜索应用深度优先算法，从A找B再到D找到方法，可能C中重写了D的方法，因此深度优先算法不能解决菱形搜索的情况，
    然而C3算法解决了以上出现的两种情况。
    
在 python 2.2 之后，python 实现了一个新的ＭＲＯ算法：Ｃ３算法，用于方法解析顺序 。
方法解析顺序 ：多重继承时，用于在子类中调用父类方法时确定调用哪个父类的方法 。


Ｃ3算法，算法的表达式为：
       A
      / \-
     B   C
      \ /
       D


L[D(B,C)]
= D + merge(L[B],L[C],[B,C])

以上表达式也等同于：

Ｌ[D(B,C)] = D + merge(mro(B,object),mro(C,object),[B,C]) ==>     
Ｌ[D(B,C)] = D + merge( [B,object], [C,object],[B,C])  [] : 列表表达式
merge: Ｃ3算法的核心，merge通用公式：mro(子类(父类1,父类2,...))=[子类]+merge(mro(父类1),mro(父类2),....,[父类1,父类2])

分析：merge时，取第一个列表的头，也就是L[B,object] ，如果这个头不在任何表的尾部，那么将它加到class D的线性化中，并且从合并中的列表里删除 ；
     否则查找下一个列表的头，如果是个好的表头则取出它。 
     需要注意的是： 表头指是第一个元素 ，尾部是指除表头之外的其它所有元素。
     如[A,B,C,D,E,F],A是表头，[B,C,D,E,F]是尾部。



方式解析：
L(D(B,C)) = D + merge( [B,object] ,[C,object] , [B,C] )

# 列表[B,object]的表头是Ｂ，没有出现在其它表([C,object] 、[B,C] )的尾部

= [D, B] + merge( [object], [C,object] , [C] )

# 列表[Ｃ,object]的表头是Ｃ，没有出现在其它表([object] 、[C] )的尾部 ，注意 [C] 这个列表只有表头，没有尾部

= [D, B, C] + merge( [object] , [object] )

= [D, B, C, object]

通过以上的运算，可以得出跟 D().__mro__ 一样的结果 
"""
