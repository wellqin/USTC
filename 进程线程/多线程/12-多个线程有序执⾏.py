# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        12-多个线程有序执⾏
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""
# 可以使⽤互斥锁完成多个任务，有序的进程⼯作，这就是线程的同步
from threading import Thread, Lock
from time import sleep


class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():   # lock1没有“锁上”，这里执行lock1.acquire()的结果为True，则可以向下执行
                print("------Task 1 -----")
                sleep(0.5)
                lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():  # lock2“锁上”，这里执行lock1.acquire()是不成功的，为False阻塞
                print("------Task 2 -----")
                sleep(0.5)
                lock3.release()


class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("------Task 3 -----")
                sleep(0.5)
                lock1.release()


# 使⽤Lock创建出的锁默认没有“锁上”
lock1 = Lock()
# 创建另外⼀把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()

# 创建另外⼀把锁，并且“锁上”
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()

"""
------Task 1 -----
------Task 2 -----
------Task 3 -----
------Task 1 -----
------Task 2 -----
------Task 3 -----
------Task 1 -----
------Task 2 -----
------Task 3 -----
------Task 1 -----
------Task 2 -----
------Task 3 -----
------Task 1 -----
------Task 2 -----
------Task 3 -----
------Task 1 -----
...
"""
