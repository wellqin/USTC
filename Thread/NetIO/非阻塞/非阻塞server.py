# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        非阻塞server
Description :   
Author :          wellqin
date:             2019/8/23
Change Activity:  2019/8/23
-------------------------------------------------

由于阻塞IO无法满足大规模请求的缺点,因此出现了非阻塞模型。
当数据报未准备好,recvfrom立即返回一个EWOULDBLOCK错误,可以利用轮询不停调用recvfrom,当数据报准备好,内核则将数据复制到应用进程缓冲区。

非阻塞IO模型需要利用轮询不断调用recvfrom,浪费大量CPU时间,且当内核接收到数据时,需要等到下一次轮询才能复制到应用进程缓冲区,数据得不到立刻处理。


运行非阻塞服务端和两个客户端实例,,服务端接收两个连接请求。由于conn被设置为非阻塞socket,
即使客户端并没有向服务端发送数据,conn.recv(1024)也会立即返回,不会阻塞,从而进程可以接收新的连接请求。
"""
import socket

def start_noblocking():
    """
    同步非阻塞
    """
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock.bind(('', 8080))
    ssock.listen(5)
    count = 0
    while True:
        conn, addr = ssock.accept()
        conn.setblocking(0)  # 设置为非阻塞socket
        count += 1
        print('Connected by', addr)
        print('Accepted clinet count:%d' % count)
        try:
            data = conn.recv(1024)  # 非阻塞,没有数据会立刻返回
            if data:
                conn.sendall(data)
        except Exception as e:
            pass
        finally:
            conn.close()
start_noblocking()