# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4-继承
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""

"""
线程执⾏代码的封装

通过上⼀⼩节，能够看出，通过使⽤threading模块能完成多任务的程序开发，为了让每个线程的封装性更完美，所以使⽤threading模块时，
往往会定义⼀个新的⼦类class，只要继承 threading.Thread  就可以了，然后重写run⽅法

python的threading.Thread类有⼀个run⽅法，⽤于定义线程的功能函数，可以在⾃⼰的线程类中覆盖该⽅法。⽽创建⾃⼰的线程实例后，通
过Thread类的start⽅法，可以启动该线程，交给python虚拟机进⾏调度，当该线程获得执⾏的机会时，就会调⽤run⽅法执⾏线程。
"""

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)  # name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()

"""
I'm Thread-1 @ 0
I'm Thread-1 @ 1
I'm Thread-1 @ 2
"""
