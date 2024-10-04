# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.SocketClient
Description :   
Author :          wellqin
date:             2020/4/15
Change Activity:  2020/4/15
-------------------------------------------------
"""

import socket


# 1.客户端初始化一个Socket，
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.然后连接服务器(connect)，如果连接成功，这时客户端与服务器端的连接就建立了。
client.connect(('127.0.0.1', 8000))  # 连接服务端

# 3.收发消息
while True:
    re_data = input()
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))

# 4.关闭连接
# client.close()
