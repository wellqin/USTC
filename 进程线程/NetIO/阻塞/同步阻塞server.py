# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        网络IO
Description :   
Author :          wellqin
date:             2019/8/23
Change Activity:  2019/8/23
-------------------------------------------------

运行server端,并运行两个client实例去连接服务端,可以看到虽然有两个客户端去连接,但却只有一个连接上,
服务端的socket conn为阻塞套接字,conn.recv(1024)未收到客户端发送的数据,处于阻塞状态,服务端无法再响应另一个客户端的连接。
"""

import socket


def start_blocking():
    """同步阻塞server,服务端的socket conn为阻塞套接字"""
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind(('localhost', 8080))
    ssock.listen(5)
    count = 0
    while True:
        conn, addr = ssock.accept()  # IO操作 在这accept的时候不能干recv的活  **等待数据**
        count += 1
        print('Connected by', addr)
        print('Accepted clinet count:%d' % count)
        # ** 将数据从内核复制到用户空间 **
        data = conn.recv(1024)  # IO操作  若无数据则阻塞 不论是客户还是服务器应用程序都用recv函数从TCP连接的另一端接收数据。
        if data:
            conn.sendall(data)
        conn.close()


start_blocking()
