#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/6 19:35
@Author  : qinwei05
"""
import dis


def myfunc(alist):
    """
    字节码测试函数
    @param alist:
    @return:
    """
    return len(alist)


print(dis.dis(myfunc))
