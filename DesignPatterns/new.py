# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        new
Description :   
Author :          wellqin
date:             2019/7/30
Change Activity:  2019/7/30
-------------------------------------------------
"""
import threading
class Solution(object):
    def __new__(cls, *args, **kwargs):
        print("allow mem")

    def __init__(self):
        print("init")

foo = Solution()
print(foo)  # allow mem
            # None   为什么是None？
print("===================================================")

class Solution1(object):
    def __new__(cls, *args, **kwargs):
        print("allow mem")
        print(cls)

        ins = super().__new__(cls)

        return ins

    def __init__(self):
        print("init")

foo1 = Solution1()
print(foo1)  # allow mem
            # None   为什么是None？

print("===================================================")


# python中单例模式

"""
class sig(object):
    pass

s1 = sig()
print(s1)

s2 = sig()
print(s2)

<__main__.sig object at 0x00000197AB33F208>
<__main__.sig object at 0x00000197AB33F240>
"""

# python中单例模式

class sig1(object):
    """
    饿汉式单例模式实现
    预先加载，急切初始化，单例对象在类实例化前创建。

    优点:
    1. 线程安全
    2. 在类实例化前已经创建好一个静态对象，调用时反应速度快
    3. 直接执行其他方法或静态方法时，单例实例不会被初始化

    缺点:
    1. 不管使用与否，实例化前就初始化静态对象，有点资源浪费; ( 其实不算是大毛病)
    """
    instance = None  # 记录对象引用

    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性instance是否为空
        if cls.instance is None:

            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        if sig1.init_flag:
            return

        print("init")

        sig1.init_flag = True

# s1 = sig1()
# print(s1)
#
# s2 = sig1()
# print(s2)


def task(arg):
    obj = sig1()
    print(obj, arg)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

"""
init
<__main__.sig1 object at 0x000001A8EABFB470>
init
<__main__.sig1 object at 0x000001A8EABFB470>

"""

class Singleton(object):
    """
    # 懒汉模式: 只有在使用时才创建单例对象，实例化时不创建
    保证了需要使用的时候才创建对象。（防止导入模块，但没有使用，造成的浪费）
    优点:
    1. 资源利用合理，不调用 get_instance 方法不创建单例对象
    缺点:
    1. 线程不安全，多线程时可能会获取到不同单例对象的情况。解决办法是加互斥锁，但会降低效率
    """
    _instance = None

    def __init__(self):
        if not hasattr(Singleton, '_instance'):
            print("__init__ method called, but no instance created")
        else:
            print("instance already created:", self._instance)

    @classmethod
    def get_instance(cls):  # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
                            # 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
        if not cls._instance:
            cls._instance = Singleton()
        return cls._instance































