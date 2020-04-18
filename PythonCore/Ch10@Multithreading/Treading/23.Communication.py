# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        23.Communication
Description :   
Author :          wellqin
date:             2020/4/16
Change Activity:  2020/4/16
-------------------------------------------------

1.3、线程间通信-共享变量和Queue
线程间的通信方式第一种就是共享变量，共享变量就像上面第一个例子那样共享一个全局变量，但这种共享变量有缺点，这是线程不安全的状态。
结果与预期值不一样。那么有没有一种线程安全的方式呢？

当然有，那就是queue--同步队列类，Python 的 Queue 模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
该queue模块实现了多生产者，多消费者队列（生产者消费者模型）。当必须在多个线程之间安全地交换信息时，它在线程编程中特别有用。
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。


在这里就只设计到queue.Queue（maxsize = 0 ），maxsize是一个整数，用于设置可以放入队列中的项目数的上限。
一旦达到此大小，插入将被阻塞，直到消耗队列项目为止。如果maxsize小于或等于零，则队列大小为无限。
其他另外两个队列(后入先出)LifoQueue、(优先级队列)PriorityQueue根据需求来选择队列。

Queue.qsize() #返回队列的大小
Queue.empty() #如果队列为空，返回True,反之False
Queue.full() #如果队列满了，返回True,反之False
Queue.full #与 maxsize 大小对应
Queue.get([block[, timeout]]) #获取队列，timeout等待时间
Queue.get_nowait() #相当Queue.get(False)
Queue.put(item) #写入队列，timeout等待时间
Queue.put_nowait(item) #相当Queue.put(item, False)
Queue.task_done() #在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() # 实际上意味着等到队列阻塞执行完毕为空，再执行别的操作
"""

# 通过queue的方式进行线程间同步
from queue import Queue
import time
import threading


def get_detail_html(queue):
    # 文章详情页
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get url：{url}".format(url=url))


def get_detail_url(queue):
    # 文章列表页
    print("get detail url started")
    time.sleep(1)
    for i in range(20):
        queue.put("http://cnblogs.com/lishuntao/{id}".format(id=i))
        queue.task_done()  # 需要配合queue.join()使用
    print("get detail url end")


if __name__ == "__main__":
    queue = Queue(maxsize=1000)  # maxsize是一个整数，用于设置可以放入队列中的项目数的上限。一旦达到此大小，插入将被阻塞，直到消耗队列项目为止。

    # 文章列表页,task_done()
    thread_detail_url = threading.Thread(target=get_detail_url, args=(queue,))  # 将实例化的Queue作为参数传入
    thread_detail_url.start()

    # 文章详情页
    for i in range(5):  # 五个线程共用数据
        html_thread = threading.Thread(target=get_detail_html, args=(queue,))
        html_thread.start()
    start_time = time.time()
    queue.join()  # 阻塞等待队列中任务全部处理完毕，需要配合queue.task_done使用
    print("last time: {}".format(time.time() - start_time))

    """
    阻塞直到队列中的所有项目都已获取并处理。
    每当将项目添加到任务中时，未完成任务的数量就会增加队列。每当使用者线程调用task_done（）时，计数就会减少
    表示已检索到该项目，并且所有工作已完成。当未完成的任务数降至零时，join（）解除阻止
    """
