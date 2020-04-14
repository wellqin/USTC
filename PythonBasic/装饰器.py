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
"""
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

@debug
def say_hello():
    print("hello!")

say_hello()

"""
这是最简单的装饰器，但是有一个问题，如果被装饰的函数需要传入参数，那么这个装饰器就坏了。
因为返回的函数并不能接受参数，你可以指定装饰器函数wrapper接受和原函数一样的参数，比如：
"""

def debug1(func):
    def wrapper(something):  # 指定一毛一样的参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func(something)
    return wrapper  # 返回包装过函数

@debug1
def say(something):
    print ("hello {}!".format(something))
say("wellqin")

"""
这样你就解决了一个问题，但又多了N个问题。因为函数有千千万，你只管你自己的函数，别人的函数参数是什么样子，鬼知道？
还好Python提供了可变参数*args和关键字参数**kwargs，有了这两个参数，装饰器就可以用于任意目标函数了。
"""

def debug2(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...',)
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug2
def say2(something):
    print ("hello {}!".format(something))

say2("wellqin2")


# 高级部分
"""
带参数的装饰器#
假设我们前文的装饰器需要完成的功能不仅仅是能在进入某个函数后打出log信息，而且还需指定log的级别，那么装饰器就会是这样的。

你可以这么理解，当带参数的装饰器被打在某个函数上时，比如@logging(level='DEBUG')，
它其实是一个函数，会马上被执行，只要这个它返回的结果是一个装饰器时，那就没问题。细细再体会一下。
"""
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print ("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say123(something):
    print ("say {}!".format(something))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do123(something):
    print ("do {}...".format(something))


say123('hello')
do123("my work")