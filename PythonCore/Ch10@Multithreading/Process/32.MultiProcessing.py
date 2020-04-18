# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        32.MultiProcessing
Description :   
Author :          wellqin
date:             2020/4/18
Change Activity:  2020/4/18
-------------------------------------------------

1.9、multiprocessing多进程编程：三种方式
"""

import multiprocessing
import time


def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == "__main__":
    # 1. 普通方式
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)  # None
    # progress.start()
    # print(progress.pid)  # 10940
    # progress.join()
    # print("main progress end")

    # 2. 使用进程池：初级
    # pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(1,))  # 异步，不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。
    #
    # # 等待所有任务完成
    # pool.close()  # 告诉主进程，你等着所有子进程运行完毕后在运行剩余部分。
    # pool.join()  # close必须在join前调用
    #
    # print(result.get())  # 1

    # 3. 使用线程池：高级 imap/imap_unordered：
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for result in pool.imap(get_html, [1, 5, 3]):  # 按照映射的顺序输出
        print("{} sleep success".format(result))
        """ 有序，等待上一个完成输出下一个
        sub_progress success
        1 sleep success
        sub_progress success
        sub_progress success
        5 sleep success
        3 sleep success
        """

    for result in pool.imap_unordered(get_html, [1, 5, 3]):  # 谁先运行完成就运行谁
        print("{} sleep success".format(result))
        """ 无序
        sub_progress success
        1 sleep success
        sub_progress success
        3 sleep success
        sub_progress success
        5 sleep success
        """
