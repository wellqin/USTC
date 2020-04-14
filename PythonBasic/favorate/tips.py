# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        tips
Description :   
Author :          wellqin
date:             2020/3/10
Change Activity:  2020/3/10
-------------------------------------------------
"""
# 1. 字符串的翻转
from functools import reduce

str1 = "hello world"
print(str1[::-1])  # dlrow olleh
print(reduce(lambda x, y: y + x, str1))  # dlrow olleh

str2 = "hello world"
print(str1 == str2)
