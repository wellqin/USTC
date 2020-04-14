# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        5.BigFile
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

1.5、生成器在UserList中的应用
"""
from abc import abstractmethod
from collections import UserList  # UserList中继承的序列Sequence中的__iter__里面就运用生成器实现的数据迭代


# Sequence中的__iter__源码
class Sequence:  # class Sequence(Sized, Iterable, Container):

    def __getitem__(self, i):
        return self[i]

    def __setitem__(self, i, item):
        self[i] = item

    def __iter__(self):
        i = 0
        try:  # list遍历逻辑，利用yield v 保存栈帧
            while True:
                v = self[i]
                yield v  # 注意生成器
                i += 1
        except IndexError:
            return


class Company:
    def __getitem__(self, item):
        pass

    def __iter__(self):
        pass


company = Company()
iter(company)  # 调用iter的时候，会去对象中寻找__iter__,如果没有的话就去寻找__getitem__

# 生成器在list中的应用，如果我们要继承list的话，就继承UserList，因为list是C语言写出来的，UserList是利用python写出来的。
# 我们可以覆盖UserList的任意函数
