# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        6-多线程-共享全局变量
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

from threading import Thread
import time

g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print("----in work1, g_num is %d---" % g_num)


def work2():
    global g_num
    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---"%g_num)


t1 = Thread(target=work1)
t1.start()
# 延时⼀会，保证t1线程中的事情做完
time.sleep(1)
t2 = Thread(target=work2)
t2.start()

"""
---线程创建之前g_num is 100---
----in work1, g_num is 103---
----in work2, g_num is 103---
"""
