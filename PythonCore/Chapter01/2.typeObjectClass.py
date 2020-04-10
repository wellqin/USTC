# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        typeObjectClass
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
https://www.cnblogs.com/lishuntao/
-------------------------------------------------
Python 为所有类都提供了一个 bases 属性，通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的元组。注意是直接父类！！！
所以每一个类有一个__bases__属性，列出其直接父类，不包括祖父类。但是类的实例是没有__bases__属性

type、object和class的关系

type用法：1.生成一个类  2. 返回对象的类型
object是最顶层的基类，所有类默认继承于它。type(object)=type，即object类这个对象是由type生成的，object.__bases__为空
type也是一个类，同时也是一个对象。它的基类是object。

type、object感觉已经形成了一个环路
"""

a = 11  # type(a) <class 'int'>  可以理解为int类实现了a这个对象
# 同时int类也是一个对象，type(int)为<class 'type'>，可认为int类这个对象是由type类生成的
# type >> int >> 11
# type >> class >> obj
b = "abc"
c = [1, 2]  # list类的实例
d = {"a": 2}


class Students:  # 我们自定义的类相当于type这个类生成的对象
    pass


class MyStudents(Students):
    pass


stu = Students()

print(type(d))  # <class 'dict'>
print(type(dict))  # <class 'type'>
#                                                    **: type==>list==>c
print(type(a))  # <class 'int'>                      **: type==>dict==>d
print(type(int))  # <class 'type'>                   **: type==>int==>a
print(type(b))  # <class 'str'>                      **: type==>str==>b
print(type(str))  # <class 'type'>                   **: type==>Students==>object

print(type(stu))  # <class '__main__.Students'>      **: type==>type==>MyStudents==>Students==>object
print(type(Students))  # <class 'type'>              **: type类的基类是object，object的基类是空，object的类型是type类，

# 由此可以总结出他们之间的关系
print(int.__bases__)  # (<class 'object'>,)
print(str.__bases__)  # (<class 'object'>,)
print(Students.__bases__)  # (<class 'object'>,)
print(MyStudents.__bases__)  # (<class '__main__.Students'>,)

print(type.__bases__)  # (<class 'object'>,)
print(object.__bases__)  # ()
print(type(object))  # <class 'type'>
