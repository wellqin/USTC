# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        多线程引入
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------

如果你的代码是CPU密集型，多个线程的代码很有可能是线性执行的。所以这种情况下多线程是鸡肋，效率可能还不如单线程因为有context switch

但是：如果你的代码是IO密集型，多线程可以明显提高效率。例如制作爬虫（我就不明白为什么Python总和爬虫联系在一起…不过也只想起来这个例子…），
绝大多数时间爬虫是在等待socket返回数据。这个时候C代码里是有release GIL的，最终结果是某个线程等待IO的时候其他线程可以继续执行。

反过来讲：你就不应该用Python写CPU密集型的代码…效率摆在那里…

如果确实需要在CPU密集型的代码里用concurrent，就去用multiprocessing库。这个库是基于multi process实现了类multi thread的API接口，
并且用pickle部分地实现了变量共享。

再加一条，如果你不知道你的代码到底算CPU密集型还是IO密集型，教你个方法：

multiprocessing这个module有一个dummy的sub module，它是基于multithread实现了multiprocessing的API。

假设你使用的是multiprocessing的Pool，是使用多进程实现了concurrency

from multiprocessing import Pool

如果把这个代码改成下面这样，就变成多线程实现concurrency

from multiprocessing.dummy import Pool

两种方式都跑一下，哪个速度快用哪个就行了。

UPDATE:
刚刚才发现concurrent.futures这个东西，包含ThreadPoolExecutor和ProcessPoolExecutor，可能比multiprocessing更简单
"""

"""

Python由于有全锁局的存在（同一时间只能有一个线程执行），并不能利用多核优势。所以，如果你的多线程进程是CPU密集型的，
那多线程并不能带来效率上的提升，相反还可能会因为线程的频繁切换，导致效率下降；
如果是IO密集型，多线程进程可以利用IO阻塞等待时的空闲时间执行其他线程，提升效率。


Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。


python 3中的多进程编程主要依靠threading模块。创建新线程与创建新进程的方法非常类似。
threading.Thread方法可以接收两个参数, 第一个是target，一般指向函数名，第二个时args，需要向函数传递的参数。

对于创建的新线程，调用start()方法即可让其开始。我们还可以使用current_thread().name打印出当前线程的名字。
 下例中我们使用多线程技术重构之前的计算代码。

"""
# import threading
# import time
#
#
# def long_time_task(i):
#     print('当前子线程: {} - 任务{}'.format(threading.current_thread().name, i))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))
#
#
# if __name__ == '__main__':
#     start = time.time()
#     print('这是主线程：{}'.format(threading.current_thread().name))
#     t1 = threading.Thread(target=long_time_task, args=(1,))
#     t2 = threading.Thread(target=long_time_task, args=(2,))
#     t1.start()
#     t2.start()
#
#     end = time.time()
#     print("总共用时{}秒".format((end - start)))

"""
下面是输出结果:

这是主线程：MainThread
当前子线程: Thread-1 - 任务1
当前子线程: Thread-2 - 任务2
总共用时0.0秒
结果: 1152921504606846976
结果: 1152921504606846976

为什么总耗时居然是0秒? 我们可以明显看到主线程和子线程其实是独立运行的，
主线程根本没有等子线程完成，
而是自己结束后就打印了消耗时间。主线程结束后，子线程仍在独立运行，这显然不是我们想要的。
"""

# 如果要实现主线程和子线程的同步，我们必需使用join方法（代码如下所示)。

import threading
import time


def long_time_task(i):
    print('当前子线程: {} 任务{}'.format(threading.current_thread().name, i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__ == '__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))  # current_thread()函数，它永远返回当前线程的实例名
    thread_list = []
    for i in range(1, 3):
        t = threading.Thread(target=long_time_task, args=(i, ))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    end = time.time()
    print("总共用时{}秒".format((end - start)))

"""
这是主线程：MainThread
当前子线程: Thread-1 任务1
当前子线程: Thread-2 任务2
结果: 1152921504606846976
结果: 1152921504606846976
总共用时2.001647710800171秒

修改代码后的输出如下所示。这时你可以看到主线程在等子线程完成后才答应出总消耗时间(2秒)，
比正常顺序执行代码(4秒)还是节省了不少时间。


由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，
子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
"""


"""
进程VS线程


功能
    进程，能够完成多任务，⽐如 在⼀台电脑上能够同时运⾏多个QQ
    线程，能够完成多任务，⽐如 ⼀个QQ中的多个聊天窗⼝
    
    
定义的不同
    进程是系统进⾏资源分配和调度的⼀个独⽴单位.
    线程是进程的⼀个实体,是CPU调度和分派的基本单位,它是⽐进程更⼩的
    能独⽴运⾏的基本单位.线程⾃⼰基本上不拥有系统资源,只拥有⼀点在运
    ⾏中必不可少的资源(如程序计数器,⼀组寄存器和栈),但是它可与同属⼀
    个进程的其他的线程共享进程所拥有的全部资源.


区别
    ⼀个程序⾄少有⼀个进程,⼀个进程⾄少有⼀个线程.
    线程的划分尺度⼩于进程(资源⽐进程少)，使得多线程程序的并发性⾼。
    进程在执⾏过程中拥有独⽴的内存单元，⽽多个线程共享内存，从⽽极
    ⼤地提⾼了程序的运⾏效率
    线线程不能够独⽴执⾏，必须依存在进程中


优缺点
    线程和进程在使⽤上各有优缺点：线程执⾏开销⼩，但不利于资源的管理和
    保护；⽽进程正相反。
"""

