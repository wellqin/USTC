# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        并发打印
Description :   
Author :          wellqin
date:             2019/9/10
Change Activity:  2019/9/10
-------------------------------------------------
"""
import threading
import time

"""
在python的原始解释器CPython中存在着GIL（Global Interpreter Lock，全局解释器锁），
因此在解释执行python代码时，会产生互斥锁来限制线程对共享资源的访问，
直到解释器遇到I/O操作或者操作次数达到一定数目时才会释放GIL。

所以，虽然CPython的线程库直接封装了系统的原生线程，但CPython整体作为一个进程，
同一时间只会有一个获得GIL的线程在跑，其他线程则处于等待状态。这就造成了即使在多核CPU中，
多线程也只是做着分时切换而已。 不过muiltprocessing的出现，
已经可以让多进程的python代码编写简化到了类似多线程的程度了。

怎么解决GIL:
1、能用进程（可以并行）不用线程。
2、高效的代码（多线程执行的任务，想并行的）使用c，c++来编写

"""

# 创建两个线程，其中一个输出1-52，另外一个输出A-Z。输出格式要求：12A 34B 56C 78D
# 大致思路
# 获取对方的锁，运行一次后，释放自己的锁


def show1():
    for i in range(1, 52, 2):
        lock_show2.acquire()
        print(i, end='')
        print(i + 1, end='')
        time.sleep(0.2)
        lock_show1.release()


def show2():
    for i in range(26):
        lock_show1.acquire()
        print(chr(i + ord('A')))
        time.sleep(0.2)
        lock_show2.release()


lock_show1 = threading.Lock()
lock_show2 = threading.Lock()

show1_thread = threading.Thread(target=show1)
show2_thread = threading.Thread(target=show2)

lock_show1.acquire()  # 因为线程执行顺序是无序的，保证show1()先执行

show1_thread.start()
show2_thread.start()

