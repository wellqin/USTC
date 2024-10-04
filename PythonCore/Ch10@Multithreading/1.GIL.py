# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.GIL
Description :   
Author :          wellqin
date:             2020/4/15
Change Activity:  2020/4/15
-------------------------------------------------

1.1、Python中的GIL锁
CPython中，global interpreter lock（简称GIL）是一个互斥体，用于保护对Python对象的访问，
从而防止多个线程一次执行Python字节码,一次只有一个线程在一个CPU上执行字节码，无法将多个线程映射到多个CPU执行
（也就是说，GIL锁每次只能允许一个线程工作，无法多个线程同时在CPU上工作）。

多个线程运行同一段代码是可能出错的。

锁定是必要的，主要是因为CPython的内存管理不是线程安全的。
（但是，由于存在GIL，因此其他功能已经变得越来越依赖于它所执行的保证。）

CPython扩展必须支持GIL，以避免破坏线程。GIL之所以引起争议，是因为它在某些情况下阻止多线程CPython程序充分利用多处理器系统。
请注意，潜在的阻塞或长时间运行的操作（例如I/O，图像处理和NumPy数字运算）发生在GIL之外。
因此，只有在GIL内部花费大量时间来解析CPython字节码的多线程程序中，GIL才成为瓶颈。但是即使不是瓶颈，GIL也会降低性能。

总结这些：系统调用开销很大，尤其是在多核硬件上。两个线程调用一个函数所花的时间可能是单个线程两次调用该函数所花时间的两倍。
GIL可以导致I / O绑定线程被调度在CPU绑定线程之前。并且它阻止了信号的传递。
"""

import threading

num = 0


def add():
    global num
    for i in range(1000000):
        num += 1


def desc():
    global num
    for i in range(1000000):
        num -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()  # 运行线程1
thread2.start()

thread1.join()  # 让线程1运行完毕才进行下一步
thread2.join()  # 让线程2运行完毕才进行下一步
print(num)  # -197054
# 打印的结果应该是0，但是每次打印的结果都不一样，这说明线程没有按照要求一个一个运行完毕才进行下一个
# GIL会根据执行的字节码行数以及时间片释放GIL，GIL在遇到I/O的操作时候也会主动释放GIL
# （也就是说，当线程1遇到I/O操作的时候，会释放GIL切换到线程2运行）

# 所以：多线程之间需要同步，不是安全的

# python多线程实际上是同一时刻只有一个线程运行的，而且线程也不会按照要求一个一个运行完毕才进行下一个，
# GIL会根据执行的字节码行数以及时间片释放GIL，以实现线程的切换。

# 但是GIL在遇到I/O的操作时候也会主动释放GIL，这样在多个线程执行时
# 遇到IO阻塞的，可以在阻塞这段时间内运行其他线程的程序，以实现快速高效操作，类似多线程效果。
