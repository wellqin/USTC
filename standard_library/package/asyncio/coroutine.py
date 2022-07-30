#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/5 17:43
@Author  : qinwei05
"""

import asyncio
import time


async def say_after(delay, what):
    print(delay)
    await asyncio.sleep(delay)
    print(what)


async def main():
    # print(f"started at {time.strftime('%X')}")
    #
    # await say_after(1, 'hello')
    # await say_after(2, 'world')
    #
    # print(f"finished at {time.strftime('%X')}")
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    print("mid")
    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
