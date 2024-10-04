# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.SocketServer
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

1.2、socket和server实现通信

socket内置函数：

s.bind(address) 将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。

sk.listen(backlog) 开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
      backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
      这个值不能无限大，因为要在内核中维护连接队列

sk.setblocking(bool)  是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。

sk.accept() 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
            接收TCP 客户的连接（阻塞式）等待连接的到来

sk.connect(address) 连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。

sk.connect_ex(address) 同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061

sk.close() 关闭套接字

sk.recv(bufsize[,flag]) 接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。
                        flag提供有关消息的其他信息，通常可以忽略。

sk.recvfrom(bufsize[.flag]) 与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。

sk.send(string[,flag]) 将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
                        即：可能未将指定内容全部发送。

sk.sendall(string[,flag]) 将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
                          内部通过递归调用send，将所有内容发送出去。

sk.sendto(string[,flag],address) 将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。
                                 返回值是发送的字节数。该函数主要用于UDP协议。

sk.settimeout(timeout)  设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
                        一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）

sk.getpeername() 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。

sk.getsockname() 返回套接字自己的地址。通常是一个元组(ipaddr,port)

sk.fileno() 套接字的文件描述符
"""
import socket

"""
先从服务器端说起。服务器端先初始化Socket，然后与端口绑定(bind)，对端口进行监听(listen)，调用accept阻塞，等待客户端连接。
在这时如果有个客户端初始化一个Socket，然后连接服务器(connect)，如果连接成功，这时客户端与服务器端的连接就建立了。
客户端发送数据请求，服务器端接收请求并处理请求，然后把回应数据发送给客户端，客户端读取数据，最后关闭连接close，一次交互结束。
"""

# 1.创建服务端socket套接字，有两种类型的套接字：基于文件的AF_UNIX 和 面向网络的AF_INET
# 面向连接TCP的SOCK_STREAM套接字 与 无连接UDP的SOCK_DGRAM套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 协议

# 2.端口绑定(bind)
server.bind(('0.0.0.0', 8000))  # 地址，端口

# 3.监听(listen)客户端请求
server.listen(10)  # 10 为backlog，指定在拒绝连接之前，可以挂起的最大连接数量

# 4.调用accept阻塞，等待客户端连接
# 弊端：这里只能接受一个客户端的请求
sock, addr = server.accept()  # accept() -> (socket object, address info)
print(sock, addr)
# <socket.socket fd=388, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,
# laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 10982)>
# ('127.0.0.1', 10982)

# 5.获取从客户端发送的数据
# 一次获取1k的数据
# def recv(self, bufsize: int, flags: int = ...) -> bytes: ...
while True:
    data = sock.recv(1024)
    print(data.decode("utf8"))  # bytes类型转换成str类型

    # 6.发送数据给客户端
    re_data = input()  # 输入发送给客户端的消息
    sock.send(re_data.encode("utf8"))

    # 7.关闭二个连接,长期通话，暂时可不关闭
    # sock.close()  # 关闭连接
    # server.close()  # 关闭服务器
