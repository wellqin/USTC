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






























