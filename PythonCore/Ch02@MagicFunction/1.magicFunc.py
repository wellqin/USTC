# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        magicFunc
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------
1.1、什么是魔法函数

魔法函数就是以双下划线开头，双下划线结尾。
第二点就是必须使用Python提供给我们的魔法函数，不能自己定义。
魔法函数是与自定义的类有关的，目的是为了增强自定义类的特性。

例如：__getitem__不是继承自object的方法，也不是自定义类的特有属性，而是python固有的，增强自定义类的特性。
定义了魔法函数后，可以让我们的类很神奇，比如原来的Company类对象，在定义魔法函数后，竟然变得可以迭代类属性！！！
"""


class Company:
    def __init__(self, emp_list):
        self.emp = emp_list

    def __getitem__(self, item):  # 传入索引，从零开始，如果没有值了就停止运行。
        # 如果将此魔法方法注释掉会报错TypeError: 'Students' object is not iterable
        return self.emp[item]     # 增加此魔法方法给类增加了可迭代的属性


# 没有魔法函数时，获取元素操作: 遍历对象实例的属性
company = Company(["Tom", "bob", "jane"])
emploee = company.emp
for i in emploee:
    print(i, end='')

# 有魔法函数时，获取元素操作: 直接遍历对象实例
print()
for i in company:  # company不可以迭代，但是__getitem__可以使得其可以迭代
    print(i, end='')
