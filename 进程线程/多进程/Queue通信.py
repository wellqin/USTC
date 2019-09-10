# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        Queue通信
Description :   
Author :          wellqin
date:             2019/8/25
Change Activity:  2019/8/25
-------------------------------------------------
"""

from multiprocessing import Process, Queue
import os, time, random

# Process之间有时需要通信，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 不只是multiprocessing的pipe，包括其他的pipe实现，都只是两个进程之间的游玩，我给你，你来接收 或者是你来，我接收。 当然也可以做成双工的状态。
# queue的话，可以有更多的进程参与进来。用法和一些别的queue差不多。

"""
可以使⽤multiprocessing模块的Queue实现多进程之间的数据传递，Queue
本身是⼀个消息列队程序，⾸先⽤⼀个⼩实例来演示⼀下Queue的⼯作原理：

初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最⼤可接收的消息数量，或数量为负值，
那么就代表可接受的消息数量没有上限（直到内存的尽头）；

    Queue.qsize()：返回当前队列包含的消息数量；
    Queue.empty()：如果队列为空，返回True，反之False ；
    Queue.full()：如果队列满了，返回True,反之False；
    Queue.get([block[, timeout]])：获取队列中的⼀条消息，然后将其从列队中移除，block默认值为True；
    
    
Queue.get([block[, timeout]])：获取队列中的⼀条消息，然后将其从列队中移除，block默认值为True；

1）如果block使⽤默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），
直到从消息列队读到消息为⽌，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
2）如果block值为False，消息列队如果为空，则会⽴刻抛出"Queue.Empty"异常；
Queue.get_nowait()：相当Queue.get(False)；


Queue.put(item,[block[, timeout]])：将item消息写⼊队列，block默认值为True；

1）如果block使⽤默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写⼊，此时程序将被阻塞（停在写⼊状态），
直到从消息列队腾出空间为⽌，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；

2）如果block值为False，消息列队如果没有空间可写⼊，则会⽴刻抛出"Queue.Full"异常；
Queue.put_nowait(item)：相当Queue.put(item, False)；
"""


q = Queue(3)  # 初始化⼀个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True

# 因为消息列队已满下⾯的try都会抛出异常，第⼀个try会等待2秒后再抛出异常，第⼆个Try会⽴刻抛出异常
try:
    q.put("消息4", True, 2)
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())
try:
    q.put_nowait("消息4")
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())

# 推荐的⽅式，先判断消息列队是否已满，再写⼊
if not q.full():
    q.put_nowait("消息4")
# 读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())


# 写数据进程执⾏的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执⾏的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break


if __name__=='__main__':
    # ⽗进程创建Queue，并传给各个⼦进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动⼦进程pw，写⼊:
    pw.start()
    # 等待pw结束:
    pw.join()
    # 启动⼦进程pr，读取:
    pr.start()
    pr.join()
    # pr进程⾥是死循环，⽆法等待其结束，只能强⾏终⽌:
    print('')
    print('所有数据都写⼊并且读完')


"""
如果要使⽤Pool创建进程，就需要使⽤multiprocessing.Manager()中的Queue()，⽽不是multiprocessing.Queue()，
否则会得到⼀条如下的错误信息：RuntimeError: Queue objects should only be shared between processes
through inheritance.
"""

# 修改import中的Queue为Manager
from multiprocessing import Manager,Pool

def reader(q):
    print("reader启动(%s),⽗进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))
def writer(q):
    print("writer启动(%s),⽗进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "dongGe":
        q.put(i)


if __name__=="__main__":
    print("(%s) start"%os.getpid())
    q=Manager().Queue()  # 使⽤Manager中的Queue来初始化
    po=Pool()
    #  使⽤阻塞模式创建进程，这样就不需要在reader中使⽤死循环了，可以让writer完全执⾏完成后，再⽤reader去读取
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())

"""
(26976) start
writer启动(26564),⽗进程为(26976)
reader启动(4548),⽗进程为(26976)
reader从Queue获取到消息：d
reader从Queue获取到消息：o
reader从Queue获取到消息：n
reader从Queue获取到消息：g
reader从Queue获取到消息：G
reader从Queue获取到消息：e
(26976) End
"""