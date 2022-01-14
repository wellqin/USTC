# -*- coding:utf-8 -*-


import random
import time

import func_timeout
import retrying
from func_timeout import func_set_timeout


class MyException(Exception):
    # retrying根据的超时异常func_timeout.exceptions.FunctionTimedOut进行重试
    # （也可以自己写自己的Exception，包装异常信息，方便后面排查）
    def __init__(self, message):
        self.message = message

    def __str__(self):
        message = 'Sleep timeout: "{}"'.format(self.message)
        print(message)
        return message


def sleep(sleep_time: int):

    @func_set_timeout(3)
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
    return isinstance(exception, MyException)


# #此处的wait_fixed指的是被retrying修饰的函数每次重试的间隔时间，区别于上面的timeout
@retrying.retry(retry_on_exception=sleep_timeout, stop_max_attempt_number=10, wait_fixed=2000)
def test():
    print('start @ ', time.asctime())
    # sleep(random.randint(2, 5))
    sleep(5)
    print('end')


if __name__ == '__main__':
    random.seed(1234)
    test()
