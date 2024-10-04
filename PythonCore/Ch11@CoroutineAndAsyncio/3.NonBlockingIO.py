# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.NonBlockingIO
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------

通过非阻塞I/O实现http请求：需要while轮询，并没有提高并发
"""

import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 1.设置成非阻塞，其他不变
    # 设置成非阻塞，本来默认阻塞，等到client.connect连接完成后send
    client.setblocking(False)  # 非阻塞时，client.connect还没有连接完成就client.send会出错
    client.connect((host, 80))  # connect本来是连接阻塞的
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    # 设置成非阻塞(抛异常：BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。)


    """
    # 2.设置成非阻塞,同时捕捉client.connect异常
    client.setblocking(False)
    try:
        client.connect((host, 80))  # connect本来是连接阻塞的
    except BlockingIOError as e:
        pass
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    # 向服务器发送数据(还未连接会抛异常)
    # OSError: [WinError 10057] 由于套接字没有连接并且(当使用一个 sendto 调用发送数据报套接字时)没有提供地址，
    # 发送或接收数据的请求没有被接受。
    """

    # # 3.设置成非阻塞, 同时捕捉client.connect异常，同时轮询捕捉client.send异常
    # # 结果一切正常
    # client.setblocking(False)
    # try:
    #     client.connect((host, 80))  # connect本来是连接阻塞的
    # except BlockingIOError as e:
    #     pass
    #
    # while True:
    #     try:
    #         client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    #         break
    #     except OSError as e:
    #         pass
    #
    # # 将数据读取完
    # data = b""
    # while True:  # send出去数据，现在不断等待返回recv数据
    #     try:  # 这里需要捕捉BlockingIOError异常
    #         d = client.recv(1024)
    #     except BlockingIOError as e:
    #         continue
    #     if d:
    #         data += d
    #     else:
    #         break
    # # 会将header信息作为返回字符串
    # data = data.decode('utf8')
    # print(data.split('\r\n\r\n')[1])
    # client.close()


if __name__ == '__main__':
    get_url('http://www.baidu.com')
