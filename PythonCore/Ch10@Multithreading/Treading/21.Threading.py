# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.Threading
Description :   
Author :          wellqin
date:             2020/4/15
Change Activity:  2020/4/15
-------------------------------------------------

线程：是指进程内的一个执行单元，同时也是操作系统即CPU执行任务的最小单位。

因为Cpython的解释器上有一把全局锁即上面提到的GIL锁，一个进程中同一时间只允许一个线程执行，遇到I/O阻塞的时候，快速切换到另一个线程，
线程也可以理解就是每当遇到I/O操作的时候，就会切换，节约的时间就是I/O操作的时间。

1.2.1：通过Thread类实例化：

threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

Thread类提供了以下方法:
run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。



总结：一般情况：主线程运行完成之后就退出，其他线程还会照样执行
     设置守护线程：主线程运行完成之后退出时就终止所有守护线程，即可完成主线程结束后会终止其他线程
     join：主线程会等待其他线程执行完才执行并退出
"""

import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")


def get_detail_url(url):  # 在获取列表时，网络等待的IO期间，执行另一个线程去获取列表详情页
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")


if __name__ == "__main__":
    # target传递函数名，函数参数通过args传递
    thread1 = threading.Thread(target=get_detail_html, args=("www.baidu.com",))
    thread2 = threading.Thread(target=get_detail_url, args=("www.baidu.com",))

    # 主线程运行完，就终止程序呢？
    """
    其实守护线程和用户线程区别不大，可以理解为特殊的用户线程。特殊就特殊在如果程序中所有的用户线程都退出了，
    那么所有的守护线程就都会被杀死，很好理解，没有被守护的对象了，也不需要守护线程了。
    """
    # thread1.setDaemon(True)  # 是否守护线程，必须在start()调用之前设置此参数
    # thread2.setDaemon(True)  # 会在主线程执行完后，程序立即结束，终止所有未完成的子线程

    start_time = time.time()
    thread1.start()
    thread2.start()

    # 当所有线程运行结束后，主线程才结束：
    thread1.join()
    thread2.join()

    # 此print由main主线程直接不等待上面二个线程执行完就直接执行了
    print("last time: {}".format(time.time() - start_time))  # 0.00099945068359375
    # print后，程序依然还在执行，子线程还在执行sleep
    # 可不可以在main主线程运行完，就终止程序呢？-- 建立守护线程(setDaemon)
    """
    get detail html started
    get detail url startedlast time: 0.00099945068359375
    get detail html end
    get detail url end
    
    # 都加上setDaemon()后结果
    get detail html started
    get detail url started
    last time: 0.0004611015319824219
    
    # 只给thread2加上setDaemon()后结果，则系统不会等待thread2，只会等待非守护线程
    get detail html started
    get detail url started
    last time: 0.0009653568267822266
    get detail html end
    
    # 当所有线程运行结束后，主线程才结束：
    get detail html started
    get detail url started
    get detail html end
    get detail url end
    last time: 4.00247859954834  # 并发执行，而不是时间相加
    """

    """
    为什么上面的时间接近0秒，因为现在这个程序总共有三个线程，那三个线程呢？
    线程1、2以及主线程，按照main下面运行，就会发现线程1、2运行之后继续运行下面的print语句。
    
    有没有就是当主线程运行完成之后就终止所有线程的呢？建立守护线程(setDaemon)这样主程序结束就会kill子线程。
    setDaemon()
    参数一个布尔值，指示此线程是否是守护线程（真）（假）。必须在start()调用之前设置此参数，
    否则RuntimeError引发该参数。它的初始值是从创建线程继承的；主线程不是守护程序线程，
    因此在主线程中创建的所有线程默认为daemonic = False。 当没有活动的非守护线程时，整个Python程序将退出。 
    """