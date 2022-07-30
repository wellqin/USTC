# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.CoroutineNesting
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------
协程嵌套

1.run_util_complete()源码：和get_event_loop中的run_forever()区别并不大，
    只是可以在运行完指定的协程后可以把loop停止掉，而run_forever()不会停止

2.loop会被放在future里面，future又会放在loop中，容易形成环状

3.取消future(task)：
    3.1 子协程调用原理：官网例子

    解释：await相当于yield from，loop运行协程print_sum(),print_sum又会去调用另一个协程compute，
         run_util_complete会把协程print_sum注册到loop中。

        1).event_loop会为print_sum创建一个task，通过驱动task执行print_sum
        （task首先会进入pending【等待】的状态）；

        2).print_sum直接进入字协程的调度，这个时候转向执行另一个协程
        （compute，所以print_sum变为suspended【暂停】状态）；

        3).compute这个协程首先打印，然后去调用asyncio的sleep（此时compute进入suspende的状态【暂停】），
        直接把返回值返回给Task（没有经过print_sum，相当于yield from，直接在调用方和子生成器通信，是由委托方print_sum建立的通道）；

        4).Task会告诉Event_loop暂停，Event_loop等待一秒后，通过Task唤醒（越过print_sum和compute建立一个通道）；

        5).compute继续执行，变为状态done【执行完成】，然后抛一个StopIteration的异常，会被await语句捕捉到，
        然后提取出1+2=3的值，进入print_sum,print_sum也被激活（因为抛出了StopIteration的异常被print_sum捕捉），
        print_sum执行完也会被标记为done的状态，同时抛出StopIteration会被Task接收
"""

import asyncio


# # 协程嵌套实例
# async def compute(x, y):
#     print("Compute %s + %s .." % (x, y))
#     await asyncio.sleep(1.0)
#     return x + y
#
#
# async def print_sum(x, y):
#     result = await compute(x, y)
#     print("%s + %s = %s" % (x, y, result))
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_sum(1, 2))  # loop.run_forever()不会停止
# # Compute 1 + 2 ..
# # 1 + 2 = 3
#
# # 在运行完指定的协程后run_until_complete可以把loop停止掉，原因何在
# # 看python\Lib\asyncio\base_events.py中有run_until_complete源码
# loop.close()


"""
# run_until_complete源码

def run_until_complete(self, future):
    # Run until the Future is done.
    # If the argument is a coroutine, it is wrapped in a Task.
    # WARNING: It would be disastrous to call run_until_complete()
    # with the same coroutine twice -- it would wrap it in two
    # different Tasks and that can't be good.
    # Return the Future's result, or raise its exception.

    self._check_closed()

    new_task = not isinstance(future, futures.Future)
    future = tasks.ensure_future(future, loop=self)
    if new_task:
        # An exception is raised if the future didn't complete, so there
        # is no need to log the "destroy pending task" message
        future._log_destroy_pending = False

    future.add_done_callback(_run_until_complete_cb)  # 注意这里，加入了回调函数
    try:
        self.run_forever()
    except:
        if new_task and future.done() and not future.cancelled():
            # The coroutine raised a BaseException. Consume the exception
            # to not log a warning, the caller doesn't have access to the
            # local task.
            future.exception()
        raise
    future.remove_done_callback(_run_until_complete_cb)
    if not future.done():
        raise RuntimeError('Event loop stopped before Future completed.')

    return future.result()
        

def _run_until_complete_cb(fut):
    exc = fut._exception
    if (isinstance(exc, BaseException)
    and not isinstance(exc, Exception)):
        # Issue #22429: run_forever() already finished, no need to
        # stop it.
        return
    fut._loop.stop()  # 回调函数_run_until_complete_cb可以终止协程
"""


# 取消future(task)示例，在console用运行，触发KeyboardInterrupt，即Ctrl + C
async def get_html(sleep_time):
    print("waiting")
    await asyncio.sleep(sleep_time)
    print("done after {}s".format(sleep_time))


task1 = get_html(2)
task2 = get_html(3)
task3 = get_html(30)
tasks = [task1, task2, task3]
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:  # 人工按键停止，希望终止所有协程
    # 这里没用loop，怎么直接获取到所有task呢？
    # 在源码中看过程
    """
        def all_tasks(cls, loop=None):
        # Return a set of all tasks for an event loop.
        # By default all tasks for the current event loop are returned.
        if loop is None:  # 如果没传递loop，回去自动找，在通过循环获取loop中的所有task
            loop = events.get_event_loop()
        return {t for t in cls._all_tasks if t._loop is loop}
    """
    all_tasks = asyncio.all_tasks(loop)  # 获取所有协程task, 3.9中把asyncio.Task.all_tasks移除了，用asyncio.all_tasks代替
    for task in all_tasks:
        print("cancel task")
        print(task.cancel())  # 返回bool值，运行中的task不可以被cancel，在asyncio.sleep中触发异常，全部返回TRUE
    loop.stop()  # 必须加这二句，否则异常pending
    print("loop状态", loop.is_running())
    loop.run_forever()
    print("loop状态", loop.is_running())
finally:
    print("loop状态", loop.is_running())
    loop.close()
