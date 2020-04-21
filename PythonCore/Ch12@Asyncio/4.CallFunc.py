# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.CallFunc
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------
在asyncio事件循环中调用非协程回调函数
call_soon、call_later、call_at、call_soon_threadsafe

1.call_soon:可以直接接收函数，而不用协程
2.call_later:可以指定多长时间后启动(实际调用call_at,时间不是传统的时间，而是loop内部的时间)
3.call_at:指定某个时间执行
4.call_soon_threadsafe:
    线程安全的方法，不仅能解决协程，也能解决线程，进程，和call_soon几乎一致，
    多了self._write_to_self()解决线程安全问题，和call_soon用法一致
"""

import asyncio


def callback(sleep_time):
    print('sleep {} success'.format(sleep_time))


# 通过该函数暂停
def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    # @1.call_soon函数示例：可以直接接收函数，而不用协程
    # call_soon(self, callback, *args)
    # loop = asyncio.get_event_loop()
    # # 可以直接传递函数，而不用协程,call_soon其实就是调用的call_later，时间为0秒
    # loop.call_soon(callback, 2)  # callback放到loop中执行
    # loop.call_soon(stoploop, loop)  # 不加会一直执行
    # # 不能用run_util_complete（因为不是协程），run_forever找到call_soon一直运行
    # loop.run_forever()

    # @2.call_later函数示例：可以指定多长时间后启动(实际调用call_at,时间不是传统的时间，而是loop内部的时间)
    # def call_later(self, delay, callback, *args)，和添加顺序无关
    # loop = asyncio.get_event_loop()
    # loop.call_later(3, callback, 1)
    # loop.call_later(1, callback, 2)
    # loop.call_later(1, callback, 2)
    # loop.call_later(1, callback, 2)
    # loop.call_soon(callback, 4)  # 先直接执行，call_soon优先于call_later
    # loop.call_soon(stoploop, loop)
    # loop.run_forever()
    """
    sleep 4 success  # 先直接执行
    sleep 2 success
    sleep 2 success
    sleep 2 success
    sleep 1 success  # delay 3s 最后在执行
    """

    # @3.call_at函数示例：指定某个时间执行，时间不是传统的时间，而是loop内部的时间
    loop = asyncio.get_event_loop()
    now = loop.time()  # loop内部的时钟时间
    print(now)
    loop.call_at(now + 3, callback, 1)
    loop.call_at(now + 1, callback, 0.5)
    loop.call_at(now + 1, callback, 2)
    loop.call_at(now + 1, callback, 2)
    # loop.call_soon(stoploop, loop)  # 立即停止
    loop.run_forever()
