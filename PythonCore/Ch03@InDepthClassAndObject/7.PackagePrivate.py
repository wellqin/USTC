# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        PackagePrivate
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------
1.7、数据封装和私有属性
    导入的Date是上面1.6 StaticClassMethod 写的类：
"""

from PythonCore.Chapter03.StaticClassMethod import Date  # 注意命名


class User:
    def __init__(self, birthday):
        self.__birthday = birthday  # 在属性前面加上双下划线，
        # 就变成了私有属性，外面实例化对象不能直接访问,子类都不能使用私有属性.只能用公共方法调用

    def get_age(self):
        """
        希望用户看不见出生日期(我们提供计算年龄的接口)在这里只能用公共方法调用，子类都不能使用私有属性
        :return: 返回用户年龄，
        """
        return 2019 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1999, 9, 9))
    # print(user.__birthday)  # AttributeError: 'User' object has no attribute '__birthday'

    print(user._User__birthday)  # 1999/9/9  如果想要访问那么对象名._classname__attr就可以获取python的私有属性
    # _classname__attr好处：在继承关系中，对象被覆盖时，也能通过classname找到

    print(user.get_age())  # 20
    # 从语言的角度来讲，没有绝对的私有属性的安全性的，都是可以突破的，
