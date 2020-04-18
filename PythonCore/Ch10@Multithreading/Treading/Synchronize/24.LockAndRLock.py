# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        24.LockAndRLock
Description :   
Author :          wellqin
date:             2020/4/16
Change Activity:  2020/4/16
-------------------------------------------------

什么叫线程同步？线程同步就是一个线程运行完成之后在进入下一个线程。
上面第一个例子为啥num值不等于零？按理来说，先加100万次，再减去100万次，最后的结果是0。
不等于0的原因是，将代码编译成字节码，前面load值以及运算值都没有出现问题，因为GIL锁会在I/O操作释放切换到其他线程，
或者在特定的运行字节码行数的时候进行切换，然而上一个函数字节码的num值，很有可能两个线程会被共用值，
赋值给desc函数的num值，因此会出此这样的情况，每次值都会不一样。

那怎么解决这种情况呢？为了保证数据的正确性，需要对多个线程进行同步。
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，
这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，
可以将其操作放到 acquire 和 release 方法之间。

但是用锁也会有缺点：1、用锁会影响性能。2、用锁会造成死锁（死锁循环-互相等待 以及 两次acquire锁，没有释放锁）

Lock可以用with实现

class lock(builtins.object)
 |  A lock object is a synchronization primitive原语.  To create a lock,
 |  call threading.Lock().  Methods are:
 |
 |  acquire() -- lock the lock, possibly blocking until it can be obtained
 |  release() -- unlock of the lock
 |  locked() -- test whether the lock is currently locked
 |
 |  A lock is not owned by the thread that locked it; another thread may
 |  unlock it.  A thread attempting to lock a lock that it has already locked
 |  will block until another thread unlocks it.  Deadlocks may ensue.
 |  锁不归于锁定它的线程所拥有；另一个线程可能解锁。试图锁定已锁定的线程的线程
 |  将阻塞，直到另一个线程将其解锁。可能会发生死锁
 |
 |  Methods defined here:
 |
 |  __enter__(...)
 |      acquire(blocking=True, timeout=-1) -> bool
 |      (acquire_lock() is an obsolete synonym)
 |
 |      Lock the lock.  Without argument, this blocks if the lock is already
 |      locked (even by the same thread), waiting for another thread to release
 |      the lock, and return True once the lock is acquired.
 |      With an argument, this will only block if the argument is true,
 |      and the return value reflects whether the lock is acquired.
 |      The blocking operation is interruptible.
 |
 |  __exit__(...)
 |      release()
 |      (release_lock() is an obsolete synonym)
 |
 |      Release the lock, allowing another thread that is blocked waiting for
 |      the lock to acquire the lock.  The lock must be in the locked state,
 |      but it needn't be locked by the same thread that unlocks it.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  acquire(...)
 |      acquire(blocking=True, timeout=-1) -> bool
 |      (acquire_lock() is an obsolete synonym)
 |
 |      Lock the lock.  Without argument, this blocks if the lock is already
 |      locked (even by the same thread), waiting for another thread to release
 |      the lock, and return True once the lock is acquired.
 |      With an argument, this will only block if the argument is true,
 |      and the return value reflects whether the lock is acquired.
 |      The blocking operation is interruptible.
 |
 |  acquire_lock(...)
 |      acquire(blocking=True, timeout=-1) -> bool
 |      (acquire_lock() is an obsolete synonym)
 |
 |      Lock the lock.  Without argument, this blocks if the lock is already
 |      locked (even by the same thread), waiting for another thread to release
 |      the lock, and return True once the lock is acquired.
 |      With an argument, this will only block if the argument is true,
 |      and the return value reflects whether the lock is acquired.
 |      The blocking operation is interruptible.
 |
 |  locked(...)
 |      locked() -> bool
 |      (locked_lock() is an obsolete synonym) 是一个过时的同义词
 |
 |      Return whether the lock is in the locked state.
 |
 |  locked_lock(...)
 |      locked() -> bool
 |      (locked_lock() is an obsolete synonym)
 |
 |      Return whether the lock is in the locked state.
 |
 |  release(...)
 |      release()
 |      (release_lock() is an obsolete synonym 是一个过时的同义词)
 |
 |      Release the lock, allowing another thread that is blocked waiting for
 |      the lock to acquire the lock.  The lock must be in the locked state,
 |      but it needn't be locked by the same thread that unlocks it.
 |
 |  release_lock(...)
 |      release()
 |      (release_lock() is an obsolete synonym 是一个过时的同义词)
 |
 |      Release the lock, allowing another thread that is blocked waiting for
 |      the lock to acquire the lock.  The lock must be in the locked state,
 |      but it needn't be locked by the same thread that unlocks it.

"""

from threading import Lock, RLock  # help(type(threading.Lock()))
import threading

# total = 0
# lock = Lock()  # 不能acquire二次
#
#
# def add():
#     global lock
#     global total
#     for i in range(10):
#         lock.acquire()  # 多线程中只让一个代码段执行，执行完后在释放
#         print(lock.locked())  # True  test whether the lock is currently locked
#         total += 1
#         lock.release()
#         print(lock.locked())  # False
#
#
# """
# #  add字节码分析
# 1. load a  a = 0
# 2. load 1  1
# 3. +    1
# 4. 赋值给a  a = 1
# """
#
#
# def desc():
#     global total
#     global lock
#     for i in range(10):
#         lock.acquire()
#         total -= 1
#         lock.release()
#
#
# """
# #  desc字节码分析
# 1. load a  a = 0
# 2. load 1  1
# 3. -    -1
# 4. 赋值给a  a = -1
# """
# # 所以，add desc执行时，在第四步切换时，a = 1或-1，但是不为0
#
#
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(total)  # 0

total = 0
lock = RLock()  # 在同一个线程里面，Rlock可以连续的调用acquire多次。一定要注意acquire的次数要和release的次数相等


def add():
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)

# 1. 用锁会影响性能
# 2. 锁会引起死锁
# 死锁的情况 1、A（a，b）  2、就是两次acquire ，第一次acquire没有将锁释放，第二次就不能获取到锁
"""
A(a、b)         当A先获取a，然后B获取到b，A就不能获取到b，B不能获取到A
acquire (a)     就这样进入到死循环即死锁的一种。
acquire (b)

B(a、b)
acquire (b)
acquire (a)
"""
