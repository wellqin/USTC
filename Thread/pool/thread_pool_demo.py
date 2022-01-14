# -*- coding:utf-8 -*-


# @see https://docs.python.org/zh-cn/3/library/concurrent.futures.html
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor


# 任务
def task(task_id):
    thread_name = threading.current_thread().name
    print('worker【%s】is processing【%d】：do something...' % (thread_name, task_id))


# 耗时任务
def task_two(task_id, consuming):
    thread_name = threading.current_thread().name
    print('工人【%s】正在处理任务【%d】：do something...' % (thread_name, task_id))
    # 模拟任务耗时(秒)
    time.sleep(consuming)
    print('任务【%d】：done' % task_id)


def main():
    """
        # 1）一个工人同一时间只做一个任务，但做完一个任务可以接着做下一个任务；
        # 2）可以分配多个任务给少量工人，减少人员成本开销。
    """
    # 初始化线程池(商会)，定义好池里最多有几个工人
    pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix='Thread')
    # 准备10个任务
    for i in range(10):
        # 提交任务到池子(商会)里（它会自动分配给工人）
        pool.submit(task, i+1)


def main_two():
    """
        # 1）一个工人同一时间只做一个任务，但做完一个任务可以接着做下一个任务；
        # 2）可以分配多个任务给少量工人，减少人员成本开销。
        # 3）任务按顺序分配给空闲工人，但每个任务的耗时不一样，任务不是按顺序被完成的，后提交的任务可能会先被完成
    """
    # 5个工人
    pool = ThreadPoolExecutor(max_workers=5, thread_name_prefix='Thread')
    # 准备10个任务
    for i in range(10):
        # 模拟任务耗时(秒)
        consuming = random.randint(1, 5)
        pool.submit(task_two, i + 1, consuming)


def pow_num(num):
    return num * num


if __name__ == '__main__':
    # 线程被复用了，而且 Thread_0 被复用了最多次，而 Thread_4 毫无用武之地，没有使用到（你可以把任务数量调大，看看结果又会是怎么样？）
    # main()
    print("===================================")
    # 多线程是异步的，且会并发
    # main_two()

    executor = ThreadPoolExecutor(max_workers=3)
    future = executor.submit(pow_num, 5)
    print('future: {}'.format(future))
    result = future.result()
    print('result: {}'.format(result))
