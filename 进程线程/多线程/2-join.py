# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2-join
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

# 2. 主线程会等待所有的⼦线程结束后才结束


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
    # t1.join()
    # t2.join() # 这二句相当于sleep(5)，达到同样的效果
    # sleep(5)  # 屏蔽此⾏代码，试试看，程序是否会⽴⻢结束？
    print('---结束---:%s' % ctime())

"""
屏蔽此⾏代码
---开始---:Wed Sep 11 00:49:42 2019
正在唱歌...0
正在跳舞...0
---结束---:Wed Sep 11 00:49:42 2019
正在唱歌...1
正在跳舞...1
正在唱歌...2
正在跳舞...2

不屏蔽此⾏代码
---开始---:Wed Sep 11 00:51:27 2019
正在唱歌...0
正在跳舞...0
正在跳舞...1
正在唱歌...1
正在跳舞...2
正在唱歌...2
---结束---:Wed Sep 11 00:51:32 2019
"""

# 所以主线程不会等待所有的⼦线程结束后才结束，需要阻塞主线程，或者让主线程睡眠等待
