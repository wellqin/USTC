# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.EventLoop
Description :   
Author :          wellqin
date:             2020/4/20
Change Activity:  2020/4/20
-------------------------------------------------

一. 事件循环

asyncio完成的功能：

包含各种特定系统实现的模块化事件循环
传输和协议抽象
对TCP, UDP, SSL、子进程、延时调用以及其他的具体支持
模仿futures模块但适用于事件循环使用的Future类
基于yield from的协议和任务,可以让你用顺序的方式编写并发代码
必须使用一个将产生阻塞IO的调用时,有接口可以把这个事件转移到线程池
模仿threading模块中的同步原语、可以用在单线程内的协程之间


1.注：
实现搭配：事件循环 + 回调（驱动生成器【协程】） + epoll（IO多路复用）

asyncio是Python用于解决异步编程的一整套解决方案；
基于asynico的框架：tornado，gevent，twisted（Scrapy，django channels）。
其中tornado（实现了web服务器，可以直接部署，真正部署还是要加nginx），django，flask（uwsgi，gunicorn + nginx部署）
"""

import asyncio
import time
from functools import partial  # partial将函数进行包装


# 1. 事件循环示例
# 先定义一个协程async，必须搭配事件循环才可以使用，asyncio实现了事件循环
# async def get_html(url):
#     print('start get url')
#     await asyncio.sleep(2)
#     print('end get url')
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()  # 不像之前我们自己写的loop逻辑
#     task = [get_html('www.baidu.com') for i in range(10)]
#     # run_until_complete 运行事件循环，直到完成Future。返回Future的结果，或引发其异常。
#     loop.run_until_complete(asyncio.wait(task))  # 把协程注册到事件循环上，直到它执行完
#     print(time.time() - start_time)


# 2.如何获取协程的返回值（和线程池类似）
async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')
    return "AHA"


# 需要接收task，如果要接收其他的参数就需要用到partial(偏函数),参数需要放到前面
def callback(url, future):  # future就是task
    print(url + ' success')
    print('send email')


def callbackNO(future):  # 无参数
    print('send email')


if __name__ == '__main__':
    start_time = time.time()
    # # 1.获取协程的返回值的第一种方式：ensure_future
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(get_html('www.baidu.com'))  # 也可以
    # # ensure_future原理还是获取event_loop，没有loop会自动获取，然后调用create_task方法，一个线程只有一个loop
    # # 其中run_until_complete可以接收future类型，task类型（是future类型的一个子类），也可以接收可迭代类型
    # loop.run_until_complete(get_future)
    # print(time.time() - start_time)
    # print(get_future.result())  # AHA
    #
    # # 2.获取协程的返回值的第二种方式：create_task
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(get_html('www.baidu.com'))
    # loop.run_until_complete(task)
    # print(time.time() - start_time)
    # print(task.result())  # AHA

    # 情景：任务get_html完成后，需要额外处理时，可以加上回调函数callback
    # 3.获取协程的返回值的第三种方式：add_done_callback与callback
    # 3.1 callback无参数的情况，默认传task
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html('www.baidu.com'))
    task.add_done_callback(callbackNO)  # 这里只接受方法名，而不接受方法的参数，用下面的partial
    loop.run_until_complete(task)
    print(task.result())  # AHA

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(get_html('www.baidu.com'))
    # task.add_done_callback(partial(callback, 'www.baidu.com'))
    # loop.run_until_complete(task)
    # print(task.result())  # AHA
