"""
-------------------------------------------------
File Name:        1.Condition
Author :          wellqin
date:             2020/4/24
-------------------------------------------------
有了互斥锁，为什么还需要条件变量呢，当然是由于有些复杂问题互斥锁搞不定了。
Python提供的Condition对象提供了对复杂线程同步问题的支持。Condition被称为条件变量，
除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。


Condition

Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，
可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，
直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

Condition():

    acquire(): 线程锁
    release(): 释放锁
    wait(timeout): 线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。
                   wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。
    notify(n=1): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,
                 最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。
    notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程

"""

"""
condition有两层锁: Condition必须同时等待/通知的情况下，可以保护内部数据
1.一把底层锁会在线程调用了wait方法的时候释放（是先创建一把锁(这就是第二把锁)，然后再release），底层还是Lock或者RLock，
2.第二把锁会在每次调用wait的时候创建一把新的，并放入到cond的等待队列中（采用的是dqueue），一直acquire，等到notify方法的唤醒。
    notify方法会出队一把锁，这把锁就是刚刚创建的锁，然后release。
    
Condition 对象就是条件变量，它总是与某种锁相关联，可以是外部传入的锁或是系统默认创建的锁。
当几个条件变量共享一个锁时，你就应该自己传入一个锁。这个锁不需要你操心，Condition 类会管理它。

acquire() 和 release() 可以操控这个相关联的锁。其他的方法都必须在这个锁被锁上的情况下使用。
wait() 会释放这个锁，阻塞本线程直到其他线程通过 notify() 或 notify_all() 来唤醒它。一旦被唤醒，这个锁又被 wait() 锁上。

release和wait都有释放锁的作用，不同在于wait后，该子线程就在那里挂起等待，要继续执行，
就需要接收到notify或者notifyAll来唤醒线程，而release该线程还能继续执行。
"""

import _thread
import threading
from time import monotonic as _time
from itertools import islice as _islice, count as _count

_allocate_lock = _thread.allocate_lock

condition = threading.Condition()

try:
    _CRLock = _thread.RLock
except AttributeError:
    _CRLock = None

try:
    from _collections import deque as _deque
except ImportError:
    from collections import deque as _deque

_PyRLock = threading._RLock


def RLock(*args, **kwargs):
    """Factory function that returns a new reentrant lock.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it again
    without blocking; the thread must release it once for each time it has
    acquired it.

    """
    if _CRLock is None:
        return _PyRLock(*args, **kwargs)
    return _CRLock(*args, **kwargs)


class Condition:
    """
    Class that implements a condition variable.

    A condition variable allows one or more threads to wait until they are
    notified by another thread.

    If the lock argument is given and not None, it must be a Lock or RLock
    object, and it is used as the underlying基础 lock. Otherwise, a new RLock object
    is created and used as the underlying lock.

    """

    def __init__(self, lock=None):
        # 如果lock为none，则创建一个;
        # 定义lock，即为一级锁
        if lock is None:  # threading.Condition()中没传递参数，默认lock=None
            lock = RLock()  # # 它的底层也是维护了一个RLock锁【底层锁】
        self._lock = lock
        # Export the lock's acquire() and release() methods
        self.acquire = lock.acquire
        self.release = lock.release

        # If the lock defines _release_save() and/or _acquire_restore(),
        # these override the default implementations (which just call
        # release() and acquire() on the lock).  Ditto for _is_owned().
        # 如果lock类型定义了_release_save和_acquire_restore尝试重载他们;重载不掉就过，说明lock类型里面就有这种方式，直接pass;
        try:
            self._release_save = lock._release_save
        except AttributeError:
            pass
        try:
            self._acquire_restore = lock._acquire_restore
        except AttributeError:
            pass
        try:
            self._is_owned = lock._is_owned
        except AttributeError:
            pass
        # 双端队列存储所有等待中的锁
        self._waiters = _deque()  # _waiters 双端队列，注意文件开头的：from collection import deque as _deque.

    def __enter__(self):  # 直接继承于Lock的上下文管理方式
        return self._lock.__enter__()

    def __exit__(self, *args):  # 直接继承于Lock的上下文管理方式
        return self._lock.__exit__(*args)

    def __repr__(self):  # 特殊方法之一，将condition类用str字符串的方法输出时候，调用此方法
        return "<Condition(%s, %d)>" % (self._lock, len(self._waiters))

    def _release_save(self):  # 释放掉一级锁，保存状态
        self._lock.release()  # No state to save

    def _acquire_restore(self, x):  # 恢复一级锁
        self._lock.acquire()  # Ignore saved state

    def _is_owned(self):
        # Return True if lock is owned by current_thread.
        # This method is called only if _lock doesn't have _is_owned().
        # 如果一级锁由当前线程获得，返回True。它是怎么判断的呢？
        # 首先尝试获得一级锁，如果可以获得，那就说明当前线程没有锁，立马释放掉，返回false；反之，返回True；
        if self._lock.acquire(0):
            self._lock.release()
            return False
        else:
            return True

    def wait(self, timeout=None):  # wait()用于阻塞本线程，直到其他线程调用notify()唤醒或者timeout结束
        """等到收到通知或发生超时为止。

        如果调用此方法时调用线程尚未获取锁，调用后，将引发RuntimeError。

        此方法释放基础锁，然后阻塞直到在相同条件下被notify（）或notify_all（）调用唤醒变量在另一个线程中，或者直到发生可选超时为止。一旦
        唤醒或超时后，它将重新获取锁并返回。

        如果存在timeout参数而不是None，则应为浮点数，以秒为单位指定操作超时（或其分数）。

        当基础锁是RLock时，不会使用其锁释放它release（）方法，因为这可能在锁定时实际上并未解锁
        被递归多次获得。而是一个内部接口使用了RLock类的，即使它具有被递归收购了好几次。另一个内部接口是
        然后在重新获得锁定时用于恢复递归级别。

        wait方法释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。
        当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。

        """
        # wait在锁被锁上的情况下使用
        if not self._is_owned():  # 线程想等待，自己要有锁吧；所以判断当前线程是否有锁，没有就抛出异常；
            raise RuntimeError("cannot wait on un-acquired lock")
        waiter = _allocate_lock()  # 创建一个新的锁对象，返回lock object
        # 再定义一个lock方法，变量waiter，并获得这个二级锁（注意，RLock是递归锁，可以嵌套）；把这个锁添加进全局私有_waiter 集合
        waiter.acquire()
        self._waiters.append(waiter)
        saved_state = self._release_save()  # 保存状态，释放一级锁；可以让其他线程获得，这样才能调用notify()
        gotit = False  # 定义一个bool类型的返回值gotit
        try:  # restore state no matter what (e.g., KeyboardInterrupt)
            if timeout is None:  # 如果timeout == None，waiter上锁，线程就此阻塞，并且gotit = true ，等待有效
                waiter.acquire()
                gotit = True
            else:  # 否则判断timeout的正负性，如果正的，就获得锁线程就此阻塞，返回True赋值给gotit；反之返回False，等待失败；
                if timeout > 0:
                    gotit = waiter.acquire(True, timeout)
                else:
                    gotit = waiter.acquire(False)
            return gotit
        finally:  # 不管try是否含有return，不管try是否抛出异常，finally都会return之前执行。
            """
            注意到wait()有可能被用户和系统中断，导致没有上锁的waiter进入了_waiters队列：
            finally中首先尝试恢复线程一级锁，也就是等待其他线程释放一级锁；没有就会一直等待。
            也就是说，调用notify函数的线程一定要释放掉底层锁，其他线程才会继续执行。
            
            进一步判断gotit，如果为False，说明waiter没有释放，我们从_waiters中剔除它，
            注意他会和下面的notify()函数同时尝试，报错的话pass就行。
            """
            self._acquire_restore(saved_state)
            if not gotit:
                try:
                    self._waiters.remove(waiter)
                except ValueError:
                    pass

    def wait_for(self, predicate, timeout=None):  # 断言等待函数
        """Wait until a condition evaluates to True.

        predicate should be a callable which result will be interpreted as a
        boolean value.  A timeout may be provided giving the maximum time to
        wait.

        """
        # 定义了变量 endtime 结束时间和 waittime 等待时间，分别初始化为：None和传入的参数timeout。
        endtime = None
        waittime = timeout
        # 获得断言的返回值，值得注意的是，断言的运行也是需要不少时间的，这个时间可能超过线程期望等待时间，下面就是要解决此问题。
        result = predicate()
        # 断言为False则进入循环
        """
        首先waittime，也就是timeout，不能是None；如果是None，那就没啥好说的，直接等待吧；如果不是才要继续判断。
        在第一次进入循环的时候，计算出剩余的等待时间（扣除第一次等待断言返回的时间）。
        这个时间太长就不能等待了；否则的话，等待剩余时间waittime，进而再计算断言；不管断言结果如何，都只能跳出循环了，
        因为waittime一定是<=0的。
        """
        while not result:
            if waittime is not None:
                if endtime is None:
                    endtime = _time() + waittime
                else:
                    waittime = endtime - _time()
                    if waittime <= 0:
                        break
            self.wait(waittime)
            result = predicate()
        return result

    def notify(self, n=1):  # notify()唤醒线程队列中前n个线程
        """Wake up one or more threads waiting on this condition, if any.

        If the calling thread has not acquired the lock when this method is
        called, a RuntimeError is raised.

        This method wakes up at most n of the threads waiting for the condition
        variable; it is a no-op if no threads are waiting.

        """
        # 和wait一样，必须在已获得Lock的前提下调用，否则将引发错误
        if not self._is_owned():  # 自己获得一级锁
            raise RuntimeError("cannot notify on un-acquired lock")

        all_waiters = self._waiters  # 备份当前线程队列

        # islice(iterable, stop) --> islice object
        waiters_to_notify = _deque(_islice(all_waiters, n))  # 定义新得队列，将前n个线程转移至此，islice返回一个迭代器

        if not waiters_to_notify:  # 队列为空则返回，有可能被异常中断了
            return

        # 循环释放二级锁，wait函数中的wait.acquire()唤醒；最后尝试将线程踢出队列；和wait()两者共同尝试，
        # 有一个成功了就行，要是抛出异常了就pass。
        for waiter in waiters_to_notify:
            waiter.release()
            try:
                all_waiters.remove(waiter)
            except ValueError:
                pass

    def notify_all(self):
        """Wake up all threads waiting on this condition.

        If the calling thread has not acquired the lock when this method
        is called, a RuntimeError is raised.

        """
        self.notify(len(self._waiters))

    notifyAll = notify_all
