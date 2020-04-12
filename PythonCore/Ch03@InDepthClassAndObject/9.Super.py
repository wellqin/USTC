# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        9.Super
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------

1.9、super真的是调用父类吗？
子类中写了super().__init__()，会调用父类的__init__方法

1. 既然重写了A的构造函数，为什么还要调用super？
    以后面的多线程为例，可以复用代码


2. super函数到底执行顺序是什么？（遵循__mro__算法逻辑顺序）
    B(C, A): 结果B, A
    B(A, C): 结果B, C
    多继承时，先执行了一个父类的__init__方法，哪个在前面调用哪个。

    本质来说：调用的不是父类构造函数，而是__mro__算法中顺序的构造函数
"""
from threading import Thread

"""
class A:
    def __init__(self):
        print("A")


# class C:
#     def __init__(self):
#         print("C")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()  # 想让他初始化B之后，运行A的初始化，这是python2的用法
        super().__init__()  # python3的用法

# b = B()  # 运行结果：B,A,A
"""


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        # self.name = name  # 实际上父类Thread的参数有了name这个参数，我们直接可以调用父类
        super().__init__(name=name)  # 这样我们就不用写具体的name相关的逻辑了


class A:
    def __init__(self):
        print("A")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class D(B, C):  # D父类优先是B，B父类为A，而此时调用的不是A，而是C，遵循了__mro__算法
    def __init__(self):
        print("D")
        super().__init__()


if __name__ == '__main__':
    d = D()  # D-B-C-A

    print(D.__mro__)
    # (<class '__main__.D'>,
    #  <class '__main__.B'>,
    #  <class '__main__.C'>,
    #  <class '__main__.A'>,
    #  <class 'object'>)

