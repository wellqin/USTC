# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test_func.py
Description :   
Author :          wellqin
date:             2020/2/8
Change Activity:  2020/2/8
-------------------------------------------------
"""
# 每个测试方法编写的时候，都要以test开头，比如test_square，否则是不被unitest识别的
# 特别说明的一点是，测试的执行顺序跟方法的顺序没有关系，四个测试是随机先后执行的


def add(a, b):
    return a + b


def multi(a, b):
    return a * b


def lower_str(string):
    return string.lower()


def square(x):
    return x ** 2
