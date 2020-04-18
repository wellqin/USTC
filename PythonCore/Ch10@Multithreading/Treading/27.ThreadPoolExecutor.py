# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        27.ThreadPoolExecutor
Description :   
Author :          wellqin
date:             2020/4/18
Change Activity:  2020/4/18
-------------------------------------------------

为什么要使用ThreadPoolExecutor？

ThreadPoolExecutor提供了一个简单的抽象，围绕多个线程并使用这些线程以并发方式执行任务。
在正确的上下文中使用线程时，向您的应用程序添加线程可以帮助极大地提高应用程序的速度。
通过使用多个线程，我们可以加快面对基于I/O操作型的应用程序，网络爬虫就是一个很好的例子。
Web爬取网页程序通常会执行很多繁重的基于I/O的任务，例如获取和解析网站，如果我们要以同步方式获取每个页面，
您会发现程序的主要瓶颈就是从互联网上获取这些页面 。

通过使用诸如ThreadPoolExecutor之类的东西，我们可以通过同时执行多个读取并在返回每个页面时对其进行处理来有效地缓解此瓶颈。
"""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future


# 为什么要使用线程池ThreadPoolExecutor？
# Future为未来对象，或者说是task的返回容器
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致
def get_html(times):
    time.sleep(times)
    print("get page {}".format(times))
    return times


# pool = ThreadPoolExecutor(max_workers=2)  # max_workers 最大同时并发数，默认是操作系统的核的数量
# # 通过submit函数提交执行的函数到线程池中, submit是立即返回，非阻塞
# task1 = pool.submit(get_html, 3)
# task2 = pool.submit(get_html, 2)
#
# # 1. 要获取已经成功的task的返回，# 初级用法 ***
# # done方法用于判定某个任务是否完成，完成返回True，没有完成返回False
# print(task1.done())  # False
# print(task2.cancel())  # False，能不能取消，如果线程已经执行了时不能取消的
# time.sleep(4)
# print(task1.done())  # True
# # result方法可以获取task的执行结果（即函数的返回结果），它是阻塞的
# print(task1.result())

# 2. 要获取已经成功的task的返回，# 高级用法--as_completed ***，其返回是谁先执行完成，先返回谁
pool = ThreadPoolExecutor(max_workers=2)  # max_workers 最大同时并发数，默认是操作系统的核的数量
urls = [2, 3, 4]
allTask = [pool.submit(get_html, url) for url in urls]
# wait(allTask)  # 主线程会等待所有allTask中线程执行完毕，再执行主线程
wait(allTask, return_when=FIRST_COMPLETED)  # return_when有很多选项，此处表示当第一个线程完成的时候，继续运行主线程
print("main")
for future in as_completed(allTask):
    data = future.result()  # result是一个阻塞的方法，result(self, timeout=None):
    print("get {} page success".format(data))
    """
    本来不加wait，谁先执行完成，先返回谁
    get page 2
    get 2 page success
    get page 3
    get 3 page success
    get page 4
    get 4 page success
    
    # 加上wait，等待所有allTask中线程执行完毕，再执行主线程
    get page 2
    get page 3
    get page 4
    get 2 page success
    get 3 page success
    get 4 page success
    """

# 3. 通过线程池map获取已经成功的task的返回，map返回顺序与urls中一致
# for data in pool.map(get_html, urls):
#     print("get {} page success".format(data))


# 上下文管理器实例化：
# 高级用法
# def task(n):
#     time.sleep(3)
#     print("Processing {}".format(n))
#
#
# def main():
#     print("Starting ThreadPoolExecutor")
#     # 上下文管理器实例化ThreadPoolExecutor(线程池)对象
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         for i in range(4):
#             future = executor.submit(task, (i))
#     print("All tasks complete")
#
#
# main()

