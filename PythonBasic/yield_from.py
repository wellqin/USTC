# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        yield_from
Description :   
Author :          wellqin
date:             2020/2/11
Change Activity:  2020/2/11
-------------------------------------------------
"""
from collections import namedtuple

Result = namedtuple("Result", "count average")

li = [40.9, 38.5, 44.3]


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


# 委派生成器
def grouper(result, key):
    while True:
        result[key] = yield from averager()


# 调用方
def main():
    results = {}
    group = grouper(results, "kg")
    next(group)
    for value in li:
        group.send(value)
    group.send(None)


if __name__ == "__main__":
    main()
