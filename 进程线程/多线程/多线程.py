# # -*- coding: utf-8 -*-
# """
# -------------------------------------------------
# File Name:        多线程
# Description :
# Author :          wellqin
# date:             2019/8/22
# Change Activity:  2019/8/22
# -------------------------------------------------
# """
# """
# == == == == ==
# == 多进程 ==
# == == == == ==
# 要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
#
# Unix / Linux操作系统提供了一个fork()
# 系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()
# 调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()
# 就可以拿到父进程的ID。
#
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
# """
# # multiprocessing.py
# import os
#
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# """
# 运行结果如下：
#
# Process(876)
# start...
# I(876)
# just
# created
# a
# child
# process(877).
# I
# am
# child
# process(877) and my
# parent is 876.
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
#
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
#
# multiprocessing
# 如果你打算编写多进程的服务程序，Unix / Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
#
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
# """
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Process will start.')
    p.start()
    p.join()
    print('Process end.')
# 执行结果如下：
#
# Parent
# process
# 928.
# Process
# will
# start.
# Run
# child
# process
# test(929)...
# Process
# end.
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()
# 方法启动，这样创建进程比fork()
# 还要简单。
#
# join()
# 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#
# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
#
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print
#     'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print
#     'Task %s runs %0.2f seconds.' % (name, (end - start))
#
#
# if __name__ == '__main__':
#     print
#     'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print
#     'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print
#     'All subprocesses done.'
# 执行结果如下：
#
# Parent
# process
# 669.
# Waiting
# for all subprocesses done...
# Run
# task
# 0(671)...
# Run
# task
# 1(672)...
# Run
# task
# 2(673)...
# Run
# task
# 3(674)...
# Task
# 2
# runs
# 0.14
# seconds.
# Run
# task
# 4(673)...
# Task
# 1
# runs
# 0.27
# seconds.
# Task
# 3
# runs
# 0.86
# seconds.
# Task
# 0
# runs
# 1.41
# seconds.
# Task
# 4
# runs
# 1.91
# seconds.
# All
# subprocesses
# done.
# 代码解读：
#
# 对Pool对象调用join()
# 方法会等待所有子进程执行完毕，调用join()
# 之前必须先调用close()，调用close()
# 之后就不能继续添加新的Process了。
#
# 请注意输出的结果，task
# 0，1，2，3
# 是立刻执行的，而task
# 4
# 要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
#
# p = Pool(5)
# 就可以同时跑5个进程。
#
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
#
# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
#
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码:
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print
#         'Put %s to queue...' % value
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读数据进程执行的代码:
# def read(q):
#     while True:
#         value = q.get(True)
#         print
#         'Get %s from queue.' % value
#
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
# 运行结果如下：
#
# Put
# A
# to
# queue...
# Get
# A
# from queue.
#
# Put
# B
# to
# queue...
# Get
# B
# from queue.
#
# Put
# C
# to
# queue...
# Get
# C
# from queue.
#
# 在Unix / Linux下，multiprocessing模块封装了fork()
# 调用，使我们不需要关注fork()
# 的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去。
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
#
# 小结
# 在Unix / Linux下，可以使用fork()
# 调用实现多进程。
#
# 要实现跨平台的多进程，可以使用multiprocessing模块。
#
# 进程间通信是通过Queue、Pipes等实现的。
#
# == == == == ==
# == 多线程 ==
# == == == == ==
# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
#
# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
#
# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix
# Thread，而不是模拟出来的线程。
#
# Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
#
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()
# 开始执行：
#
# import time, threading
#
#
# # 新线程执行的代码:
# def loop():
#     print
#     'thread %s is running...' % threading.current_thread().name
#     n = 0
#     while n < 5:
#         n = n + 1
#         print
#         'thread %s >>> %s' % (threading.current_thread().name, n)
#         time.sleep(1)
#     print
#     'thread %s ended.' % threading.current_thread().name
#
#
# print
# 'thread %s is running...' % threading.current_thread().name
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print
# 'thread %s ended.' % threading.current_thread().name
# 执行结果如下：
#
# thread
# MainThread is running...
# thread
# LoopThread is running...
# thread
# LoopThread >> > 1
# thread
# LoopThread >> > 2
# thread
# LoopThread >> > 3
# thread
# LoopThread >> > 4
# thread
# LoopThread >> > 5
# thread
# LoopThread
# ended.
# thread
# MainThread
# ended.
# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()
# 函数，它永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
# 如果不起名字Python就自动给线程命名为Thread - 1，Thread - 2……
#
# Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享。
# 所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：
#
# import time, threading
#
# # 假定这是你的银行存款:
# balance = 0
#
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print
# balance
# 我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，
# 当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
#
# 原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
#
# balance = balance + n
# 也分两步：
#
# 计算balance + n，存入临时变量中；
# 将临时变量的值赋给balance。
# 也就是可以看成：
#
# x = balance + n
# balance = x
# 由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
#
# 初始值
# balance = 0
#
# t1: x1 = balance + 5  # x1 = 0 + 5 = 5
# t1: balance = x1  # balance = 5
# t1: x1 = balance - 5  # x1 = 5 - 5 = 0
# t1: balance = x1  # balance = 0
#
# t2: x2 = balance + 8  # x2 = 0 + 8 = 8
# t2: balance = x2  # balance = 8
# t2: x2 = balance - 8  # x2 = 8 - 8 = 0
# t2: balance = x2  # balance = 0
#
# 结果
# balance = 0
# 但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
#
# 初始值
# balance = 0
#
# t1: x1 = balance + 5  # x1 = 0 + 5 = 5
#
# t2: x2 = balance + 8  # x2 = 0 + 8 = 8
# t2: balance = x2  # balance = 8
#
# t1: balance = x1  # balance = 5
# t1: x1 = balance - 5  # x1 = 5 - 5 = 0
# t1: balance = x1  # balance = 0
#
# t2: x2 = balance - 5  # x2 = 0 - 5 = -5
# t2: balance = x2  # balance = -5
#
# 结果
# balance = -5
# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
#
# 两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
#
# 如果我们要确保balance计算正确，就要给change_it()
# 上一把锁，当某个线程开始执行change_it()
# 时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，
# 只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
# 创建一个锁就是通过threading.Lock()
# 来实现：
#
# balance = 0
# lock = threading.Lock()
#
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()
#
#
# 当多个线程同时执行lock.acquire()
# 时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
#
# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
#
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
# 其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
#
# 多核CPU
# 如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。
#
# 如果写一个死循环的话，会出现什么情况呢？
#
# 打开Mac
# OS
# X的Activity
# Monitor，或者Windows的Task
# Manager，都可以监控某个进程的CPU使用率。
#
# 我们可以监控到一个死循环线程会100 % 占用一个CPU。
#
# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200 % 的CPU，也就是占用两个CPU核心。
#
# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
#
# 试试用Python写个死循环：
#
# import threading, multiprocessing
#
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有160 %，也就是使用不到两核。
#
# 即使启动100个线程，使用率也就170 % 左右，仍然不到两核。
#
# 但是用C、C + +或Java来改写相同的死循环，直接可以把全部核心跑满，4
# 核就跑到400 %，8
# 核就跑到800 %，为什么Python不行呢？
#
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global
# Interpreter
# Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，
# 解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
# 也只能用到1个核。
#
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
#
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
#
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
#
# 小结
# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
#
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
#
# == == == == == == == =
# == ThreadLocal ==
# == == == == == == == =
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
#
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
#
# def process_student(name):
#     std = Student(name)
#     # std是局部变量，但是每个函数都要用它，因此必须传进去：
#     do_task_1(std)
#     do_task_2(std)
#
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
#
# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)
#
#
# 每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。
#
# 如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
#
# global_dict = {}
#
#
# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
#
#
# def do_task_1():
#     # 不传入std，而是根据当前线程查找：
#     std = global_dict[threading.current_thread()]
#     ...
#
#
# def do_task_2():
#     # 任何函数都可以查找出当前线程的std变量：
#     std = global_dict[threading.current_thread()]
#     ...
#
#
# 这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。
#
# 有没有更简单的方式？
#
# ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
#
# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
#
# def process_student():
#     print
#     'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# 执行结果：
#
# Hello, Alice( in Thread - A)
# Hello, Bob( in Thread - B)
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，
# 但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
#
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
#
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
#
# == == == == == == =
# == 分布式进程 ==
# == == == == == == =
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
#
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。
# 由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
#
# 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。
# 怎么用分布式进程实现？
#
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
#
# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
#
# # taskmanager.py
#
# import random, time, Queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
# task_queue = Queue.Queue()
# # 接收结果的队列:
# result_queue = Queue.Queue()
#
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
#
# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey='abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
# 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()
# 获得的Queue接口添加。
#
# 然后，在另一台机器上启动任务进程（本机上启动也可以）：
#
# # taskworker.py
#
# import time, sys, Queue
# from multiprocessing.managers import BaseManager
#
#
# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
#
# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')
#
# # 连接到服务器，也就是运行taskmanager.py的机器:
# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与taskmanager.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey='abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n * n)
#         time.sleep(1)
#         result.put(r)
#     except Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')
# 任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。
#
# 现在，可以试试分布式进程的工作效果了。先启动taskmanager.py服务进程：
#
# $ python
# taskmanager.py
# Put
# task
# 3411...
# Put
# task
# 1605...
# Put
# task
# 1398...
# Put
# task
# 4729...
# Put
# task
# 5300...
# Put
# task
# 7471...
# Put
# task
# 68...
# Put
# task
# 4219...
# Put
# task
# 339...
# Put
# task
# 7866...
# Try
# get
# results...
# taskmanager进程发送完任务后，开始等待result队列的结果。现在启动taskworker.py进程：
#
# $ python
# taskworker.py
# 127.0
# .0
# .1
# Connect
# to
# server
# 127.0
# .0
# .1...
# run
# task
# 3411 * 3411...
# run
# task
# 1605 * 1605...
# run
# task
# 1398 * 1398...
# run
# task
# 4729 * 4729...
# run
# task
# 5300 * 5300...
# run
# task
# 7471 * 7471...
# run
# task
# 68 * 68...
# run
# task
# 4219 * 4219...
# run
# task
# 339 * 339...
# run
# task
# 7866 * 7866...
# worker
# exit.
# taskworker进程结束，在taskmanager进程中会继续打印出结果：
#
# Result: 3411 * 3411 = 11634921
# Result: 1605 * 1605 = 2576025
# Result: 1398 * 1398 = 1954404
# Result: 4729 * 4729 = 22363441
# Result: 5300 * 5300 = 28090000
# Result: 7471 * 7471 = 55815841
# Result: 68 * 68 = 4624
# Result: 4219 * 4219 = 17799961
# Result: 339 * 339 = 114921
# Result: 7866 * 7866 = 61873956
# 这个简单的Manager / Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，
# 比如把计算n * n的代码换成发送邮件，就实现了邮件队列的异步发送。
#
# Queue对象存储在哪？注意到taskworker.py中根本没有创建Queue的代码，所以，Queue对象存储在taskmanager.py进程中。
#
# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
#
# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果taskworker.py的authkey和taskmanager.py的authkey不一致，肯定连接不上。
#
# 小结
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
#
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，
# 由Worker进程再去共享的磁盘上读取文件。
#
# == == == == ==
# == 异步IO ==
# == == == == ==
# 1.
# 协程：
# 考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，
# 因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。
#
# 现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，
# 这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，
# 可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。
#
# 对应到Python语言，单进程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。
#
# Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。
# 在学习异步IO模型前，我们先来了解协程。
#
# 协程，又称微线程，纤程。英文名Coroutine。
#
# 协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。
#
# 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
#
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
#
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
#
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
#
# 注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：
#
# def A():
#     print('1')
#     print('2')
#     print('3')
#
#
# def B():
#     print('x')
#     print('y')
#     print('z')
#
#
# 假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：
#
# 1
# 2
# x
# y
# 3
# z
# 但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。
#
# 看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
#
# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#
# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程 + 协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
#
# Python对协程的支持是通过generator实现的。
#
# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()
# 函数获取由yield语句返回的下一个值。
#
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
#
# 来看例子：
#
# 传统的生产者 - 消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
#
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
#
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)
# 执行结果：
#
# [PRODUCER]
# Producing
# 1...
# [CONSUMER]
# Consuming
# 1...
# [PRODUCER]
# Consumer
# return: 200
# OK
# [PRODUCER]
# Producing
# 2...
# [CONSUMER]
# Consuming
# 2...
# [PRODUCER]
# Consumer
# return: 200
# OK
# [PRODUCER]
# Producing
# 3...
# [CONSUMER]
# Consuming
# 3...
# [PRODUCER]
# Consumer
# return: 200
# OK
# [PRODUCER]
# Producing
# 4...
# [CONSUMER]
# Consuming
# 4...
# [PRODUCER]
# Consumer
# return: 200
# OK
# [PRODUCER]
# Producing
# 5...
# [CONSUMER]
# Consuming
# 5...
# [PRODUCER]
# Consumer
# return: 200
# OK
# 注意到consumer函数是一个generator，把一个consumer传入produce后：
# 首先调用c.send(None)
# 启动生成器；
# 然后，一旦生产了东西，通过c.send(n)
# 切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()
# 关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
# 最后套用Donald
# Knuth的一句话总结协程的特点：
# “子程序就是协程的一种特例。”
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 2.
# gevent
# gevent是第三方库，通过greenlet实现协程，其基本思想是：
#
# 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，
# 有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
#
# 由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey
# patch完成：
#
# from gevent import monkey;
#
# monkey.patch_socket()
# import gevent
#
#
# def f(n):
#     for i in range(n):
#         print
#         gevent.getcurrent(), i
#
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()
# 运行结果：
#
# < Greenlet
# at
# 0x10e49f550: f(5) > 0
# < Greenlet
# at
# 0x10e49f550: f(5) > 1
# < Greenlet
# at
# 0x10e49f550: f(5) > 2
# < Greenlet
# at
# 0x10e49f550: f(5) > 3
# < Greenlet
# at
# 0x10e49f550: f(5) > 4
# < Greenlet
# at
# 0x10e49f910: f(5) > 0
# < Greenlet
# at
# 0x10e49f910: f(5) > 1
# < Greenlet
# at
# 0x10e49f910: f(5) > 2
# < Greenlet
# at
# 0x10e49f910: f(5) > 3
# < Greenlet
# at
# 0x10e49f910: f(5) > 4
# < Greenlet
# at
# 0x10e49f4b0: f(5) > 0
# < Greenlet
# at
# 0x10e49f4b0: f(5) > 1
# < Greenlet
# at
# 0x10e49f4b0: f(5) > 2
# < Greenlet
# at
# 0x10e49f4b0: f(5) > 3
# < Greenlet
# at
# 0x10e49f4b0: f(5) > 4
# 可以看到，3
# 个greenlet是依次运行而不是交替运行。
#
# 要让greenlet交替运行，可以通过gevent.sleep()
# 交出控制权：
#
# def f(n):
#     for i in range(n):
#         print
#         gevent.getcurrent(), i
#         gevent.sleep(0)
#
#
# 执行结果：
#
# < Greenlet
# at
# 0x10cd58550: f(5) > 0
# < Greenlet
# at
# 0x10cd58910: f(5) > 0
# < Greenlet
# at
# 0x10cd584b0: f(5) > 0
# < Greenlet
# at
# 0x10cd58550: f(5) > 1
# < Greenlet
# at
# 0x10cd584b0: f(5) > 1
# < Greenlet
# at
# 0x10cd58910: f(5) > 1
# < Greenlet
# at
# 0x10cd58550: f(5) > 2
# < Greenlet
# at
# 0x10cd58910: f(5) > 2
# < Greenlet
# at
# 0x10cd584b0: f(5) > 2
# < Greenlet
# at
# 0x10cd58550: f(5) > 3
# < Greenlet
# at
# 0x10cd584b0: f(5) > 3
# < Greenlet
# at
# 0x10cd58910: f(5) > 3
# < Greenlet
# at
# 0x10cd58550: f(5) > 4
# < Greenlet
# at
# 0x10cd58910: f(5) > 4
# < Greenlet
# at
# 0x10cd584b0: f(5) > 4
# 3
# 个greenlet交替运行，
#
# 把循环次数改为500000，让它们的运行时间长一点，然后在操作系统的进程管理器中看，线程数只有1个。
#
# 当然，实际代码里，我们不会用gevent.sleep()
# 去切换协程，而是在执行到IO操作时，gevent自动切换，代码如下：
#
# from gevent import monkey;
#
# monkey.patch_all()
# import gevent
# import urllib2
#
#
# def f(url):
#     print('GET: %s' % url)
#     resp = urllib2.urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data), url))
#
#
# gevent.joinall([
#     gevent.spawn(f, 'https://www.python.org/'),
#     gevent.spawn(f, 'https://www.yahoo.com/'),
#     gevent.spawn(f, 'https://github.com/'),
# ])
# 运行结果：
#
# GET: https: // www.python.org /
# GET: https: // www.yahoo.com /
# GET: https: // github.com /
# 45661
# bytes
# received
# from https: // www.python.org /.
# 14823
# bytes
# received
# from https: // github.com /.
# 304034
# bytes
# received
# from https: // www.yahoo.com /.
# 从结果看，3
# 个网络操作是并发执行的，而且结束顺序不同，但只有一个线程。
#
# 小结
# 使用gevent，可以获得极高的并发性能，但gevent只能在Unix / Linux下运行，在Windows下不保证正常安装和运行。
# 由于gevent是基于IO切换的协程，所以最神奇的是，我们编写的Web
# App代码，不需要引入gevent的包，也不需要改任何代码，仅仅在部署的时候，用一个支持gevent的WSGI服务器，立刻就获得了数倍的性能提升。
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 3.
# asyncio
# asyncio是Python
# 3.4
# 版本引入的标准库，直接内置了对异步IO的支持。
#
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
#
# 用asyncio实现Hello
# world代码如下：
#
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
#
#
# @asyncio.coroutine把一个generator标记为coroutine类型
#
# ，然后，我们就把这个coroutine扔到EventLoop中执行。
#
# hello()
# 会首先打印出Hello
# world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()
# 也是一个coroutine，所以线程不会等待asyncio.sleep()，
# 而是直接中断并执行下一个消息循环。当asyncio.sleep()
# 返回时，线程就可以从yield
# from拿到返回值（此处是None），然后接着执行下一行语句。
#
# 把asyncio.sleep(1)
# 看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
#
# 我们用Task封装两个coroutine试试：
#
# import threading
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# 观察执行过程：
#
# Hello
# world! (< _MainThread(MainThread, started 140735195337472) >)
# Hello
# world! (< _MainThread(MainThread, started 140735195337472) >)
# (暂停约1秒)
# Hello
# again! (< _MainThread(MainThread, started 140735195337472) >)
# Hello
# again! (< _MainThread(MainThread, started 140735195337472) >)
# 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
#
# 如果把asyncio.sleep()
# 换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
#
# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
#
# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# 执行结果如下：
#
# wget
# www.sohu.com...
# wget
# www.sina.com.cn...
# wget
# www
# .163.com...
# (等待一段时间)
# (打印出sohu的header)
# www.sohu.com
# header > HTTP / 1.1
# 200
# OK
# www.sohu.com
# header > Content - Type: text / html
# ...
# (打印出sina的header)
# www.sina.com.cn
# header > HTTP / 1.1
# 200
# OK
# www.sina.com.cn
# header > Date: Wed, 20
# May
# 2015
# 04: 56:33
# GMT
# ...
# (打印出163的header)
# www
# .163.com
# header > HTTP / 1.0
# 302
# Moved
# Temporarily
# www
# .163.com
# header > Server: Cdn
# Cache
# Server
# V2
# .0
# ...
# 可见3个连接由一个线程通过coroutine并发完成。
#
# 小结
# asyncio提供了完善的异步IO支持；
# 异步操作需要在coroutine中通过yield
# from完成；
# 多个coroutine可以封装成一组Task然后并发执行。
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 4.
# async / await
# 用asyncio提供的 @ asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield
# from调用另一个coroutine实现异步操作。
#
# 为了简化并更好地标识异步IO，从Python
# 3.5
# 开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
#
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#
# 把 @ asyncio.coroutine替换为async；
# 把yield
# from替换为await。
# 让我们对比一下上一节的代码：
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
#
# 用新语法重新编写如下：
#
# async def hello():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")
#
#
# 剩下的代码保持不变。
#
# 小结
# Python从3
# .5
# 版本开始为asyncio提供了async和await的新语法.
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 5.
# aiohttp
# asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，
# 因此可以用单线程 + coroutine实现多用户的高并发支持。
#
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
#
# 我们先安装aiohttp：
#
# pip
# install
# aiohttp
# 然后编写一个HTTP服务器，分别处理以下URL：
#
# / - 首页返回b
# '<h1>Index</h1>'；
#
# / hello / {name} - 根据URL参数返回文本hello, % s!。
#
# 代码如下：
#
# import asyncio
#
# from aiohttp import web
#
#
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>')
#
#
# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = '<h1>hello, %s!</h1>' % request.match_info['name']
#     return web.Response(body=text.encode('utf-8'))
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print('Server started at http://127.0.0.1:8000...')
#     return srv
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
# 注意aiohttp的初始化函数init()
# 也是一个coroutine，loop.create_server()
# 则利用asyncio创建TCP服务。
#
