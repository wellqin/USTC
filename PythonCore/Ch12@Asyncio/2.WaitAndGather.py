# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.WaitAndGather
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------

wait和gather的区别:
    gather和wait的区别：（定制性不强时可以优先考虑gather）
    gather更加高层，可以将tasks分组；还可以成批的取消任务，【优先使用】

协程的wait和线程的wait相似，也有timeout，return_when（什么时候返回）等参数
"""
import asyncio
import time
from functools import partial


async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')


if __name__ == '__main__':
    start_time = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html('www.baidu.com') for i in range(10)]
    # 1.wait简单使用: 等待所有协程完成之后，才会执行下一步
    # wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
    # wait和线程的wait相似
    # loop.run_until_complete(asyncio.wait(tasks))
    # print(time.time() - start_time)

    # 2.gather简单使用，与wait作用基本一样
    # gather注意加*，这样就会解析变成参数
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time() - start_time)

    # 3.gather和wait的区别：（定制性不强时可以优先考虑gather）
    # gather更加高层，可以将tasks分组；还可以成批的取消任务
    loop = asyncio.get_event_loop()
    groups1 = [get_html('www.baidu.com') for i in range(10)]
    groups2 = [get_html('www.baidu.com') for i in range(10)]
    # gather注意加*，这样就会变成参数
    loop.run_until_complete(asyncio.gather(*groups1, *groups2))
    print(time.time() - start_time)

    # 这种方式也可以
    # groups1 = [get_html('www.baidu.com') for i in range(10)]
    # groups2 = [get_html('www.baidu.com') for i in range(10)]
    # groups1 = asyncio.gather(*groups1)
    # groups2 = asyncio.gather(*groups2)
    # loop.run_until_complete(asyncio.gather(groups1, groups2))

    # 取消任务
    # groups2.cancel()
    # loop.run_until_complete(asyncio.gather(groups1,groups2))
