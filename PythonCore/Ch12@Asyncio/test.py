#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/5 16:35
@Author  : qinwei05
"""

import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)


def callback(future):  # 回调函数
    ret = future.result()
    if ret:
        print('Callback: ', ret)
    return 'Callback return' + ret


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)  # task = loop.create_task(coroutine)
task.add_done_callback(callback)  # 添加回调函数
loop.run_until_complete(task)
print(task.result())

print('TIME: ', now() - start)
