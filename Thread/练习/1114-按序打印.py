# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1114-按序打印
Description :   
Author :          wellqin
date:             2020/3/24
Change Activity:  2020/3/24
-------------------------------------------------
"""
# 我们提供了一个类：
# public class Foo {
#   public void one() { print("one"); }
#   public void two() { print("two"); }
#   public void three() { print("three"); }
# }
#
# 三个不同的线程将会共用一个 Foo 实例。
#
#
# 线程 A 将会调用 one() 方法
# 线程 B 将会调用 two() 方法
# 线程 C 将会调用 three() 方法
#
#
# 请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: "onetwothree"
# 解释:
# 有三个线程会被异步启动。
# 输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
# 正确的输出是 "onetwothree"。
#
#
# 示例 2:
# 输入: [1,3,2]
# 输出: "onetwothree"
# 解释:
# 输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
# 正确的输出是 "onetwothree"。

# 注意:
# 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
# 你看到的输入格式主要是为了确保测试的全面性。

from threading import Condition, Thread

"""
class Foo:
    def __init__(self):
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
"""

# class Foo:
#     def __init__(self):
#         self.t = 0
#
#     def first(self, printFirst: 'Callable[[], None]') -> None:
#         printFirst()
#         self.t = 1
#
#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         while self.t != 1:
#             pass
#         printSecond()
#         self.t = 2
#
#     def third(self, printThird: 'Callable[[], None]') -> None:
#         while self.t != 2:
#             pass
#         printThird()
from threading import Condition, Thread


"""
# 线程 A 将会调用 one() 方法, print('one', end='')
# 线程 B 将会调用 two() 方法, print('two', end='')
# 线程 C 将会调用 three() 方法, print('three', end='')

确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。
即不管输入什么，必须确保输出"onetwothree"
"""
def One():
    print('one', end='')


def Two():
    print('two', end='')


def Three():
    print('three', end='')


class Foo:
    def __init__(self):
        self.cd = Condition()
        self.NUM = 0

    def first(self, PrintFirst: callable):
        # 这里使用with语法糖
        with self.cd:
            while self.NUM != 0:
                self.cd.wait()
            PrintFirst()
            self.NUM += 1
            self.cd.notify_all()

    def Second(self, PrintSecond: callable):
        self.cd.acquire()
        while self.NUM != 1:
            self.cd.wait()
        PrintSecond()
        self.NUM += 1
        self.cd.notify_all()
        self.cd.release()

    def Third(self, PrintThird: callable):
        self.cd.acquire()
        while self.NUM != 2:
            self.cd.wait()
        PrintThird()
        self.NUM += 1
        self.cd.notify_all()
        self.cd.release()


if __name__ == '__main__':
    foo = Foo()
    callablelist = [foo.first, foo.Second, foo.Third]
    callablelistargs = [One, Two, Three]
    order = [2, 1, 3]
    A = Thread(target=callablelist[order[0] - 1], args=(callablelistargs[order[0] - 1],))
    B = Thread(target=callablelist[order[1] - 1], args=(callablelistargs[order[1] - 1],))
    C = Thread(target=callablelist[order[2] - 1], args=(callablelistargs[order[2] - 1],))
    A.start()
    B.start()
    C.start()
