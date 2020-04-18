# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        22.Run
Description :   
Author :          wellqin
date:             2020/4/16
Change Activity:  2020/4/16
-------------------------------------------------
1.2.2:通过继承Thread来实现多线程：（继承之后重写run方法，逻辑在run中进行）
更适用

"""

import time
import threading


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("last time: {}".format(time.time() - start_time))
    """
    get detail html started
    get detail url started
    get detail html end
    get detail url end
    last time: 4.001150369644165
    """
