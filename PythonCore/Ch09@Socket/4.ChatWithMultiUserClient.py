# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.ChatWithMultiUserClient
Description :   
Author :          wellqin
date:             2020/4/15
Change Activity:  2020/4/15
-------------------------------------------------
"""


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    # 先发送，再接受
    re_data = input()
    if re_data.upper() == "Q":
        break
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))
client.close()
