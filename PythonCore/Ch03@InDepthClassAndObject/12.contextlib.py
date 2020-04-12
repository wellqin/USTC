# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        12.contextlib
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------
2.2、contextlib简化上下文管理器
    在之前定义上下文管理器，需要定义一个类，然后在类中实现__enter__方法和__exit__方法，那可否简化呢？
"""

import contextlib
# 修饰的函数必须是生成器：yield


@contextlib.contextmanager  # 装饰器将函数变为上下文管理器（上下文管理器都可以用with用）
def file_open(filename):
    print("file open")  # yield之前的相当于__enter__函数的操作
    yield {}
    print("file end")   # yield之后相当于__exit__函数的操作


# with file_open("test.txt") as fp:
#     print("file open processing")
    """
    运行结果：
    file open
    file open processing
    file end
    """


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextlib.contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


create_query("wellqin")

