# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.Select
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------

使用select完成http请求（循环回调）：单线程模式

优点：并发性高，和之前相比效率提升几十倍
    1.驱动整个程序主要是回调循环loop()，不会等待，请求操作系统有什么准备好了，准备好了就执行
    2.没有线程切换等，只有一个线程，当一个url连接建立完成后就会注册，然后回调执行，省去了线程切换和内存
      本来方式中如果10个url，就需要10个线程。现在select会监听所有准备好的，则一个线程就可以完成.
"""

# 自动根据OS环境选择poll和epoll
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import socket
from urllib.parse import urlparse
import select  # selectors包装了select，使得其更加好用
# select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)


selector = DefaultSelector()


class Fetcher:
    """
    因为需要回调，所以写成类的形式，比如全局利用self.client，不然单个函数不好获取到这种变量
    """
    def connected(self, key):
        # 取消注册，即不监控了，【key.fd？】
        selector.unregister(key.fd)
        # 回调函数就可以send了，因为select回调时，就代表之前的connect已经完成了，不然就需要捕捉异常
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # 数据发送出去后，就需要接受数据，此时需要继续注册，此时事件是可读状态
        # EVENT_WRITE时报错：BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。
        # self.readable代表socket可读的时候，需要的操作
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        # 此处没有用之前的while循环，因为数据分批recv时，不代表下一次内核空间已经准备好数据了，此时会阻塞报错
        # 之前会阻塞到数据完成，可以直接用了
        # 此时select中，只要是可读就会继续调用readable注册函数，所以self.data全局变量，防止下一次调用时重置为空
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            # 如果此时d为空怎么办，代表数据读完了，需要取消注册
            selector.unregister(key.fd)
            # 会将header信息作为返回字符串
            data = self.data.decode('utf8')
            print(data.split('\r\n\r\n')[1])
            self.client.close()

            # 此处代码是windows环境下的补充，不加会出错，若在Linux下，selector会选择epoll模式，则不会报错，Windows下选择Select模式
            urls.remove(self.spider_url)
            if not urls:
                global stop  # 不加global则为局部
                stop = True

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册写事件,及回调函数
        # selector = DefaultSelector()
        # register(self, fileobj, events, data=None)，fileobj就是Socket，events代表事件，data为回调函数
        # events事件有EVENT_READ、EVENT_WRITE
        # data为回调函数，就是满足events事件后，需要执行的逻辑
        # client.fileno()就是socket的文件描述符
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
        # self.connected函数不能写在get_url中，否则此处本来就阻塞了等待回调，没有意义


# 并发性高,驱动整个程序主要是回调循环loop()，不会等待，请求操作系统有什么准备好了，准备好了就执行回调
def loop():
    # 回调+事件循环+select（poll/epoll）
    # 事件循环，不停的调用socket的状态并调用对应的回调函数，即上面的注册函数回调就由loop来做
    # 判断哪个可读可写，select本身不支持register模式
    # socket状态变化后的回调是程序员自己完成的
    if not stop:
        while True:
            # selector.select()可以找到register的事件，所以不填写参数
            # select.select()不可以找到，需要填写参数
            # ready作为返回值，源码中可知为('SelectorKey', ['fileobj', 'fd', 'events', 'data'])形式
            ready = selector.select()
            for key, mask in ready:
                call_back = key.data
                call_back(key)


urls = ['http://www.baidu.com', ]
stop = False  # 二个全局变量
if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url('http://www.baidu.com')
    loop()
