# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        5-线程的执⾏顺序
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        t.start()
        t.join()  # join使得线程按照顺序执行


# def test():
#     MyThreads = []
#     for i in range(5):
#         t = MyThread()
#         t.start()
#         MyThreads.append(t)
#     for i in MyThreads:
#         i.join()  # join加在这个位置使得线程并发执行


if __name__ == '__main__':
    test()

"""
I'm Thread-1 @ 0
I'm Thread-3 @ 0
I'm Thread-2 @ 0
I'm Thread-4 @ 0
I'm Thread-5 @ 0
                sleep(1)
I'm Thread-1 @ 1
I'm Thread-4 @ 1
I'm Thread-3 @ 1
I'm Thread-2 @ 1
I'm Thread-5 @ 1
                sleep(1)
I'm Thread-1 @ 2
I'm Thread-2 @ 2
I'm Thread-4 @ 2
I'm Thread-3 @ 2
I'm Thread-5 @ 2
"""

"""
从代码和执⾏结果我们可以看出，多线程程序的执⾏顺序是不确定的。
当执⾏到sleep语句时，线程将被阻塞（Blocked），到sleep结束后，线程进⼊就绪（Runnable）状态，等待调度。
⽽线程调度将⾃⾏选择⼀个线程执⾏。上⾯的代码中只能保证每个线程都运⾏完整个run函数，但是线程的启动顺序、
run函数中每次循环的执⾏顺序都不能确定。
"""

"""
t.join()使得线程按照顺序执行


I'm Thread-1 @ 0
I'm Thread-1 @ 1
I'm Thread-1 @ 2
I'm Thread-2 @ 0
I'm Thread-2 @ 1
I'm Thread-2 @ 2
I'm Thread-3 @ 0
I'm Thread-3 @ 1
I'm Thread-3 @ 2
I'm Thread-4 @ 0
I'm Thread-4 @ 1
I'm Thread-4 @ 2
I'm Thread-5 @ 0
I'm Thread-5 @ 1
I'm Thread-5 @ 2
"""
