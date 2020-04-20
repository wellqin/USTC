# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        74.YieldFrom
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------

4.yield from：（Python 3.3新加的语法） --  很难理解
"""

from itertools import chain

my_list = [1, 2, 3]
my_dict = {'name1': '1',
           'name2': '2'}


# 将所有值遍历输出
# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)


# yield from iterable
def my_chain(*args, **kwargs):
    for my_iterable in args:
        # 功能非常多
        # 1. yield方式
        for value in my_iterable:
            yield value

        # 1. yield from 方式
        # 语法: yield from iterable
        # yield from my_iterable


for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


# 再看一次
def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable  # 将可迭代对象中的值全部拿出来


for value in g1(range(10)):
    print(value)  # range(0, 10)

for value in g2(range(10)):
    print(value)  # 0 1 2 3 4 5 6 7 8 9
