# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.IterativeProtocol
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退。迭代器有两个基本的方法：iter() 和 next()。


在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
并在下一次执行 next() 方法时从当前位置继续运行。调用一个生成器函数，返回的是一个迭代器对象。

1.1、python中的迭代协议
    什么是迭代协议?
    迭代协议：一个是 __iter__(也就是可迭代类型)，另一个是Iterator（迭代器）。

    迭代器是什么？ 迭代器是访问集合内元素的一种方式， 一般用来遍历数据。
    迭代器和以下标的访问(list[0])方式不一样， 迭代器是不能返回的, 迭代器提供了一种惰性数据的方式。

python中能完成for循环，就是借助了迭代器
实现了__iter__，就是可迭代的
再实现了__next__，就是迭代器


Iterator源码：实现了__next__和__iter__二个魔法函数
class Iterator(Iterable):  # 继承了Iterable

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):  # 重载了
        return self

    @classmethod
    def __subclasshook__(cls, C):  # 虚拟子类（virtual subclass）
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and
                any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        return NotImplemented


再看 Iterable 源码，Iterable继承抽象基类
class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    @classmethod
    def __subclasshook__(cls, C):  # 虚拟子类（virtual subclass）
        if cls is Iterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
"""

# list[item]访问的原理是__getitem__
# list中实现了__iter__，是可迭代对象。但不是迭代器

# Iterable继承的是抽象基类（metaclass=ABCMeta）（__iter__）
# Iterator(迭代器)这个是继承了Iterable，实现的魔法函数有__iter__，__next__
from collections.abc import Iterable, Iterator  # （Iterator迭代器：实现了__next__和__iter__二个魔法函数）

a = [1, 2]  # list是实现__iter__是可迭代类型，可迭代类型与迭代器（__iter__，__next__）是不一样的
print(isinstance(a, Iterable))  # True
print(isinstance(a, Iterator))  # False
print(isinstance(iter(a), Iterator))  # True  iter() 函数用来生成迭代器

"""
iter(object[, sentinel])
iter(obj)，会返现一个迭代器，如果 obj 不是可迭代对象，则会报错。
然后我们可以对获取到的迭代器不断使⽤next()函数来获取下⼀条数据。iter()函数实际上就是调⽤了可迭代对象的__iter__方法

    object -- 支持迭代的集合对象。
    sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），
                此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。  
"""
