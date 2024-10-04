# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.ChatWithMultiUser
Description :   
Author :          wellqin
date:             2020/4/15
Change Activity:  2020/4/15
-------------------------------------------------
"""

import socket
import threading

backlog = 10
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(backlog)


def handle_sock(skObj, address):
    while True:
        # 先接受消息，再发送
        data = skObj.recv(1024)
        if data.decode("utf8") == "Q" or data.decode("utf8") == "q":
            break
        print(data.decode("utf8"))
        re_data = input()
        skObj.send(re_data.encode("utf8"))
    skObj.close()
    server.close()


def SocketServer():
    while True:
        sock, addr = server.accept()
        # 用线程去处理新接收的连接(用户)
        client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
        client_thread.start()


SocketServer()
