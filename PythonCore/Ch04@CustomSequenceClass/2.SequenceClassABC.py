# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.SequenceClassABC
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------
1.2、python中序列类型的abc继承关系

Sequence抽象基类，里面规定了一些方法。序列要满足这些方法才可以
"""

# 容器相关的一些数据结构它的抽象基类都是放在abc中的
from abc import abstractmethod
from collections import abc, Sequence  # ctrl+鼠标左键进去可以看见，注意分析源码

"""
进到里面可以看见定义了collections相关的抽象基类，其中二个和序列相关，即Sequence和MutableSequence。
__all__ = ["Awaitable", "Coroutine", "AsyncIterable", "AsyncIterator",
           "Hashable", "Iterable", "Iterator", "Generator",
           "Sized", "Container", "Callable",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",  <---- 此处
           "ByteString",
           ]
           
Sequence就是不可变序列的方法集合的抽象基类，MutableSequence是集合了可变序列的方法和协议的抽象基类。

序列相关的是： Sequence as Sequence（不可变序列类型）,MutableSequence as MutableSequence（可变序列类型）,
from . import (
    Sequence as Sequence,        ################********************
    MutableSequence as MutableSequence,###########*******************
)
"""

"""
可变序列（MutableSequence）从不可变序列（Sequence）那里继承了一些方法.
Sequence继承了collection，collection又继承了Sized、Container、Iterable
python的内置序类型并没有直接继承这些基类，但是这些基类定义了某种特性序列的方法和协议，
了解这些基类间的继承关系能很好的帮助我们了解python的内置序列类型。
"""


# 分析MutableSequence源码，规定了许多方法
# 这就是可变序列的抽象基类
class MutableSequence(Sequence):
    __slots__ = ()

    """All the operations on a read-write sequence.

    Concrete subclasses must provide __new__ or __init__,
    __getitem__, __setitem__, __delitem__, __len__, and insert().

    """

    @abstractmethod
    def __setitem__(self, index, value):
        raise IndexError

    @abstractmethod
    def __delitem__(self, index):
        raise IndexError

    @abstractmethod
    def insert(self, index, value):
        """S.insert(index, value) -- insert value before index"""
        raise IndexError

    def append(self, value):
        """S.append(value) -- append value to the end of the sequence"""
        self.insert(len(self), value)

    def clear(self):
        """S.clear() -> None -- remove all items from S"""
        try:
            while True:
                self.pop()
        except IndexError:
            pass

    def reverse(self):
        """S.reverse() -- reverse *IN PLACE*"""
        n = len(self)
        for i in range(n // 2):
            self[i], self[n - i - 1] = self[n - i - 1], self[i]

    def extend(self, values):
        """S.extend(iterable) -- extend sequence by appending elements from the iterable"""
        for v in values:
            self.append(v)

    def pop(self, index=-1):
        """S.pop([index]) -> item -- remove and return item at index (default last).
           Raise IndexError if list is empty or index is out of range.
        """
        v = self[index]
        del self[index]
        return v

    def remove(self, value):
        """S.remove(value) -- remove first occurrence of value.
           Raise ValueError if the value is not present.
        """
        del self[self.index(value)]

    def __iadd__(self, values):
        self.extend(values)
        return self


MutableSequence.register(list)
MutableSequence.register(bytearray)  # Multiply inheriting, see ByteString
