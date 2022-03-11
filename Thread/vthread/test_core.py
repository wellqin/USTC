# -*- coding:utf-8 -*-
import time
from Thread.vthread import vthread


# vthread.thread
# ========#
# 多线程 #
# ========#
# eg.1
@vthread.thread(5)  # 只要这一行就能让函数变成开5个线程执行同个函数
def fool_func(num):
    time.sleep(1)
    print(f"foolstring, test1 fool numb: {num}")


fool_func(123)

