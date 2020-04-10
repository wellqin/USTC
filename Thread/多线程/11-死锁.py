# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        11-死锁
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

"""
在线程间共享多个资源的时候，如果两个线程分别占有⼀部分资源并且同时等待对⽅的资源，就会造成死锁。

尽管死锁很少发⽣，但⼀旦发⽣就会造成应⽤的停⽌响应。下⾯看⼀个死锁的例⼦

# 锁定    mutex.acquire([blocking])（如果没有指定，那么默认为True）
"""

import threading
import time


class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name + '----do1---up----')
            time.sleep(1)
            if mutexB.acquire():   #
                print(self.name + '----do1---down----')
                mutexB.release()
            mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name+'----do2---up----')
            time.sleep(1)
            if mutexA.acquire():
                print(self.name+'----do2---down----')
                mutexA.release()
            mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()
if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()  # 此时已经进⼊到了死锁状态，可以使⽤ctrl-z退出

"""
Thread-1----do1---up----
Thread-2----do2---up----
"""

"""
3. 避免死锁
程序设计时要尽量避免（银⾏家算法）
添加超时时间等
"""

"""
解决方法，递归锁：在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。

直到一个线程所有的acquire都被release，其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁
"""
