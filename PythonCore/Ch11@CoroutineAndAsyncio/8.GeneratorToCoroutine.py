# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        8.GeneratorToCoroutine
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------
python3.5之前协程都是通过生成器实现的，但是3.5之后已经支持原生的协程了

1.生成器可以暂停并获取状态
2.协程的调度依然是 事件循环+协程模式 ，协程是单线程模式
"""

# 生成器是可以暂停的函数
import inspect
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()


# gen_func实现value = yield from的生产消费模型，就可以认为是协程了
# 1. 首先用同步的方式编写异步的代码，然后在适当的时候暂停函数并在适当的时候启动函数【yield from】
def gen_func():
    yield 1

    # value = yield from
    # 第一返回值给调用方， 第二调用方通过send方式返回值给gen
    return "leven"


# 2.协程的调度依然是 事件循环+协程模式 ，协程是单线程模式
# 单线程模式中千万不能写sleep，否则影响整个代码流程，应该将耗时的操作yield出去
def get_socket_data():
    yield "leven"


class Fetcher:
    def downloader(self, url):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setblocking(False)

        try:
            client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

        # 如果get_socket_data()中出现异常，会直接抛给downloader（向上抛)
        source = yield from get_socket_data()
        data = source.decode("utf8")
        html_data = data.split("\r\n\r\n")[1]
        print(html_data)


def download_html(html):
    html = yield from Fetcher().downloader(html)  # downloader子生成器


if __name__ == "__main__":
    # 说明第一点
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))  # getgeneratorstate获取生成器状态 GEN_CREATED(创建)
    next(gen)
    print(inspect.getgeneratorstate(gen))  # GEN_SUSPENDED 暂停
    try:
        next(gen)
    except StopIteration:
        pass

    print(inspect.getgeneratorstate(gen))  # GEN_CLOSED  关闭
