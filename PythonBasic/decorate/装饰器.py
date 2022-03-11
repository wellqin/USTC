# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        装饰器
Description :   
Author :          wellqin
date:             2019/9/1
Change Activity:  2019/9/1
-------------------------------------------------

装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，

比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。

装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能。

总结几种类型：
装饰器修饰的函数参数：无参数 | 一个参数 | 任意参数   【二层函数嵌套】
装饰器本身的参数：最外层为装饰器参数 【三层函数嵌套】
元信息保存：from functools import wraps 中使用进行装饰 @wraps(func)

"""


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()

    return wrapper


@debug
def say_hello():  # 无参数
    print("hello!")


print("==========初级部分：装饰器无参数==============")
say_hello()

"""
这是最简单的装饰器，但是有一个问题，如果被装饰的函数需要传入参数，那么这个装饰器就坏了。
因为返回的函数并不能接受参数，你可以指定装饰器函数wrapper接受和原函数一样的参数，比如：
"""


def debug1(func):
    def wrapper(something):  # 指定一毛一样的参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(something)

    return wrapper  # 返回包装过函数


@debug1
def say(something):
    print("hello {}!".format(something))


print("==========初级部分：装饰器有指定参数==============")
say("wellqin")

"""
这样你就解决了一个问题，但又多了N个问题。因为函数有千千万，你只管你自己的函数，别人的函数参数是什么样子，鬼知道？
还好Python提供了可变参数*args和关键字参数**kwargs，有了这两个参数，装饰器就可以用于任意目标函数了。
"""


def debug2(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...', )
        return func(*args, **kwargs)

    return wrapper  # 返回


@debug2
def say2(something):
    print("hello {}!".format(something))


print("==========初级部分：装饰器有任意参数==============")
say2("wellqin2")

# 高级部分：装饰器本身的参数
print("==========高级部分：装饰器本身的参数==============")
"""
带参数的装饰器#
假设我们前文的装饰器需要完成的功能不仅仅是能在进入某个函数后打出log信息，而且还需指定log的级别，那么装饰器就会是这样的。

你可以这么理解，当带参数的装饰器被打在某个函数上时，比如@logging(level='DEBUG')，
它其实是一个函数，会马上被执行，只要这个它返回的结果是一个装饰器时，那就没问题。细细再体会一下。
"""
from functools import wraps


def logging(level=None):  # 支持默认参数None
    def wrapper(func):
        @wraps(func)  # 加上后 -- say123.__name__ say123
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


# @logging(level='INFO')
@logging()  # 支持默认参数
def say123(something):
    print("say {}!".format(something))


print("say123.__name__", say123.__name__)  # inner_wrapper, 这样有大问题，原函数变了


# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do123(something):
    print("do {}...".format(something))


say123('hello')
do123("my work")

# 元信息
"""
问题，我们使用的其实已经不再是原函数了，而是一个由装饰器返回的新函数，虽然这个函数的功能和原函数一样，但是一些基础的信息其实已经丢失了。

正常的函数调用__name__返回的都是函数的名称，但是当我们加上了装饰器的注解之后，就会发生变化，同样，我们输出加上了装饰器注解之后的

我们会发现输出的结果变成了wrapper，这是因为我们实现的装饰器内部的函数叫做wrapper。
不仅仅是__name__，函数内部还有很多其他的基本信息，比如记录函数内描述的__doc__，__annotations__等等，
这些基本信息被称为是元信息，这些元信息由于我们使用注解发生了丢失。
"""
# Python当中为我们提供了一个专门的装饰器用来保留函数的元信息，我们只需要在实现装饰器的wrapper函数当中加上一个注解wraps即可
# @wraps(func) 加上了这个注解之后，我们再来检查函数的元信息，会发现它和我们预期一致了
# 参考上面实例：line83


# 自行实例
from functools import wraps
import time


def timeSpend(func):  # 1
    @wraps(func)
    def wrapper(*args, **kwargs):  # 3
        st = time.time()  # 4
        f = func(*args, **kwargs)  # 5  # 10 --> f接受了第9步的返回值li
        lt = time.time() - st
        print('%.8f' % lt)
        print(func.__name__)
        return f  # 11

    return wrapper  # 2


@timeSpend
def iterFunc(m):  # 6
    li = []
    for i in range(m):  # 7
        li.append(i ** 2)
    print(len(li))  # 8
    return li  # 9


n = 10
print(iterFunc(n))  # 先执行timeSpend，timeSpend里面有func(*args, **kwargs)，就是iterFunc
# iterFunc作为参数传给timeSpend(func)
"""
注意打印的顺序

10
0.00000000
iterFunc
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

import random


def provide_number(min_num, max_num):
    """装饰器：随机生成一个在 [min_num, max_num] 范围的整数，追加为函数的第一个位置参数
    """

    def wrapper(func):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)
            # 将 num 作为第一个参数追加后调用函数
            return func(num, *args, **kwargs)

        return decorated

    return wrapper


class Foo:
    @provide_number(1, 100)
    def print_random_number(self, num):
        print(num)


# OUTPUT: <__main__.Foo object at 0x104047278>
Foo().print_random_number()
