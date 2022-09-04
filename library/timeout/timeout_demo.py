# -*- coding:utf-8 -*-
import time

from func_timeout import func_set_timeout
import func_timeout
import retrying

"""
retrying根据的超时异常func_timeout.exceptions.FunctionTimedOut进行重试（也可以自己写自己的Exception，包装异常信息，方便后面排查）

"""

# 设定函数执行的时间，超过就停止
# @param timeout int/float、lambda/function
# @param allowOverride <bool> Default False, 如果为True时，参数timeout为数字时，将被覆盖，为函数时将不会执行


@func_set_timeout(timeout=3, allowOverride=True)  # 设定函数超执行时间
def task(forceTimeout):
    """
    task被重新包装为：task = func_set_timeout(3)(task)
    task()相当于执行：func_set_timeout(3)(task)()
    @return:
    """
    while True:
        print('hello world')
        print('force_timeout = ', forceTimeout)
        time.sleep(1)
    print("执行函数中")
    return '执行成功_未超时'


if __name__ == '__main__':
    try:
        print("开始执行函数")
        print(task(forceTimeout=5))
        # 若调用函数超时自动走异常(可在异常中写超时逻辑处理)
    except func_timeout.exceptions.FunctionTimedOut:
        print('超时时执行的函数')
    finally:
        print("都执行的函数")
