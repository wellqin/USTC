#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/3 09:14
@Author  : qinwei05
"""
from greenlet import greenlet


class Coroutine:
    """
    协程的四种实现方式
    协程不是计算机提供的，是程序员认为创造协程也被称为微线程，是一种用户态的上下文切换技术，
    简而言之，就是通过一个线程实现代码互相切换执行实现协程的几种方法.
    """

    def __init__(self):
        pass  # test

    @staticmethod
    def greenlet_func():
        """
        1)greenlet, 早期模块
        注意：switch 中也可以传递参数用于在切换执行时相互传递值。
        输出的结果:
        1
        3
        2
        4
        """
        def func1():
            print(1)  # 第2步：输出 1
            gr2.switch()  # 第3步：切换到 func2 函数
            print(2)  # 第6步：输出 2
            gr2.switch()  # 第7步：切换到 func2 函数，从上一次执行的位置继续向后执行

        def func2():
            print(3)  # 第4步：输出 3
            gr1.switch()  # 第5步：切换到 func1 函数，从上一次执行的位置继续向后执行
            print(4)  # 第8步：输出 4

        gr1 = greenlet(func1)
        gr2 = greenlet(func2)
        gr1.switch()  # 第1步：去执行 func1 函数

    @staticmethod
    def yield_func():
        """
        2)基于 Python 的生成器的 yield 和 yield form 关键字实现协程代码。
        注：用这种方法比较牵强，真正开发环境中基本不会用这种方法实现协程 (yield form 关键字是在 Python3.3 中引入的。)
        执行结果
        1
        3
        4
        2
        """
        def func1():
            yield 1  # 第一步执行这里会生成1
            # Python 版本 2.7 不支持此语法。自 Python 3.3 起可以委托给子生成器；改为对子生成器使用显式迭代。
            yield from func2()  # 这里会跳到func2，然后执行里面的代码，执行完func2函数后会继续以跳转之前的状态继续执行以下代码
            yield 2

        def func2():
            yield 3
            yield 4

        # 这里是一个生成器对象
        f1 = func1()
        # 遍历执行生成器
        for item in f1:
            print(item)




if __name__ == "__main__":
    coroutine = Coroutine()
    coroutine.greenlet_func()
    coroutine.yield_func()

