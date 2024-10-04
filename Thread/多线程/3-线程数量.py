# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3-线程数量
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

import threading
from time import sleep, ctime


def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        sleep(1)


if __name__ == '__main__':
    print('---开始---:%s' % ctime())
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前运⾏的线程数为：%d' % length)
        if length <= 1:
            break
        sleep(0.5)

    print('---结束---:%s' % ctime())

# threading.enumerate()


"""
---开始---:Wed Sep 11 00:57:37 2019
正在唱歌...0
正在跳舞...0
当前运⾏的线程数为：3
当前运⾏的线程数为：3
正在唱歌...1
当前运⾏的线程数为：3
正在跳舞...1
当前运⾏的线程数为：3
正在唱歌...2
正在跳舞...2
当前运⾏的线程数为：3
当前运⾏的线程数为：3
当前运⾏的线程数为：1
---结束---:Wed Sep 11 00:57:40 2019
"""
