#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/5 21:36
@Author  : qinwei05
"""


# 一、函数装饰函数
def wrapFun(func):
    def inner(a, b):
        print('function name:', func.__name__)
        r = func(a, b)
        return r

    return inner


@wrapFun
def myadd(a, b):
    return a + b


print(myadd(2, 3))
print(wrapFun(myadd)(2, 3))
print("*" * 30)


# 执行myadd(2, 3)就相当于执行：wrapFun(myadd)(2, 3)，wrapFun(myadd)返回inner函数的应用，此时还不可执行，需要加()才可以执行


# 二：函数装饰类
def wrapClass(cls):
    def inner(a):
        print('class name:', cls.__name__)
        return cls(a)

    return inner


@wrapClass
class Foo():
    def __init__(self, a):
        self.a = a

    def fun(self):
        print('self.a =', self.a)


m = Foo('xiemanR')
m.fun()
print("*" * 30)


# 三、类装饰函数
class ShowFunName():
    def __init__(self, func):
        self._func = func

    def __call__(self, a):
        # 使得ShowFunName的实例showFunName，在showFunName()就可以调用call方法，而不是需要showFunName.__call__()这种方式进行调用
        print('function name:', self._func.__name__)
        return self._func(a)


@ShowFunName
def Bar(a):
    return a


# Bar = ShowFunName(Bar)
# Bar('xiemanR') == ShowFunName(Bar).__call__('xiemanR')
print(Bar('xiemanR'))  # 本质完成了ShowFunName的实例化对象调用，这个对象_func属性为原来的Bar，所以可以执行
print("*" * 30)


# 四、类装饰类
class ShowClassName(object):
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, a):
        print('class name:', self._cls.__name__)
        return self._cls(a)


@ShowClassName
class Foobar(object):
    def __init__(self, a):
        self.value = a

    def fun(self):
        print(self.value)


# Foobar = ShowClassName(Foobar)
a = Foobar('xiemanR')
a.fun()
