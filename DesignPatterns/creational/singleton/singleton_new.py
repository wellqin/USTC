# -*- coding:utf-8 -*-
import threading
import time

import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


if __name__ == '__main__':
    # 采用这种方式的单例模式，以后实例化对象时，和平时实例化对象的方法一样obj = Singleton()
    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()
