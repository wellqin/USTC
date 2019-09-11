# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        15-异步
Description :   
Author :          wellqin
date:             2019/9/12
Change Activity:  2019/9/12
-------------------------------------------------
"""

from multiprocessing import Pool
import time
import os


def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"


def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)


if __name__ == '__main__':
    pool = Pool(3)
    pool.apply_async(func=test, callback=test2)
    time.sleep(5)
    print("----主进程-pid=%d----" % os.getpid())

"""
---进程池中的进程---pid=24164,ppid=27124--
----0---
----1---
----2---
---callback func--pid=27124
---callback func--args=hahah
----主进程-pid=27124----
"""
