# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        0.UnderStand
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------
举个例子：假设有1个洗衣房，里面有10台洗衣机，有一个洗衣工在负责这10台洗衣机。那么洗衣房就相当于1个进程，洗衣工就相当1个线程。
如果有10个洗衣工，就相当于10个线程，1个进程是可以开多线程的。这就是多线程！

那么协程呢？先不急。大家都知道，洗衣机洗衣服是需要等待时间的，如果10个洗衣工，1人负责1台洗衣机，这样效率肯定会提高，但是不觉得浪费资源吗？
明明1 个人能做的事，却要10个人来做。只是把衣服放进去，打开开关，就没事做了，等衣服洗好再拿出来就可以了。
就算很多人来洗衣服，1个人也足以应付了，开好第一台洗衣机，在等待的时候去开第二台洗衣机，再开第三台，……直到有衣服洗好了，
就回来把衣服取出来，接着再取另一台的（哪台洗好先就取哪台，所以协程是无序的）。这就是计算机的协程！洗衣机就是执行的方法。

当你程序中方法需要等待时间的话，就可以用协程，效率高，消耗资源少。
好了！现在来总结一下：
洗衣房 ==> 进程
洗衣工 ==> 线程
洗衣机 ==> 方法（函数）
"""

"""
正常的函数在执行时是不会中断的，所以你要写一个能够中断的函数，就需要添加async关键。

async 用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，去执行其他异步函数，
等到挂起条件（假设挂起条件是sleep(5)）消失后，也就是5秒到了再回来执行。

await 用来用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异步程序。
await 后面只能跟异步程序或有__await__属性的对象，因为异步程序与一般程序不同。

假设
有两个异步函数async a，async b，a中的某一步有await，当程序碰到关键字await b()后，异步程序挂起后去执行另一个异步b程序，
就是从函数内部跳出去执行其他函数，当挂起条件消失后，不管b是否执行完，要马上从b程序中跳出来，回到原程序执行原来的操作。
如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，无法在b执行的过程中返回。如果要在b执行完才返回，
也就不需要用await关键字了，直接调用b函数就行。所以这就需要await后面跟的是异步函数了。在一个异步函数中，可以不止一次挂起，
也就是可以用多个await。
"""

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():

    # print(f"started at {time.strftime('%X')}")
    # all_tasks = asyncio.all_tasks()
    # await say_after(1, 'hello')
    # all_tasks = asyncio.all_tasks()
    # await say_after(2, 'world')
    # all_tasks = asyncio.all_tasks()
    # print(f"finished at {time.strftime('%X')}")


    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    all_tasks = asyncio.all_tasks()

    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

    # print(f"started at {time.strftime('%X')}")
    # ret = await asyncio.gather(say_after(1, 'hello'), say_after(2, 'world'))
    # print(ret)
    # print(f"finished at {time.strftime('%X')}")




asyncio.run(main())
