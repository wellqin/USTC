# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        反射
Description :   
Author :          wellqin
date:             2019/9/16
Change Activity:  2019/9/16
-------------------------------------------------
"""


# 什么是反射？可以用字符串的方式去访问对象的属性
# 反射是程序执行时检查其所拥有的结构。尤其是类型的一种能力。这是元编程的一种形式。它同一时候也是造成混淆的重要来源。


class Test:
    _name = "sss"

    def fun(self):
        return "Helloword"


t = Test()
# print(hasattr(t,"_name"))   # hasattr(obj, name) # 查看类里面有没有name属性
# print(hasattr(t,"fun"))  #True

if hasattr(t, "_name"):
    print(getattr(t, "_name"))  # sss
if hasattr(t, "fun"):
    print(getattr(t, "fun")())  # Helloword
    if not hasattr(t, "age"):  # 如果属性不存在
        print("没有该属性和方法，我来给设置一个")
        setattr(t, "age", "18")  # 给t对象设置一个默认值，默认age=18
        print(getattr(t, "age"))
