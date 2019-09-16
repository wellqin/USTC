# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        9-互斥锁
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

"""
互斥锁
当多个线程⼏乎同时修改某⼀个共享数据的时候，需要进⾏同步控制线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引⼊互斥锁。

互斥锁为资源引⼊⼀个状态：锁定/⾮锁定。

某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；直到该线程释放资源，将资源的状态变成“⾮锁定”，其他的
线程才能再次锁定该资源。互斥锁保证了每次只有⼀个线程进⾏写⼊操作，从⽽保证了多线程情况下数据的正确性。
"""
"""

# threading模块中定义了Lock类，可以⽅便的处理锁定：
# 创建锁  mutex = threading.Lock()
# 锁定    mutex.acquire([blocking])
# 释放    mutex.release()

其中，锁定⽅法acquire可以有⼀个blocking参数。如果设定blocking为True，则当前线程会堵塞，直到获取到这个锁为⽌
（如果没有指定，那么默认为False）如果设定blocking为False，则当前线程不会堵塞
"""

from threading import Thread, Lock
import time

g_num = 0


def test1():
    global g_num
    for i in range(1000000):
        # True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这⾥⼀直等待到解锁为⽌
        # False表示⾮堵塞，即不管本次调⽤能够成功上锁，都不会卡在这,⽽是继续执⾏下⾯的代码
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            g_num += 1
        mutex.release()
    print("---test1---g_num=%d" % g_num)


def test2():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True)  # True表示堵塞
        if mutexFlag:
            g_num += 1
        mutex.release()
    print("---test2---g_num=%d" % g_num)

# 创建⼀个互斥锁
# 这个所默认是未上锁的状态


mutex = Lock()   # 默认是未上锁的状态
p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()
print("---g_num=%d---" % g_num)

"""
运⾏结果：
---g_num=48691---
---test1---g_num=1987779
---test2---g_num=2000000
可以看到，加⼊互斥锁后，运⾏结果与预期相符。

acquire(False)时情况
---g_num=96408---
---test2---g_num=658765
---test1---g_num=927444
"""


# 上锁解锁过程
"""
当⼀个线程调⽤锁的acquire()⽅法获得锁时，锁就进⼊“locked”状态。每次只有⼀个线程可以获得锁。如果此时另⼀个线程试图获得这个锁，该线
程就会变为“blocked”状态，称为“阻塞”，直到拥有锁的线程调⽤锁的release()⽅法释放锁之后，锁进⼊“unlocked”状态。

线程调度程序从处于同步阻塞状态的线程中选择⼀个来获得锁，并使得该线程进⼊运⾏（running）状态。
"""


# 总结
"""
锁的好处： 确保了某段关键代码只能由⼀个线程从头到尾完整地执⾏

锁的坏处： 阻⽌了多线程并发执⾏，包含锁的某段代码实际上只能以单线程模式执⾏，效率就⼤⼤地下降了

由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对⽅持有的锁时，可能会造成死锁
"""

"""
with lock:  # with Lock的作用相当于自动获取和释放锁(资源)
    while (c < 100):
        c += 1
        count += 1
        print("{0}: set count to {1}".format(threadName, count))

与
if(lock.acquire()):
        while(c<100):
            c+=1
            count+=1
            print("{0}: set count to {1}".format( threadName, count) )
        lock.release()

二者作用一样的
"""