# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/9/10
Change Activity:  2019/9/10
-------------------------------------------------
"""
import time
import os


# def long_time_task():
#     print('当前进程: {}'.format(os.getpid()))
#     time.sleep(2)
#     print("结果: {}".format(8 ** 20))
#
#
# if __name__ == "__main__":
#     print('当前母进程: {}'.format(os.getpid()))
#     start = time.time()
#     for i in range(2):
#         long_time_task()
#
#     end = time.time()
#     print("用时{}秒".format((end-start)))
#

from multiprocessing import Process

# 启动⼦进程并等待其结束


def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    print('父进程: {} - 任务{}'.format(os.getppid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


"""
创建⼦进程时，只需要传⼊⼀个执⾏函数target 和函数的参数args，创建⼀个Process实例，
⽤start()⽅法启动，这样创建进程⽐fork()还要简单。
"""
if __name__ == '__main__':
    print('当前母进程: {}'.format(os.getpid()))
    start = time.time()
    p1 = Process(target=long_time_task, args=(1,))
    p2 = Process(target=long_time_task, args=(2,))
    print('等待所有子进程完成。')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))

# ⼦进程要执⾏的代码
# def run_proc(name):
#     print('⼦进程运⾏中，name= %s ,pid=%d...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('⽗进程 %d.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('⼦进程将要执⾏')
#     p.start()
#     p.join()
#     print('⼦进程已结束')

def run_proc(name):
    time.sleep(1)
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    processes = list()
    for i in range(5):
        p = Process(target=run_proc, args=('test',))
        print('Process will start.')
        p.start()
        processes.append(p)

    for p in processes:
        p.join()       # 不加join的话，主进程不会等待子进程结束，二者谁先执行完，谁先退出。
    print('Process end.')

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     这样放在一起写，才是多进程
"""
Parent process 1100.
Process will start.
Process will start.
Process will start.
Process will start.
Process will start.
Run child process test (12896)...
Run child process test (10388)...
Run child process test (20548)...
Run child process test (22228)...
Run child process test (5300)...
Process end.
"""


def run_proc(name):
    time.sleep(1)
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    processes = list()
    for i in range(5):
        p = Process(target=run_proc, args=('test',))
        print('Process will start.')
        p.start()
        p.join()  # 不加join的话，主进程不会等待子进程结束，二者谁先执行完，谁先退出。
    print('Process end.')
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     这样分开写，不是多进程，而是阻塞一个个进程执行完，才执行下一个。
"""
Parent process 24028.
Process will start.
Run child process test (25768)...
Process will start.
Run child process test (9664)...
Process will start.
Run child process test (23164)...
Process will start.
Run child process test (21372)...
Process will start.
Run child process test (26052)...
Process end.
"""

























