# -*- coding:utf-8 -*-


import random
import time

import func_timeout
from retrying import retry
from func_timeout import func_set_timeout


def retry_if_error(exception):
    print("---------------------------")
    return isinstance(exception, func_timeout.exceptions.FunctionTimedOut)


@retry(retry_on_exception=retry_if_error)
@func_set_timeout(3)
def timeout_retry_task():
    """
    这两个模块都是装饰器，第一个能让python函数超时时候抛出一个超时异常，第二个能让python函数异常时候重试
    根据这两个模块的功能，把他们用到一起，就能实现函数超时重试的功能
    """
    while True:
        print('hello world')
        time.sleep(1)


class MyException(Exception):
    # retrying根据的超时异常func_timeout.exceptions.FunctionTimedOut进行重试
    # （也可以自己写自己的Exception，包装异常信息，方便后面排查）
    def __init__(self, message):
        self.message = message

    def __str__(self):
        message = 'Sleep timeout: "{}"'.format(self.message)
        print(message)
        return message


def func(sleep_time: int):
    @func_set_timeout(1)
    def do_sleep():
        print('sleep time ', sleep_time)
        time.sleep(sleep_time)

    try:
        do_sleep()
        print('sleep finish')
    except func_timeout.exceptions.FunctionTimedOut:
        print('sleep timeout')
        raise MyException(sleep_time)


def sleep_timeout(exception: Exception) -> bool:
    """
    Exception
    @param exception:
    @return:
    """
    return isinstance(exception, MyException)


# #此处的wait_fixed指的是被retrying修饰的函数每次重试的间隔时间，区别于上面的timeout
@retry(retry_on_exception=sleep_timeout, stop_max_attempt_number=3, wait_fixed=200)
def test():
    print('\nstart @ ', time.asctime())
    # sleep(random.randint(2, 5))
    func(2)
    print('end')


if __name__ == '__main__':
    # random.seed(1234)
    test()
