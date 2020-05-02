"""
-------------------------------------------------
File Name:        Lock
Author :          wellqin
date:             2020/4/24
-------------------------------------------------
线程同步：Lock、Rlock锁机制

使用锁的原因
为了避免线程间进行数据竞争，有时必须使用一些机制来强制线程同步。因为Cpython解释器中GIL(全局解释锁)的存在
在每一时刻只有一个线程在CPU中执行，每个线程执行了一定数量的字节码或者过了一定的时间切片再或者遇到了IO操作，
CPU就会切换其他线程执行部分字节码。那么如果使用两个线程分别执行add()、reduce()方法，在理论情况下最后的结果num可能是0、1、-1，
因为代码分解为字节码时，就分解成了很多步骤，有可能某个线程只执行了一些字节码，又去执行另一个线程的字节码，这样就可能造成结果的错乱。

  5           0 LOAD_FAST         0 (num)  加载变量num到内存
              2 LOAD_CONST        1 (1)    加载变量1到内存
              4 INPLACE_ADD                执行加法
              6 STORE_FAST        0 (num)  将结果赋值给num

  6           8 LOAD_FAST         0 (num)
             10 RETURN_VALUE      None

 10           0 LOAD_FAST                0 (num)
              2 LOAD_CONST               1 (1)
              4 INPLACE_SUBTRACT
              6 STORE_FAST               0 (num)

 11           8 LOAD_FAST                0 (num)
             10 RETURN_VALUE             None


class Lock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> Optional[bool]: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...
    def locked(self) -> bool: ...


class _RLock:
    def __init__(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> Optional[bool]: ...
    if sys.version_info >= (3,):
        def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
    else:
        def acquire(self, blocking: bool = ...) -> bool: ...
    def release(self) -> None: ...


RLock = _RLock

"""


import threading

num = 0


def add(lock):
    global num
    for i in range(10):
        lock.acquire()  # 默认TRUE，阻塞
        num += 1
        lock.release()


def reduce(lock):
    global num
    for i in range(10):
        lock.acquire()
        num -= 1
        lock.release()


# 创建锁
lock = threading.Lock()
# 创建线程
t1 = threading.Thread(target=add, args=(lock, ))
t2 = threading.Thread(target=reduce, args=(lock, ))
t1.start()
t2.start()
# 等待子进程执行完
t1.join()
t2.join()
print(num)
