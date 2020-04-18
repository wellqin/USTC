# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        25.Condition
Description :   
Author :          wellqin
date:             2020/4/16
Change Activity:  2020/4/16
-------------------------------------------------

Condition（条件变量）里面有enter和exit两个魔法方法，因此可以利用with语句实现。

with语句相当于就是一次获取锁以及释放锁的过程。条件变量总是与某种锁定相关联。可以传入，也可以默认创建一个。
（当多个条件变量必须共享相同的锁时，传递一个输入很有用。）条件变量具有acquire()和release() 方法，它们调用关联锁的相应方法。

它还具有一个wait()方法以及notify()和 notifyAll()方法。
只有在调用线程获得了锁之后(with self.condition)，才必须调用这三个对象。

wait()   # 方法释放锁，然后块直到其被唤醒一个notify（）或notifyAll的（）调用在另一个线程相同的条件变量。
            唤醒后，它将重新获取锁并返回。也可以指定超时。

notify() # 方法唤醒等待条件变量的线程中的一个，如果有的话正在等待。所述notifyAll的（） 方法唤醒等待条件变量的所有线程。


注意：notify()和notifyAll()方法不会释放锁；
一个线程将获得独占资源的锁去访问共享资源,通过生产者/消费者可以更好的描述这种方式，生产者添加一个随机数字到公共列表，
而消费者将这个数字在公共列表中清除。看一下生产者类，生产者获得一个锁，添加一个数字，然后通知消费者线程有一些东西可以来清除，
最后释放锁定。在各项动作不段切换的时候，将会触发不定期的随机暂停。


"""

import threading

# 通过condition完成协同读诗,用于复杂的线程间同步，比如：交替执行
# 线程在执行时，当满足了特定的条件后，才可以访问相关的数据
"""
Condition内部有一把锁，默认是RLock，在调用wait()和notify()之前必须先调用acquire()获取这个锁，才能继续执行；
当wait()和notify()执行完后，需调用release()释放这个锁，在执行with condition时，会先执行acquire()，with结束时，执行了release()；
所以condition有两层锁，最底层锁在调用wait()时会释放，同时会加一把锁到等待队列，等待notify()唤醒释放锁

wait() ：允许等待某个条件变量的通知，notify()可唤醒
notify()： 唤醒等待队列wait()


可以认为Condition对象维护了一个锁（Lock/RLock)和一个waiting池。线程通过acquire获得Condition对象，
当调用wait方法时，线程会释放Condition内部的锁并进入blocked状态，同时在waiting池中记录这个线程。
当调用notify方法时，Condition对象会从waiting池中挑选一个线程，通知其调用acquire方法尝试取到锁。
"""

# class Condition:
#     """Class that implements a condition variable.
#
#     A condition variable allows one or more threads to wait until they are
#     notified by another thread.
#
#     If the lock argument is given and not None, it must be a Lock or RLock
#     object, and it is used as the underlying lock. Otherwise, a new RLock object
#     is created and used as the underlying lock.
#
#     """
#
#     def __init__(self, lock=None):
#         if lock is None:
#             lock = RLock()  # Condition内部有一把锁，默认是RLock
#         self._lock = lock
#         # Export the lock's acquire() and release() methods
#         self.acquire = lock.acquire
#         self.release = lock.release
#         # If the lock defines _release_save() and/or _acquire_restore(),
#         # these override the default implementations (which just call
#         # release() and acquire() on the lock).  Ditto for _is_owned().
#         try:
#             self._release_save = lock._release_save
#         except AttributeError:
#             pass
#         try:
#             self._acquire_restore = lock._acquire_restore
#         except AttributeError:
#             pass
#         try:
#             self._is_owned = lock._is_owned
#         except AttributeError:
#             pass
#         self._waiters = _deque()
#
#     def __enter__(self):
#         return self._lock.__enter__()
#
#     def __exit__(self, *args):
#         return self._lock.__exit__(*args)
#
#     def __repr__(self):
#         return "<Condition(%s, %d)>" % (self._lock, len(self._waiters))
#
#     def _release_save(self):
#         self._lock.release()  # No state to save
#
#     def _acquire_restore(self, x):
#         self._lock.acquire()  # Ignore saved state
#
#     def _is_owned(self):
#         # Return True if lock is owned by current_thread.
#         # This method is called only if _lock doesn't have _is_owned().
#         if self._lock.acquire(0):
#             self._lock.release()
#             return False
#         else:
#             return True
#
#     def wait(self, timeout=None):
#         """Wait until notified or until a timeout occurs.
#
#         If the calling thread has not acquired the lock when this method is
#         called, a RuntimeError is raised.
#
#         This method releases the underlying lock, and then blocks until it is
#         awakened by a notify() or notify_all() call for the same condition
#         variable in another thread, or until the optional timeout occurs. Once
#         awakened or timed out, it re-acquires the lock and returns.
#
#         When the timeout argument is present and not None, it should be a
#         floating point number specifying a timeout for the operation in seconds
#         (or fractions thereof).
#
#         When the underlying lock is an RLock, it is not released using its
#         release() method, since this may not actually unlock the lock when it
#         was acquired multiple times recursively. Instead, an internal interface
#         of the RLock class is used, which really unlocks it even when it has
#         been recursively acquired several times. Another internal interface is
#         then used to restore the recursion level when the lock is reacquired.
#
#         """
#         if not self._is_owned():
#             raise RuntimeError("cannot wait on un-acquired lock")
#         waiter = _allocate_lock()
#         waiter.acquire()
#         self._waiters.append(waiter)
#         saved_state = self._release_save()
#         gotit = False
#         try:  # restore state no matter what (e.g., KeyboardInterrupt)
#             if timeout is None:
#                 waiter.acquire()
#                 gotit = True
#             else:
#                 if timeout > 0:
#                     gotit = waiter.acquire(True, timeout)
#                 else:
#                     gotit = waiter.acquire(False)
#             return gotit
#         finally:
#             self._acquire_restore(saved_state)
#             if not gotit:
#                 try:
#                     self._waiters.remove(waiter)
#                 except ValueError:
#                     pass
#
#     def wait_for(self, predicate, timeout=None):
#         """Wait until a condition evaluates to True.
#
#         predicate should be a callable which result will be interpreted as a
#         boolean value.  A timeout may be provided giving the maximum time to
#         wait.
#
#         """
#         endtime = None
#         waittime = timeout
#         result = predicate()
#         while not result:
#             if waittime is not None:
#                 if endtime is None:
#                     endtime = _time() + waittime
#                 else:
#                     waittime = endtime - _time()
#                     if waittime <= 0:
#                         break
#             self.wait(waittime)
#             result = predicate()
#         return result
#
#     def notify(self, n=1):
#         """Wake up one or more threads waiting on this condition, if any.
#
#         If the calling thread has not acquired the lock when this method is
#         called, a RuntimeError is raised.
#
#         This method wakes up at most n of the threads waiting for the condition
#         variable; it is a no-op if no threads are waiting.
#
#         """
#         if not self._is_owned():
#             raise RuntimeError("cannot notify on un-acquired lock")
#         all_waiters = self._waiters
#         waiters_to_notify = _deque(_islice(all_waiters, n))
#         if not waiters_to_notify:
#             return
#         for waiter in waiters_to_notify:
#             waiter.release()
#             try:
#                 all_waiters.remove(waiter)
#             except ValueError:
#                 pass
#
#     def notify_all(self):
#         """Wake up all threads waiting on this condition.
#
#         If the calling thread has not acquired the lock when this method
#         is called, a RuntimeError is raised.
#
#         """
#         self.notify(len(self._waiters))
#
#     notifyAll = notify_all

"""
方法：
acquire(*args)   获取锁。这个方法调用底层锁的相应方法。
release()        释放锁。这个方法调用底层锁的相应方法。

wait(timeout=None)
线程挂起，等待被唤醒(其他线程的notify方法)或者发生超时。调用该方法的线程必须先获得锁，否则引发RuntimeError。
该方法会释放底层锁，然后阻塞，直到它被另一个线程中的相同条件变量的notify()或notify_all()方法唤醒，
或者发生超时。一旦被唤醒或超时，它会重新获取锁并返回。
返回值为True，如果给定timeout并发生超时，则返回False。

wait_for(predicate, timeout=None)
等待知道条件变量的返回值为True。predicate应该是一个返回值可以解释为布尔值的可调用对象。可以设置timeout以给定最大等待时间。
该方法可以重复调用wait()，直到predicate的返回值解释为True，或发生超时。该方法的返回值就是predicate的最后一个返回值，如果发生超时，返回值为False。
如果忽略超时功能，该方法大致相当于：

while not predicate():
    con.wait()

它与wait()的规则相同：调用前必须先获取锁，阻塞时释放锁，并在被唤醒时重新获取锁并返回。

notify(n=1)
默认情况下，唤醒等待此条件变量的一个线程(如果有)。调用该方法的线程必须先获得锁，否则引发RuntimeError。
该方法最多唤醒n个等待中的线程，如果没有线程在等待，它就是要给无动作的操作。
注意：要被唤醒的线程实际上不会马上从wait()方法返回(唤醒)，而是等到它重新获取锁。
这是因为notify()并不会释放锁，需要线程本身来释放(通过wait()或者release())

notify_all()
此方法类似于notify()，但唤醒的时所有等待的线程。
"""


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):  # threading.Thread方式用run覆盖
        self.cond.acquire()  # 与with self.cond:语句一样的效果
        # __enter__,:(self.cond.acquire()) __exit__:（self.cond.release()）
        # acquire获取锁。调用底层锁的相应方法。

        self.cond.wait()  # 先等待，即后执行，回答完话之后，进行通知
        # 调用该wait方法的线程必须先acquire获得锁，否则引发RuntimeError。
        # wait方法会释放底层锁，然后阻塞，直到它被另一个线程中的相同条件变量的notify()或notify_all()方法唤醒

        """
        非常好奇wait()的逻辑进入时释放锁，然后阻塞，被唤醒后获取锁，然后返回是怎么实现的，明明只绑定了一个锁，阻塞如何实现的，被唤醒怎么实现的？
        原理：原来是维护了一个_waiters双端队列，在wait()中连续wait.acquire()两次，把自己阻塞；
             在调用notify()后，选择其中一个waiter.release()唤醒一个等待的线程。
        """
        print("{} : 在 ".format(self.name))
        self.cond.notify()  # notify()和notifyAll()方法不会释放锁

        self.cond.wait()
        print("{} : 好啊 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 君住长江尾 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 共饮长江水 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 此恨何时已 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 定不负相思意 ".format(self.name))
        self.cond.notify()
        self.cond.release()  # 全部执行完后，释放锁


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{} : 小爱同学 ".format(self.name))
            self.cond.notify()  # 说完话，然后notify通知
            self.cond.wait()  # 进入等待，等另一个线程的notify通知
            # 先执行tianmao.start()，会导致出错，因为notify没有通知出去就wait，另一线程也在wait

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    condition = threading.Condition()
    xiaoai = XiaoAi(condition)
    tianmao = TianMao(condition)
    # 在调用with condition之后才能调用wait或者notify方法
    # condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放，
    # 上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，等到notify方法的唤醒

    # 启动顺序很重要
    xiaoai.start()
    tianmao.start()
    """
    天猫精灵 : 小爱同学 
    小爱 : 在 
    天猫精灵 : 我们来对古诗吧 
    小爱 : 好啊 
    天猫精灵 : 我住长江头 
    小爱 : 君住长江尾 
    天猫精灵 : 日日思君不见君 
    小爱 : 共饮长江水 
    天猫精灵 : 此水几时休 
    小爱 : 此恨何时已 
    天猫精灵 : 只愿君心似我心 
    小爱 : 定不负相思意 
    """

    """
    过程分析：
    xiaoai.start()
    (X1)with self.cond      # 调用__enter__函数，对_lock加锁
    (X2)self.cond.wait()    # 1.waiter=Lock(), waiter.require()，
                              2._lock.release() (T1)可以运行了，
                              3.waiter.require(), 线程暂停，等待notify来释放, 
                              4._lock.require(), 线程暂停，等待(T4-2)释放
    (X3)print("{} : 在 ".format(self.name))
    (X4)self.cond.notify() # waiter.release(),(T4-3)可以运行了，运行到(T4-4)重新获取_lock请求，暂停
    
    tianmao.start()
    (T1)with self.cond      # _lock.require()，线程暂停，等待_lock释放
    (T2)print("{} : 小爱同学 ".format(self.name))   # 天猫精灵 : 小爱同学
    (T3)self.cond.notify()  # waiter.release(),(X2-3)可以运行了，运行到(X2-4)重新获取_lock请求，暂停
    (T4)self.cond.wait()    # 1.waiter=Lock(), waiter.require()，
                              2._lock.release() (X2-4)可以向下运行了，
                              3.waiter.require(), 线程暂停，等待notify来释放, 
                              4._lock.require()



    以此类推完成一问一答的过程
    从上可知，wait函数有四个步骤
    1.创建waiter锁，并require()
    2.释放底层锁_lock
    3.waiter.require()重新加锁
    4.重新获取_lock加锁
    
    疑问: 为什么notify释放的就是上一个waiter锁呢？ 
    因为wait函数调用的时候，把新创建的waiter锁放入到一个双端队列deque中，notify的时候，释放的永远是头端的waiter锁。
    即实现的是先进先出（FIFO）的数据结构
                                    
    """
