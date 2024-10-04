# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        7-列表当做实参传递到线程中
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

from threading import Thread
import time


def work1(nums):
    nums.append(44)
    print("----in work1---", nums)


def work2(nums):
    # 延时⼀会，保证t1线程中的事情做完
    time.sleep(1)
    print("----in work2---", nums)


g_nums = [11, 22, 33]

t1 = Thread(target=work1, args=(g_nums,))
t1.start()
t2 = Thread(target=work2, args=(g_nums,))
t2.start()

"""
----in work1--- [11, 22, 33, 44]
----in work2--- [11, 22, 33, 44]
"""

"""
在⼀个进程内的所有线程共享全局变量，能够在不适⽤其他⽅式的前提下完成多线程之间的数据共享（这点要⽐多进程要好）
缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程⾮安全）
"""
