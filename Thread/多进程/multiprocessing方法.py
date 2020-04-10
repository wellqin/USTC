# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        多进程
Description :   
Author :          wellqin
date:             2019/8/25
Change Activity:  2019/8/25
-------------------------------------------------
"""

# 1. 使用 multiprocessing
"""
multiprocessing模块提供了⼀个Process类来代表⼀个进程对象，下⾯的例⼦
演示了启动⼀个⼦进程并等待其结束：

创建⼦进程时，只需要传⼊⼀个执⾏函数和函数的参数，创建⼀个
Process实例，⽤start()⽅法启动，这样创建进程⽐fork()还要简单。
join()⽅法可以等待⼦进程结束后再继续往下运⾏，通常⽤于进程间的同步。

所以join是用来阻塞主进程的，让其等待子进程执行完毕，再向下执行。
"""

from multiprocessing import Process
import os
import time


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


# def run_proc(name):
#     time.sleep(3)
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     processes = list()
#     for i in range(5):
#         p = Process(target=run_proc, args=('test',))
#         print('Process will start.')
#         p.start()
#         processes.append(p)
#
#     for p in processes:
#         p.join()       # 不加join的话，主进程不会等待子进程结束，二者谁先执行完，谁先退出。
#     print('Process end.')


"""
Process语法结构如下：

Process([group [, target [, name [, args [, kwargs]]]]])
    target：表示这个进程实例所调⽤对象；
    args：表示调⽤对象的位置参数元组；
    kwargs：表示调⽤对象的关键字参数字典；
    name：为当前进程实例的别名；
    group：⼤多数情况下⽤不到；
    
Process类常⽤⽅法：
    is_alive()：判断进程实例是否还在执⾏；
    join([timeout])：是否等待进程实例执⾏结束，或等待多少秒；
    start()：启动进程实例（创建⼦进程）；
    run()：如果没有给定target参数，对这个对象调⽤start()⽅法时，就将执⾏对象中的run()⽅法；
    terminate()：不管任务是否完成，⽴即终⽌；
    
Process类常⽤属性：
    name：当前进程实例别名，默认为Process-N，N为从1开始递增的整数；
    pid：当前进程实例的PID值；
"""

# 实例1
# from multiprocessing import Process
# import os
# from time import sleep
#
#
# # ⼦进程要执⾏的代码
# def run_proc(name, age, **kwargs):
#     for i in range(10):
#         print('⼦进程运⾏中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
#         print(kwargs)
#         sleep(0.5)
#
# if __name__=='__main__':
#     print('⽗进程 %d.' % os.getpid())
#     p = Process(target=run_proc, args=('test',18), kwargs={"m":20})
#     print('⼦进程将要执⾏')
#     p.start()
#     sleep(1)
#     p.terminate()
#     p.join()
#     print('⼦进程已结束')


#两个⼦进程将会调⽤的两个⽅法
from multiprocessing import Process
import time
import os
def worker_1(interval):
    print("worker_1,⽗进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
    t_start = time.time()
    time.sleep(interval) #程序将会被挂起interval秒
    t_end = time.time()
    print("worker_1,执⾏时间为'%0.2f'秒"%(t_end - t_start))

def worker_2(interval):
    print("worker_2,⽗进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_2,执⾏时间为'%0.2f'秒"%(t_end - t_start))
    #输出当前程序的ID
    print("进程ID：%s"%os.getpid())

# 创建两个进程对象，target指向这个进程对象要执⾏的对象名称，
# args后⾯的元组中，是要传递给worker_1⽅法的参数，
# 因为worker_1⽅法就⼀个interval参数，这⾥传递⼀个整数2给它，
# 如果不指定name参数，默认的进程对象名称为Process-N，N为⼀个递增的整数
p1=Process(target=worker_1,args=(2,))
p2=Process(target=worker_2,name="dongGe",args=(1,))
# 使⽤"进程对象名称.start()"来创建并执⾏⼀个⼦进程，
# 这两个进程对象在start后，就会分别去执⾏worker_1和worker_2⽅法中的内容
p1.start()
p2.start()
# 同时⽗进程仍然往下执⾏，如果p2进程还在执⾏，将会返回True

print("p2.is_alive=%s"%p2.is_alive())
# 输出p1和p2进程的别名和pid
print("p1.name=%s"%p1.name)
print("p1.pid=%s"%p1.pid)
print("p2.name=%s"%p2.name)
print("p2.pid=%s"%p2.pid)
# join括号中不携带参数，表示⽗进程在这个位置要等待p1进程执⾏完成后，
# 再继续执⾏下⾯的语句，⼀般⽤于进程间的数据同步，如果不写这⼀句，
# 下⾯的is_alive判断将会是True，在shell（cmd）⾥⾯调⽤这个程序时
# 可以完整的看到这个过程，⼤家可以尝试着将下⾯的这条语句改成p1.join(1)，
# 因为p2需要2秒以上才可能执⾏完成，⽗进程等待1秒很可能不能让p1完全执⾏完成，
# 所以下⾯的print会输出True，即p1仍然在执⾏
p1.join()
print("p1.is_alive=%s"%p1.is_alive())

"""
进程ID：19866
p2.is_alive=True
p1.name=Process-1
p1.pid=19867
p2.name=dongGe
p2.pid=19868
worker_1,⽗进程(19866),当前进程(19867)
worker_2,⽗进程(19866),当前进程(19868)
worker_2,执⾏时间为'1.00'秒
worker_1,执⾏时间为'2.00'秒
p1.is_alive=False
"""