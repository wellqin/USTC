# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        非阻塞client
Description :   
Author :          wellqin
date:             2019/8/23
Change Activity:  2019/8/23
-------------------------------------------------
"""

import socket

def start_blocking():
    host = 'localhost'
    port = 8080
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csock.connect((host, port))
    data = csock.recv(1024)
    print(data)

start_blocking()