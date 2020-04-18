# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        26.Semaphore
Description :   
Author :          wellqin
date:             2020/4/18
Change Activity:  2020/4/18
-------------------------------------------------

信号量管理一个内部计数器，该计数器由每个acquire()调用递减， 并由每个release() 调用递增。
计数器永远不能低于零。当acquire() 发现它为零时，它将阻塞，等待其他线程调用release()。
即可以利用它来控制爬虫每次的请求次数，一次请求过多，会被禁止，为了反反爬就可以设置线程请求的并发数。


def __init__(self, value=1):
    if value < 0:
        raise ValueError("semaphore initial value must be >= 0")
    self._cond = Condition(Lock())  # 源码内部由Condition实现
    self._value = value
"""

# Semaphore 是用于控制进入数量的锁
# 文件读、写， 写一般只是用于一个线程写，读可以允许有多个

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(1)
        print("got html text success")
        self.sem.release()  # 释放一个信号量，使内部计数器增加一。当它在进入时为零
        # 并且另一个线程正在等待它再次变得大于零时，唤醒该线程。


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()  # 不带参数调用时：如果内部计数器在输入时大于零，则将其递减1并立即返回。
            # 如果在进入时为零，则阻塞，等待其他线程调用 release使之大于零。（要互锁需要的代码块）
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)  # 设置每次运行数是3
    url_producer = UrlProducer(sem)
    url_producer.start()
