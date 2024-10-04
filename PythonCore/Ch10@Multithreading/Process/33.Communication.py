# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        33.Communication
Description :   
Author :          wellqin
date:             2020/4/18
Change Activity:  2020/4/18
-------------------------------------------------

2.0、进程间通信 -- 【 Queue、Pipe，Manager（共享内存）】

多进程之间的通信，不能运用多线程提供的queue.Queue。
为了解决这个，多进程自己提供了一个multiprocessing.Queue。进程的用法和线程用法类似。

多进程之间是不能共享全局变量的，然而多线程是可以共享全局变量的。

多进程的数据是完全隔离的，当在linux/unix中fork数据的时候，在进程中的变量完全复制一份，复制到子进程中，
这样两边的数据是互不影响的。还有multiprocessing中的queue不能用于pool进程池的。

那么谁能用于进程池中呢？multiprocessing.Manager.Queue提供了可以用于进程池间的通信。

"""

"""
总结：
    XX 共享全局变量通信，不能用于多进程编程，可用于多线程 XX
    
    1.Queue通信：
    普通进程方式:用multiprocessing.Queue，而不是多线程的queue.Queue
    线程池pool方式：用manager中的queue，multiprocessing中的queue不能用于pool进程池的
    所以有三种Queue：queue  |  multiprocessing.Queue  |  manager.queue
            【多线程专用】        【普通进程方式】         【线程池pool方式】
    
    2.Pipe（只能适用于两个进程之间的通信）：pipe性能高于queue
    
    3.进程间共享内存
"""

import time
from multiprocessing import Process, Queue
from multiprocessing import Pool, Manager
from multiprocessing import Process, Pipe
from multiprocessing import Process, Manager

# from queue import Queue 不是这个Queue，在多进程不可以，多线程可以


"""1.mutiprocessing.Queue（进程间的通信Queue）"""
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)  # 2
#
#
# if __name__ == "__main__":
#     queues = Queue(10)
#     my_producer = Process(target=producer, args=(queues,))
#     my_consumer = Process(target=consumer, args=(queues,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


"""1.1 pool方式中的进程间通信需要使用manager中的queue"""
# multiprocessing.Manager.Queue（进程池间通信Manager）
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)  # 2
#
#
# if __name__ == "__main__":
#     queues = Manager().Queue(10)
#     pool = Pool(2)
#
#     pool.apply_async(producer, args=(queues,))
#     pool.apply_async(consumer, args=(queues,))
#     # 等待完成
#     pool.close()
#     pool.join()


"""2.通过pipe实现二个进程间通信"""
# pipe的性能高于queue

# def producer(pipe):
#     pipe.send("lisha")  # pipe发送数据
#
#
# def consumer(pipe):
#     print(pipe.recv())  # pipe接收数据
#
#
# if __name__ == "__main__":
#     recevie_pipe, send_pipe = Pipe()  # 实例化的时候是两个参数
#
#     # pipe只能适用于两个进程
#     my_producer = Process(target=producer, args=(send_pipe,))
#     my_consumer = Process(target=consumer, args=(recevie_pipe,))
#
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


"""3.进程间共享内存"""


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    progress_dict = Manager().dict()  # 还有许多种数据类型

    first_progress = Process(target=add_data, args=(progress_dict, "lisha", 22))
    second_progress = Process(target=add_data, args=(progress_dict, "lichen", 18))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_dict)  # {'lichen': 18, 'lisha': 22}
