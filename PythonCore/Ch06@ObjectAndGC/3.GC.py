# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.GC
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.3、del语句和垃圾回收
    python采用的是引用计数机制为主，标记-清除和分代收集两种机制为辅的策略。

    GC中引用计数为0时，GC会调用对象的__del__方法，将其销毁，我们重写这个方法观察一下
"""


class Pyobj:
    def __del__(self):
        print("obj is GC")


print("1")
obj = Pyobj()
obj = 6  # obj指向其他对象，原来对象则销毁
print("2")

"""
1
obj is GC
2
"""


a = 1  # a = 1 然后1的引用计数加一，b=1然后1的引用计数再加一，当删除a的时候，
b = 1  # 引用计数减一，当减到0的时候才会启用垃圾回收机制，然而c++ 是del直接回收
del a
print(b)  # 1
print(a)  # NameError: name 'a' is not defined


# 如果我们要对我们的对象做垃圾回收机制的时候，我们就重载__del__魔法函数
class A:
    def __del__(self):
        pass
