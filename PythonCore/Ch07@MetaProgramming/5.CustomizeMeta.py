# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        5.CustomizeMete
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.5、自定义元类


用type动态创建类,例如创建User类
User = type("User", (), {})  # ** 语法：type(object_or_name, bases, dict) **
User = type("User", (BaseClass, ), {"name": "user", "say": say})，其中可以为类添加对象
    "name": "user" 为类属性对象
    "say": say 为类方法对象
    BaseClass 为其父类，继承形式创建
一般在开发中，很少利用type创建类，多用元类形式

什么是元类，元类就是创建类的类 （对象<-class(类对象)<-type）
class MetaClass(type):  # 这个就是元类，继承type（在生成类对象之前做的操作）
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

python中类的实例化过程，会首先寻找metaclass，如果找不到就会去基类中找metaclass，通过metaclass去创建user类
最后都找不到的话，就用默认用type去创建
class User(metaclass=MetaClass):  # metaclass=MetaClass，这可以控制我们类的创建
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"
"""

# 类也是对象，type创建类的类
# 通过字符来动态创建类，但是这种方式不灵活
"""关系：元类---实例化---->类（People）---实例化---->对象（obj）"""


def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


# 改进：用type动态创建类
User = type("User", (), {})  # ** 语法：type(object_or_name, bases, dict) **


def say(self):
    return "I am user"
    # return self.name


class BaseClass:
    def answer(self):
        return "I am baseclass"


# 引入元类 #
class MetaClass(type):  # 这个就是元类，继承type（在生成类对象之前做的操作）
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)  # 元类中，参数与之前super不同


from collections.abc import *


# 什么是元类， 元类是创建类的类 （对象<-class(类对象)<-type）
# python中类的实例化过程，会首先寻找metaclass，如果找不到就会去基类中找metaclass，通过metaclass去创建user类
class User(metaclass=MetaClass):  # metaclass=MetaClass，这可以控制我们类的创建
    def __init__(self, name):
        self.name = name

    def __str__(self):  # 打印对象的字符串形式
        return "user"


if __name__ == "__main__":
    # 原来动态创建类的形式，但是不灵活
    # MyClass = create_class("user")  # 用函数创建类对象
    # my_obj = MyClass()
    # print(my_obj)  # user
    # print(type(my_obj))  # <class '__main__.create_class.<locals>.User'>

    """
    type本身也是继承object的类
    class type(object):
        type(object_or_name, bases, dict) **
        type(object) -> the object's type
        type(name, bases, dict) -> a new type  
    """
    # 改进：用type动态创建类,可见和上面的作用一样
    # User = type("User", (), {})
    # my_obj = User()
    # print(my_obj)  # <__main__.User object at 0x00000193D5247C18>

    # 改进扩展1，加普通参数，即创建类时添加属性
    # User = type("User", (), {"name": "user"})
    # my_obj = User()
    # print(my_obj)  # <__main__.User object at 0x000001B669D68B38>

    # 改进扩展2，加方法参数，即创建类时添加属性
    # User = type("User", (), {"name": "user", "say": say})
    # my_obj = User()
    # print(my_obj.say())  # I am user

    # 改进扩展3，加基类参数，即创建类时不光添加属性，加上方法，还继承了某个基类来创建
    # User = type("User", (BaseClass,), {"name": "user", "say": say})  # type也可以实现类对象（传入参数）
    # my_obj = User()
    # print(my_obj.answer())  # I am baseclass
    # print(my_obj.name)  # user

    # 元类方式
    my_obj = User(name="lisha")
    print(my_obj)  # user

    pass
