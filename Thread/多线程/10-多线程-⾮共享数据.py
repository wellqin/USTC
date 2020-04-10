# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        10-多线程-⾮共享数据
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

# 对于全局变量，在多线程中要格外⼩⼼，否则容易造成数据错乱的情况发⽣

# 1. ⾮全局变量是否要加锁呢？
# 在多线程开发中，全局变量是多个线程都共享的数据，⽽局部变量等是各⾃线程的，是⾮共享的

import threading
import time


class MyThread(threading.Thread):
    # 重写 构造⽅法
    def __init__(self, num, sleepTime):
        threading.Thread.__init__(self)
        self.num = num
        self.sleepTime = sleepTime

    def run(self):
        self.num += 1
        time.sleep(self.sleepTime)
        print('线程(%s),num=%d' % (self.name, self.num))


if __name__ == '__main__':
    mutex = threading.Lock()
    t1 = MyThread(100, 5)
    t1.start()
    t2 = MyThread(200, 1)
    t2.start()

"""
线程(Thread-2),num=201
线程(Thread-1),num=101
说明每个线程数据不一样，有各自的数据
"""
from time import sleep


def test(sleepTime):
    num = 1
    sleep(sleepTime)
    num += 1
    print('---(%s)--num=%d'%(threading.current_thread(), num))


t1 = threading.Thread(target=test, args=(5,))
t2 = threading.Thread(target=test, args=(1,))
t1.start()
t2.start()

"""
---(<Thread(Thread-2, started 26228)>)--num=2
---(<Thread(Thread-1, started 4552)>)--num=2
"""
