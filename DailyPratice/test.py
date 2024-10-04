"""
-------------------------------------------------
File Name:        test
Author :          wellqin
date:             2020/4/29
-------------------------------------------------
"""
from functools import wraps
import time


def timeSpend(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        f = func(*args, **kwargs)
        lt = time.time() - st
        print('%.8f' % lt)
        print(func.__name__)
        return f

    return wrapper


@timeSpend
def iterFunc(m):
    li = []
    for i in range(m):
        li.append(i ** 2)
    print(len(li))
    return li


n = 10
print(iterFunc(n))
