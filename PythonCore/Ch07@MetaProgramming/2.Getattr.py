# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.Getattr
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.2、__getattr__、__getattribute__魔法函数

# __getattr__, __getattribute__
# __getattr__ 就是在查找不到属性的时候调用,如果没有这个魔法函数会报错
  即访问函数不存在的属性，如果没有__getattr__，就会报错

# __getattribute__则是无条件第一进入此魔法函数，不管能不能找到属性
  因此能不写这个魔法函数就不写，写框架会用到这个魔法函数
"""

from datetime import date


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        return "not find"


user = Person("lisha", date(year=1998, month=11, day=1))
# 访问函数不存在的属性，如果没有__getattr__，就会报错
print(user.age)  # AttributeError: 'Person' object has no attribute 'age'
# 有__getattr__,则返回有__getattr__中内容
print(user.age)  # not find


class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    # def __getattribute__(self, item):  # 无条件优先进入这个魔法函数内，不会先寻找其他属性
    #     return "lishuntao"


if __name__ == "__main__":
    user = User(info={"company_name": "alibaba", "name": "lisha"})
    print(user.company_name)  # 如果没有此属性会进入__getattr__魔法函数，
