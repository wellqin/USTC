# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        6.Coroutine
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19

协程：可以解决回调编写难的问题
-------------------------------------------------

C10M问题和协程

1.C10M问题：
如何利用8核心CPU，64G内存，在10gps的网络上保持1000万的并发连接。

2.协程：
2.1问题：
    回调模式编码复杂度高；
    同步编程的并发性不高；
    多线程需要线程间同步，lock会降低性能

2.2解决：
    采用同步的方式去编写异步的代码；
    采用单线程去解决任务：线程是由操作系统切换，单线程切换意味着需要我们自己去调度任务；不在需要锁，并发性高，
    如果单线程内切换函数，性能远高于线程切换，并发性更高。

2.3协程：
    传统函数调用 过程 A->B->C；
    我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行；
    出现了协程 -> 有多个入口的函数， 可以暂停的函数， 可以暂停的函数(可以向暂停的地方传入值)；
    原理：生成器
"""
import time
from urllib3.util import parse_url


def get_html(n):
    time.sleep(n)
    print("success")
    return n


def get_url(url):
    # do someting 1
    html = get_html(url)  # 耗时操作，此处可否暂停，切换到另一个函数去执行
    # parse html
    urls = parse_url(html)


def get_url1(url):
    # do someting 1
    html = get_html(url)  # 此处暂停，切换到另一个函数去执行
    # parse html
    urls = parse_url(html)
