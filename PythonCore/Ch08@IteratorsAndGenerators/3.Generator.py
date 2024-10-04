# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.Generator
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

1.3、生成器函数的使用
    生成器函数，函数里只要有yield关键字。
"""


def func():
    return 1
    # return 2 # 不能一直返回，用yield生成器方案
    # return 3


def gen_func():  # 提交的值都能for循环打印出来
    yield 1
    yield 2
    yield 3


def fib(index):  # 1、求斐波拉契只能看见最终结果，看不到过程
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):  # 2、改动之后，将每次产生的值添加到列表中，就可以看到过程中产生的值
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


def gen_fib(index):  # 3、用生成器改动，将每次结果yield出来，
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


# 斐波拉契 0 1 1 2 3 5 8
# 惰性求值， 延迟求值提供了可能


if __name__ == "__main__":
    # 原来普通方式
    # re = func()
    # print(re)

    # gen为生成器对象， python编译字节码的时候就产生了
    gen = gen_func()
    # 1.用next方式调用
    # print(next(gen))  # 1
    # print(next(gen))  # 2
    # print(next(gen))  # 3
    # print(next(gen))  # StopIteration，迭代空时报错

    # 2.用for循环调用迭代
    for value in gen:
        print(value, end=' ')  # 1 2 3

    print()
    # 应用：利用生成器将yield提交的值遍历出来
    for data in gen_fib(10):
        print(data, end=" ")  # 1 1 2 3 5 8 13 21 34 55
