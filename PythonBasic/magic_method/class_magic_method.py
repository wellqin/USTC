#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/3/3 14:08
@Author  : qinwei05
"""


class Foo(object):
    """
    class
    """
    def __init__(self):
        self.name = 'jack'

    def __getitem__(self, item):
        if item in self.__dict__:  # item = key，判断该key是否存在对象的 __dict__ 里，
            return self.__dict__[item]  # 返回该对象 __dict__ 里key对应的value

    def __setitem__(self, key, value):
        self.__dict__[key] = value  # 在对象 __dict__ 为指定的key设置value

    def __delitem__(self, key):
        del self.__dict__[key]  # 在对象 __dict__ 里删除指定的key


f1 = Foo()
print(f1['name'])  # jack
f1['age'] = 10
print(f1['age'])  # 10
del f1['name']
print(f1.__dict__)  # {'age': 10}
print("*" * 50)


class Parent(object):
    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def p_test(self):
        pass


class Child(Parent):
    a = 4
    b = 5

    def __init__(self):
        super(Child, self).__init__()
        # self.a = 6
        # self.b = 7

    def c_test(self):
        pass

    def p_test(self):
        pass


p = Parent()
c = Child()
print(Parent.__dict__)
print(Child.__dict__)
print(p.__dict__)
print(c.__dict__)

