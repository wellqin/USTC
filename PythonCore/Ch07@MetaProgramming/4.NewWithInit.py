# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.NewWithInit
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.4、__new__和__init__的区别
"""


class User:
    def __new__(cls, *args, **kwargs):  # 在对象生成之前的一些操作，所以有参数cls
        print("new")
        print(args)  # ('li',)  ()
        return super().__new__(cls)  # 注释后，就不会执行__init__函数

    def __init__(self, name):  # new方法不返回对象， 则不会调用__init__函数
        self.name = name
        print("init")
        pass


a = int()
# new 是用来控制对象的生成过程， 在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象， 则不会调用__init__函数

user1 = User("li")  # 传入__new__元祖，('li',)
user = User(name="li")  # 指定name后，传入__init__的参数name
"""
new 
init
"""

# 拓展，单例模式
"""
我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象；
然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式

采用这种方式的单例模式，以后实例化对象时，和平时实例化对象的方法一样 obj = Singleton() 
"""

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


for i in range(10):
    t = threading.Thread(target=task, args=[i])
    t.start()

"""
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
<__main__.Singleton object at 0x000001F9992388D0>
"""
