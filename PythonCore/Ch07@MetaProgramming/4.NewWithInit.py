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
    def __new__(cls, *args, **kwargs):  # 在对象生成之前的一些操作
        print("new ")
        return super().__new__(cls)

    def __init__(self, name):  # new方法不返回对象， 则不会调用__init__函数
        self.name = name
        print("init")
        pass


a = int()
# new 是用来控制对象的生成过程， 在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象， 则不会调用__init__函数
if __name__ == "__main__":
    user = User(name="li")
    """
    new 
    init
    """
