# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        6.AsyncioHttp
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------

# asyncio目前没有提供http协议的接口：aiohttp
本次不用socket包来完成http请求
"""

import asyncio
from urllib.parse import urlparse
import time


# 改为协程async
async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立socket连接(比较耗时)，非阻塞需要注册，都在open_connection中实现了
    # def open_connection(host=None, port=None, *,
    #                     loop=None, limit=_DEFAULT_LIMIT, **kwds):  --> reader, writer

    reader, writer = await asyncio.open_connection(host, 80)
    # 向服务器发送数据,unregister和register都实现了
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    # 读取数据
    all_lines = []
    # 源码实现较复杂，有__anext__的魔法函数（协程）
    async for line in reader:  # 将for循环过程异步化
        data = line.decode('utf8')
        all_lines.append(data)
    html = '\n'.join(all_lines)
    return html


async def main():
    tasks = []
    for i in range(20):
        url = "http://www.baidu.com/"
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 1.获取不到结果
    # tasks = [get_url('http://www.baidu.com') for i in range(10)]

    # 2.在外部获取结果,保存为future对象
    # tasks = [asyncio.ensure_future(get_url('http://www.baidu.com')) for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print(task.result())

    # 3.执行完一个打印一个
    loop.run_until_complete(main())
    print(time.time() - start_time)
