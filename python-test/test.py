# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/17
Change Activity:  2019/7/17
-------------------------------------------------
"""

hehe=6
def f():
    global hehe
    print(hehe)
    hehe=3
f()
print(hehe)