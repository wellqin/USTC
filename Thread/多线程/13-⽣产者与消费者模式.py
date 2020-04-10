# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        13-⽣产者与消费者模式
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

"""
Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先⼊先出)队列Queue，LIFO（后⼊先出）队列LifoQueue，和优先级队列
PriorityQueue。这些队列都实现了锁原语（可以理解为原⼦操作，即要么不做，要么就做完），能够在多线程中直接使⽤。

可以使⽤队列来实现线程间的同步。⽤FIFO队列实现上述⽣产者与消费者问题的代码如下：

1. 对于Queue，在多线程通信之间扮演重要的⻆⾊
2. 添加数据到队列中，使⽤put()⽅法
3. 从队列中取数据，使⽤get()⽅法
4. 判断队列中是否还有数据，使⽤qsize()⽅法
"""
import threading
import time
# python2中
# from Queue import Queue
# python3中
from queue import Queue

# 通过阻塞队列来进⾏通讯,消除二者之间的耦合
class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '⽣成产品'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了 '+queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()
    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()

"""
⽣产者消费者模式的说明

为什么要使⽤⽣产者和消费者模式

在线程世界⾥，⽣产者就是⽣产数据的线程，消费者就是消费数据的线程。
在多线程开发当中，如果⽣产者处理速度很快，⽽消费者处理速度很慢，那
么⽣产者就必须等待消费者处理完，才能继续⽣产数据。同样的道理，如果
消费者的处理能⼒⼤于⽣产者，那么消费者就必须等待⽣产者。为了解决这
个问题于是引⼊了⽣产者和消费者模式。

什么是⽣产者消费者模式
⽣产者消费者模式是通过⼀个容器来解决⽣产者和消费者的强耦合问题。⽣
产者和消费者彼此之间不直接通讯，⽽通过阻塞队列来进⾏通讯，所以⽣产
者⽣产完数据之后不⽤等待消费者处理，直接扔给阻塞队列，消费者不找⽣
产者要数据，⽽是直接从阻塞队列⾥取，阻塞队列就相当于⼀个缓冲区，平
衡了⽣产者和消费者的处理能⼒。

这个阻塞队列就是⽤来给⽣产者和消费者解耦的。纵观⼤多数设计模式，都
会找⼀个第三者出来进⾏解耦，
"""