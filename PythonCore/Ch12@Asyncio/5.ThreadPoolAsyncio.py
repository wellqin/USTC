# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        5.ThreadPoolAsyncio
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------
ThreadPoolExecutor+asyncio（线程池和协程结合）

1.使用run_in_executor：就是把阻塞的代码放进线程池运行，性能并不是特别高，和多线程差不多
run_in_executor(self, executor, func, *args)

def run_in_executor(self, executor, func, *args):
    if (coroutines.iscoroutine(func)
    or coroutines.iscoroutinefunction(func)):
        raise TypeError("coroutines cannot be used with run_in_executor()")
    self._check_closed()
    if isinstance(func, events.Handle):
        assert not args
        assert not isinstance(func, events.TimerHandle)
        if func._cancelled:
            f = self.create_future()
            f.set_result(None)
            return f
        func, args = func._callback, func._args
    if executor is None:
        executor = self._default_executor
        if executor is None:
            executor = concurrent.futures.ThreadPoolExecutor(_MAX_WORKERS)
            self._default_executor = executor
    return futures.wrap_future(executor.submit(func, *args), loop=self)
"""

# 使用多线程，在协程中集成阻塞io【本来在协程中是不能阻塞的】
# 把线程里面的future进行包装，形成协程里面的future
# 写的同步方法，可以用ThreadPoolExecutor来代替执行，然后让主线程的event_loop等待结果。
import asyncio
import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, wait
import time


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    # 向服务器发送数据
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    # 将数据读取完
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    # 会将header信息作为返回字符串
    data = data.decode('utf8')
    print(data.split('\r\n\r\n')[1])
    client.close()


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for i in range(20):
        # run_in_executor(self, executor, func, *args)
        # run_in_executor就是把阻塞的代码放到线程池里面运行
        task = loop.run_in_executor(executor, get_url, 'http://www.imooc.com')
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)

    # 单纯线程池方式
    # start_time = time.time()
    # executor = ThreadPoolExecutor()  # max_workers 最大同时并发数，默认是操作系统的核的数量
    # allTask = [executor.submit(get_url, 'http://www.imooc.com') for _ in range(20)]
    # # wait(allTask)  # 主线程会等待所有allTask中线程执行完毕，再执行主线程
    # wait(allTask)  # return_when有很多选项，此处表示当第一个线程完成的时候，继续运行主线程
    # print(time.time() - start_time)
