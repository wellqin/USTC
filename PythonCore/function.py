# -*- coding:utf-8 -*-
from pprint import pprint


def until(n, filter_func, v):
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v + 1)


def example(a, b, **kw):
    return a * b


if __name__ == "__main__":
    pprint(until(10, lambda x: x % 3 == 0 or x % 5 == 0, 0))
    # 纯函数
    pprint(type(example))
    pprint(example.__code__.co_varnames)
    pprint(example.__code__.co_argcount)
