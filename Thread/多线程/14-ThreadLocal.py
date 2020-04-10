# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        14-ThreadLocal
Description :   
Author :          wellqin
date:             2019/9/12
Change Activity:  2019/9/12
-------------------------------------------------
"""

"""
在多线程环境下，每个线程都有⾃⼰的数据。⼀个线程使⽤⾃⼰的局部变量
⽐使⽤全局变量好，因为局部变量只有线程⾃⼰能看⻅，不会影响其他线
程，⽽全局变量的修改必须加锁。
"""

# 1. 使⽤函数传参的⽅法 但是局部变量也有问题，就是在函数调⽤的时候，传递起来很麻烦：


# def process_student(name):
#     std = Student(name)
#     # std是局部变量，但是每个函数都要⽤它，因此必须传进去：
#     do_task_1(std)
#     do_task_2(std)
#
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
#
# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)

"""
每个函数⼀层⼀层调⽤都这么传参数那还得了？⽤全局变量？也不⾏，因为
每个线程处理不同的Student对象，不能共享。
"""

# 2. 使⽤全局字典的⽅法
# 如果⽤⼀个全局dict存放所有的Student对象，然后以thread⾃身作为key获得
# 线程对应的Student对象如何？
"""
这种⽅式理论上是可⾏的，它最⼤的优点是消除了std对象在每层函数中的传
递问题，但是，每个函数获取std的代码有点low。
有没有更简单的⽅式？
"""
# global_dict = {}
# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
# def do_task_1():
#     # 不传⼊std，⽽是根据当前线程查找：
#     std = global_dict[threading.current_thread()]
#     ...
# def do_task_2():
#     # 任何函数都可以查找出当前线程的std变量：
#     std = global_dict[threading.current_thread()]
#     ...



# 3. 使⽤ThreadLocal的⽅法
"""

ThreadLocal应运⽽⽣，不⽤查找dict，ThreadLocal帮你⾃动做这件事：

全局变量local_school就是⼀个ThreadLocal对象，每个Thread对它都可以读
写student属性，但互不影响。你可以把local_school看成全局变量，但每个
属性如local_school.student都是线程的局部变量，可以任意读写⽽互不⼲
扰，也不⽤管理锁的问题，ThreadLocal内部会处理。

可以理解为全局变量local_school是⼀个dict，不但可以⽤
local_school.student，还可以绑定其他变量，如local_school.teacher等等。

ThreadLocal最常⽤的地⽅就是为每个线程绑定⼀个数据库连接，HTTP请
求，⽤户身份信息等，这样⼀个线程的所有调⽤到的处理函数都可以⾮常⽅
便地访问这些资源。


java中ThreadLocal就是一种以空间换时间的做法，在每个Thread里面维护了一个以开地址法实现的ThreadLocal.ThreadLocalMap，
把数据进行隔离，数据不共享，自然就没有线程安全方面的问题了
"""
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('dongGe',), name="dongGe")
t2 = threading.Thread(target=process_thread, args=('⽼王',), name='⽼王')
t1.start()
t2.start()
t1.join()
t2.join()

"""
⼀个ThreadLocal变量虽然是全局变量，但每个线程都只能读写⾃⼰线程的独
⽴副本，互不⼲扰。ThreadLocal解决了参数在⼀个线程中各个函数之间互相
传递的问题
"""

