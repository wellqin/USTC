# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        Process⼦类
Description :   
Author :          wellqin
date:             2019/8/25
Change Activity:  2019/8/25
-------------------------------------------------
"""
from multiprocessing import Process
import time
import os


# 继承Process类
class Process_Class(Process):
    # 因为Process类本身也有__init__⽅法，这个⼦类相当于重写了这个⽅法，
    # 但这样就会带来⼀个问题，我们并没有完全的初始化⼀个Process类，所以就不能使⽤从这个类继承的⼀些⽅法和属性，
    # 最好的⽅法就是将继承类本身传递给Process.__init__⽅法，完成这些初始化操作
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    # 重写了Process类的run()⽅法
    def run(self):
        print("⼦进程(%s) 开始执⾏，⽗进程为（%s）"%(os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("(%s)执⾏结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))

if __name__=="__main__":
    t_start = time.time()
    print("当前程序进程(%s)"%os.getpid())
    p1 = Process_Class(2)
    # 对⼀个不包含target属性的Process类执⾏start()⽅法，就会运⾏这个类中的run()⽅法，所以这⾥会执⾏p1.run()
    p1.start()
    p1.join()
    t_stop = time.time()
    print("(%s)执⾏结束，耗时%0.2f"%(os.getpid(),t_stop-t_start))

"""
当前程序进程(5896)
⼦进程(3080) 开始执⾏，⽗进程为（5896）
(3080)执⾏结束，耗时2.00秒

(5896)执⾏结束，耗时2.57
"""