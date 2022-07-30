# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        9.AsyncAndAwait
Description :   
Author :          wellqin
date:             2020/4/20
Change Activity:  2020/4/20
-------------------------------------------------

八. async和await原生协程
1.python为了将语义变得更加明确，就引入了async和await关键字定义原生的协程：
    生成器实现的协程又可以当生成器，又可以当协程，且代码凌乱，不利于后期维护。原生的协程中不可以yield，否则会抛错（让协程更加明确）

可异步调用：实际实现了__await__魔法函数
await：将控制权交出去并等待结果返回,await只能接收awaitable对象，可以理解成yield from
"""
import types
# from collections import Awaitable


# async def downloader(url):
#     return "leven"
#
#
# async def download_url(url):
#     # dosomethings
#     # async里面不能写yield与yield from
#     html = await downloader(url)  # await委托并等待downloader返回
#     return html
#
#
# coro = download_url("http://www.imooc.com")
# # next(None)    # 不能这样调用  TypeError: 'NoneType' object is not an iterator
# coro.send(None)

"""
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-3-879770ebad5e> in <module>
if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
----> 9     coro.send(None)

StopIteration: leven
"""


# 用yield 可以实现 生成器和协程，但容易混淆，就引入了await关键字
# 如果是函数,就要使用coroutine装饰器，实际将__await_指向___iter__
@types.coroutine  # 加上就不会抛出异常，将__await_指向___iter__
def downloader(url):
    yield "lewen"


async def download_url(url):
    # dosomethings
    # 将控制权交出去并等待结果返回,await只能接收awaitable对象，可以理解成yield from
    html = await downloader(url)
    return html


if __name__ == "__main__":
    coro = download_url("http://www.imooc.com")
    # next(None)    # 不能这样调用
    coro.send(None)
