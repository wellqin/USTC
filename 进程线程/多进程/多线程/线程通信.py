# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/8/25
Change Activity:  2019/8/25
-------------------------------------------------
"""
"""
1.Queue
使用线程队列有一个要注意的问题是，向队列中添加数据项时并不会复制此数据项，线程间通信实际上是在线程间传递对象引用。
如果你担心对象的共享状态，那你最好只传递不可修改的数据结构（如：整型、字符串或者元组）或者一个对象的深拷贝。

Queue 对象提供一些在当前上下文很有用的附加特性。比如在创建 Queue 对象时提供可选的 size 参数来限制可以添加到队列中的元素数量。
对于“生产者”与“消费者”速度有差异的情况，为队列中的元素数量添加上限是有意义的。
比如，一个“生产者”产生项目的速度比“消费者”“消费”的速度快，那么使用固定大小的队列就可以在队列已满的时候阻塞队列，
以免未预期的连锁效应扩散整个程序造成死锁或者程序运行失常。在通信的线程之间进行“流量控制”是一个看起来容易实现起来困难的问题。
如果你发现自己曾经试图通过摆弄队列大小来解决一个问题，这也许就标志着你的程序可能存在脆弱设计或者固有的可伸缩问题。 
get() 和 put() 方法都支持非阻塞方式和设定超时。
"""

# import queue
# q = queue.Queue()
#
# item = "msg"  # queue中消息
#
# try:
#     data = q.get(block=False)
# except queue.Empty:
#     pass
# try:
#     q.put(item, block=False)
# except queue.Full:
#     pass
# try:
#     data = q.get(timeout=5.0)
# except queue.Empty:
#     pass
# print(q)
#
#
# # producer
# def producer(q):
#     """..."""
#     try:
#         q.put(item, block=False)
#     except queue.Full:
#         print('queued item %r discarded!', item)
#
#
# # consumer
# _running = True
# def consumer(q):
#     while _running:
#         try:
#             item = q.get(timeout=5.0)
#             # Process item
#             pass
#         except queue.Empty:
#             pass
# producer(q)
# consumer(q)


"""
同步机制
Event
线程的一个关键特性是每个线程都是独立运行且状态不可预测。如果程序中的其他线程需要通过断某个线程的状态来确定自己下一步的操作，
这时线程同步问题就会变得非常棘手。为了解决这些问题，我们需要使用 threading 库中的 Event 对象。

Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在初始情况下，event 对象中的信号标志被设置假。
如果有线程等待一个 event 对象，而这个 event 对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。
一个线程如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待个 event 对象的线程。
如果一个线程等待一个已经被设置为真的 event 对象，那么它将忽略这个事件，继续执行。
"""

# from threading import Thread, Event
# import time
#
# def countdown(n, start_evt):
#     print('countdown is starting...')
#     start_evt.set()
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(5)
#
# start_evt = Event()  # 可通过Event 判断线程的是否已运行
# t = Thread(target=countdown, args=(10, start_evt))
# t.start()
#
# print('launching countdown...')
# start_evt.wait()  # 等待countdown执行
#
# # event 对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程
#
# print('countdown is running...')

"""
countdown is starting...
T-minus 10
launching countdown...
countdown is running...
T-minus 9
T-minus 8
T-minus 7
T-minus 6
T-minus 5
T-minus 4
T-minus 3
T-minus 2
T-minus 1
"""


"""
Semaphore（信号量）
在多线程编程中，为了防止不同的线程同时对一个公用的资源（比如全部变量）进行修改，
需要进行同时访问的数量（通常是1）的限制。信号量同步基于内部计数器，每调用一次acquire()，计数器减1；
每调用一次release()，计数器加1.当计数器为0时，acquire()调用被阻塞。
"""
from threading import Semaphore, Lock, RLock, Condition, Event, Thread
import time

# 信号量
sema = Semaphore(3)  # 限制同时能访问资源的数量为3


def foo(tid):
    with sema:
        print('{} acquire sema'.format(tid))
        time.sleep(1)
    print('{} release sema'.format(tid))


threads = []

for i in range(5):
    t = Thread(target=foo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

"""
0 acquire sema
1 acquire sema
2 acquire sema
1 release sema
0 release sema
3 acquire sema
4 acquire sema
2 release sema
4 release sema
3 release sema
"""

"""
Lock（锁）
互斥锁为资源引入一个状态：锁定/非锁定。某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，
其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。

互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。

"""
# import threading
# #创建锁
# mutex = threading.Lock()
# #锁定
# mutex.acquire([timeout])
# #释放
# mutex.release()


"""
RLock（可重入锁）
为了支持在同一线程中多次请求同一资源，python提供了“可重入锁”：threading.RLock。
RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次acquire。
直到一个线程所有的acquire都被release，其他的线程才能获得资源。

RLock无法跨线程。需要跨线程就得使用Lock。
"""
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num = num+1
            msg = self.name+' set num to '+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()
num = 0
mutex = threading.RLock()

def test():
    for i in range(5):
        t = MyThread()
        t.start()
test()


"""
Condition（条件变量）
Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。
线程首先acquire一个条件变量，然后判断一些条件。如果条件不满足则wait；如果条件满足，进行一些处理改变条件后，
通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。不断的重复这一过程，
从而解决复杂的同步问题。

可以认为Condition对象维护了一个锁（Lock/RLock)和一个waiting池。线程通过acquire获得Condition对象，
当调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程。
当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁。

Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock。

除了notify方法外，Condition对象还提供了notifyAll方法，可以通知waiting池中的所有线程尝试acquire内部锁。
由于上述机制，处于waiting状态的线程只能通过notify方法唤醒，所以notifyAll的作用在于防止有线程永远处于沉默状态。
"""
import threading
import time

class Producer:
    def run(self):
        global count
        while True:
            if con.acquire():
                if count > 1000:
                    con.wait()
                else:
                    count += 100
                    msg = threading.current_thread().name + ' produce 100, count=' + str(count)
                    print(msg)
                    con.notify()  # 通知 waiting线程池中的线程
                con.release()
                time.sleep(1)

count = 0
con = threading.Condition()

class Consumer:
    def run(self):
        global count
        while True:
            if con.acquire():
                if count < 100:
                    con.wait()
                else:
                    count -= 3
                    msg = threading.current_thread().name + ' consumer 3, count=' + str(count)
                    print(msg)
                    con.notify()
                con.release()
                time.sleep(3)

producer = Producer()
consumer = Consumer()



















