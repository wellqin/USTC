#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/10 17:04
@Author  : qinwei05
"""


# 创建一个函数，只有函数在调用的时候才会运行
def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


# factorial(42)是函数function的实例
print(factorial(42))
print(type(factorial))

# 函数众多属性中的其中一个
print(factorial.__doc__)
