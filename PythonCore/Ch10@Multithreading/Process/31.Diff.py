# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        31.Diff
Description :   
Author :          wellqin
date:             2020/4/18
Change Activity:  2020/4/18
-------------------------------------------------
1.8、多线程和多进程对比
多线程与多进程的对比，当遇到I/O操作的时候（例如爬虫，读文件等），多线程的速度优于多进程，进程切换代价大。
当遇到计算密集型操作【耗费CPU操作】的时候（耗费CPU的操作，例如计算），多进程优于多线程。
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


# 1、计算密集型（运用多进程）
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# if __name__ == "__main__":  # Windows下一定要加，否则异常
#     with ProcessPoolExecutor(3) as executor:  # ProcessPoolExecutor替换成ThreadPoolExecutor
#         # 多进程：25s  ||  多线程：47s
#         all_task = [executor.submit(fib, num) for num in range(25, 40)]
#         start_time = time.time()
#         for future in as_completed(all_task):  # 返回一个迭代器，跟map()不同，这个迭代器的迭代顺序依照all_task返回（线程结束）的顺序。
#             data = future.result()
#             print("exe result: {}".format(data))
#
#         print("last time is: {}".format(time.time() - start_time))


# 2. 对于IO操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        # 多进程：20s  ||  多线程：20s
        all_task = [executor.submit(random_sleep, num) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time() - start_time))
#
#     """
#     executor.map(func, list)
#     第一个参数为只接受一个参数的函数，后一个为可迭代对象。
#     这个map方法会把对函数的调用映射到到多个线程中。并返回一个future的迭代器。
#     """
