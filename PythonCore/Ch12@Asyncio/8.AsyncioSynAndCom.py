# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        8.AsyncioSynAndCom
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------
asyncio同步和通信

1.单线程协程不需要锁
2.某种情况需要锁
"""

import asyncio

total = 0


# 1. 单线程协程不需要锁，不涉及IO等操作的，执行完了再执行其他代码
async def add():
    global total
    for i in range(1000000):
        total += 1


async def decs():
    global total
    for i in range(1000000):
        total -= 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [add(), decs()]
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)  # 0


# 2. 某种情况需要锁
import asyncio, aiohttp
# aiohttp requires Python '>=3.5.3' but the running Python is 3.5.2
# 这是并没有调用系统的锁，只是简单的自己实现（注意是非阻塞的）,Queue也是非阻塞的,都用了yield from，不用用到condition【单线程】】
# Queue还可以限流，如果只需要通信还可以直接使用全局变量否则可以
from asyncio import Lock, Queue  # 没有Rlock，因为协程为单线程


# Queue可用于通信与限流
catche = {}
lock = Lock()


async def get_stuff(url):
    # 实现了__enter__和__exit__两个魔法函数，可以用with
    # with await lock:
    # 更明确的语法__aenter__和__await__
    async with lock:  # 注意是asyncio的Lock，不是线程的
        # 注意加await,是一个协程
        # await lock.acquire()
        for url in catche:
            return catche[url]
        # 异步的接收
        stauff = aiohttp.request('Get', url)
        catche[url] = stauff
        return stauff
        # lock.release()  # release是一个简单的函数


async def parse_stuff():
    stuff = await get_stuff()


async def use_stuff():
    stuff = await get_stuff()


# 如果没有同步机制，就会发起两次请求（这里就可以加一个同步机制）
tasks = [parse_stuff(), use_stuff()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
