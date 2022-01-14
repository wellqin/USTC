# -*- coding:utf-8 -*-
import time

from func_timeout import func_set_timeout
import func_timeout
import retrying

"""
retrying根据的超时异常func_timeout.exceptions.FunctionTimedOut进行重试（也可以自己写自己的Exception，包装异常信息，方便后面排查）

"""


@func_set_timeout(3)  # 设定函数超执行时间_
def task():
    print('开始执行')
    time.sleep(5)
    return '执行成功_未超时'


if __name__ == '__main__':
    try:
        print(task())
    # 若调用函数超时自动走异常(可在异常中写超时逻辑处理)
    except func_timeout.exceptions.FunctionTimedOut:
        print('执行函数超时')
