# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.Property
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------
1.1、property动态属性
"""

from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0  # 命名默认规则，表示不想动这个属性，而不是私有属性

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property  # 直接调用属性描述符就可以运行函数（将取函数模式变成取属性模式）
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter  # 修改属性
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User("lisha", date(year=1998, month=11, day=1))
    user.age = 18
    print(user.get_age())  # 22
    print(user._age)  # 18
    print(user.age)   # 22
