# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        72.Close
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------

2.close()方法：（关闭生成器）
        自己处理的话会抛异常，gen.close()，RuntimeError: generator ignored GeneratorExit，
        如果不处理，正确关闭的话一切正常
        所以自己不要随意去异常处理yield

        如果是except Exception就不会抛异常，
        GeneratorExit是继承至BaseException的，Exception也是继承于BaseException的
"""


def gen_func():
    # 自己处理的话会抛异常，gen.close()，RuntimeError: generator ignored GeneratorExit
    try:
        yield 'https://www.baidu.com'
    # 如果是except Exception就不会抛异常，GeneratorExit是继承至BaseException的，Exception也是继承于BaseException的
    except GeneratorExit as e:  # 如果是except Exception就不会抛异常
        pass  # raise StopIteration

    # yield 'https://www.baidu.com'  # 不进行异常捕获，则close后StopIteration
    yield 1
    yield 2
    return 'LYQ'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()  # 自己处理异常时，此处RuntimeError: generator ignored GeneratorExit
    # print(next(gen))  # close后抛异常类型StopIteration：
