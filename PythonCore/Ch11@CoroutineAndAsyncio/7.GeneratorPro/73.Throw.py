# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        73.Throw
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------

3.throw()方法：向生成器中扔异常，需要自己处理，否则会抛错
"""


def gen_func():
    try:
        yield 'https://www.baidu.com'
    except Exception:
        pass

    # yield 'https://www.baidu.com'  # 变成上面处理后，不会报异常 'download error'
    yield 1
    yield 2
    return 'LYQ'


if __name__ == '__main__':
    # 抛异常StopIteration：
    gen = gen_func()
    print(next(gen))  # 'https://www.baidu.com'

    # 扔一个异常，是第一句的异常,即yield 'https://www.baidu.com'的异常
    # 此时我们可以进行异常处理，即try...expect...
    gen.throw(Exception, 'download error')
    print(next(gen))  # 2

    # 扔一个异常，是第二句的异常，即
    gen.throw(Exception, 'download error')
    print(next(gen))
