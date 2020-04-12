# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        dataModel
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------
1.2、Python的数据模型以及数据模型对Python的影响
要成为一名高级的开发工程师，就需要对Python的内部源码做一定的理解，这样当自己定义类的时候，才会更加灵活的定义。
"""


class Students(object):
    def __init__(self, student_list):
        self.student = student_list

    def __getitem__(self, item):  # 给类增加了可迭代的属性
        return self.student[item]

    def __len__(self):
        return len(self.student)  # 这里一定要返回的是正整数


students = Students(["lishuntao", "wang", "li"])
print(len(students))  # 当注释掉len魔法方法运行出现错误TypeError: object of type 'Students' has no len()
# 当有len魔法函数的时候，运行出现值3

students1 = students[:2]  # 没有__len__也可以执行
print(len(students1))

"""
在使用python的len函数的时候，尽量去使用python原生的类型（list、set、dict），这些类型性能很高.
CPython是用C语言写出来的，因此效率很高。再用python语法去写的话，效率会大大下降。
因为魔法函数内部会做很多优化，大大提升效率。
"""

