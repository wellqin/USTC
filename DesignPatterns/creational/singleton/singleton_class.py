# -*- coding:utf-8 -*-
import threading
import time


def task(arg):
    obj = SingletonBest.instance()  # 如果用obj=Singleton() , 这种方式得到的不是单例
    print(obj)


class Singleton(object):

    def __init__(self):
        # 看起来也没有问题，那是因为执行速度过快，如果在 init 方法中有一些 IO 操作，就会发现问题了，下面我们通过 time.sleep 模拟
        # 问题出现了！按照以上方式创建的单例，无法支持多线程
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(SingletonBest, "_instance"):
            SingletonBest._instance = SingletonBest(*args, **kwargs)
        return SingletonBest._instance


def task_thread(arg):
    obj = SingletonThread.instance()
    print(obj)


class SingletonThread(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(0.1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with SingletonThread._instance_lock:
            if not hasattr(SingletonThread, "_instance"):
                SingletonThread._instance = SingletonThread(*args, **kwargs)
        return SingletonThread._instance


class SingletonBest(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(SingletonBest, "_instance"):
            with SingletonBest._instance_lock:
                if not hasattr(SingletonBest, "_instance"):
                    SingletonBest._instance = SingletonBest(*args, **kwargs)
        return SingletonBest._instance


if __name__ == '__main__':
    """
    这种方式实现的单例模式，使用时会有限制，以后实例化必须通过obj = Singleton.instance()  
    如果用obj=Singleton() , 这种方式得到的不是单例
    """
    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()
    # 问题出现了！按照以上方式创建的单例，无法支持多线程
    # 解决办法：加锁！未加锁部分并发执行, 加锁部分串行执行, 速度降低, 但是保证了数据安全
    print("============支持多线程版本============")
    for i in range(10):
        t = threading.Thread(target=task_thread, args=[i, ])
        t.start()

    # 这样就差不多了，但是还是有一点小问题，就是当程序执行时，执行了 time.sleep(20) 后，下面实例化对象时，此时已经是单例模式了，
    # 但我们还是加了锁，这样不太好，再进行一些优化，把 intance 方法，改成下面的这样就行：SingletonBest
