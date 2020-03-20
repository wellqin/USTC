# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        素数
Description :   
Author :          wellqin
date:             2020/3/19
Change Activity:  2020/3/19
-------------------------------------------------
"""
from math import sqrt


# 使用isPrime函数  素数：一个大于1的正整数，除了1和它自身外，再没有其它因子的自然数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


count = 0
for i in range(101):
    if isPrime(i):
        count += 1
print(count)


def is_prime(n):
    # 当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句。
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return
    else:
        return n


res = list(map(is_prime, range(2, 101)))
print(len(res))
print([i for i in res if i])
