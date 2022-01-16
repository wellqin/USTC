# -*- coding:utf-8 -*-
import threading
import time

"""
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""


class FooExample:
    def __init__(self):
        print("FooExample.__init__")

    def __call__(self, *args, **kwargs):
        print("FooExample.__call__")


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    obj = FooExample()
    obj()

    obj1 = Foo('name')
    obj2 = Foo('name')
    print(obj1, obj2)
