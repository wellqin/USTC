# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.DictWithAbc
Description :   
Author :          wellqin
date:             2020/4/12
Change Activity:  2020/4/12
-------------------------------------------------
1.1、dict的abc继承关系

__all__ = ["Awaitable", "Coroutine", "AsyncIterable", "AsyncIterator",
           "Hashable", "Iterable", "Iterator", "Generator",
           "Sized", "Container", "Callable",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",  **注意这二个**
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           "ByteString",
           ]

dict属于mapping类型
下面是其源码
"""
from abc import abstractmethod
from collections.abc import Mapping

"""
class Mapping(Sized, Iterable, Container):

    __slots__ = ()

    A Mapping is a generic container for associating key/value
    pairs.

    This class provides concrete generic implementations of all
    methods except for __getitem__, __iter__, and __len__.


    @abstractmethod
    def __getitem__(self, key):
        raise KeyError

    def get(self, key, default=None):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        return KeysView(self)

    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        return ItemsView(self)

    def values(self):
        "D.values() -> an object providing a view on D's values"
        return ValuesView(self)

    def __eq__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        return dict(self.items()) == dict(other.items())

Mapping.register(mappingproxy)
"""


class MutableMapping(Mapping):
    __slots__ = ()  # 在所有情况下99.9％不需要的硬核优化，更多的是用来作为一个内存优化工具

    """A MutableMapping is a generic container for associating
    key/value pairs.

    This class provides concrete generic implementations of all
    methods except for __getitem__, __setitem__, __delitem__,
    __iter__, and __len__.

    """

    @abstractmethod
    def __setitem__(self, key, value):
        raise KeyError

    @abstractmethod
    def __delitem__(self, key):
        raise KeyError

    __marker = object()

    def pop(self, key, default=__marker):
        """D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
          If key is not found, d is returned if given, otherwise KeyError is raised.
        """
        try:
            value = self[key]
        except KeyError:
            if default is self.__marker:
                raise
            return default
        else:
            del self[key]
            return value

    def popitem(self):
        """D.popitem() -> (k, v), remove and return some (key, value) pair
           as a 2-tuple; but raise KeyError if D is empty.
        """
        try:
            key = next(iter(self))
        except StopIteration:
            raise KeyError
        value = self[key]
        del self[key]
        return key, value

    def clear(self):
        """D.clear() -> None.  Remove all items from D."""
        try:
            while True:
                self.popitem()
        except KeyError:
            pass

    def update(*args, **kwds):
        """ D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
            If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
            If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
            In either case, this is followed by: for k, v in F.items(): D[k] = v
        """
        if not args:
            raise TypeError("descriptor 'update' of 'MutableMapping' object "
                            "needs an argument")
        self, *args = args
        if len(args) > 1:
            raise TypeError('update expected at most 1 arguments, got %d' %
                            len(args))
        if args:
            other = args[0]
            if isinstance(other, Mapping):
                for key in other:
                    self[key] = other[key]
            elif hasattr(other, "keys"):
                for key in other.keys():
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value
        for key, value in kwds.items():
            self[key] = value

    def setdefault(self, key, default=None):
        """D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D"""
        try:
            return self[key]
        except KeyError:
            self[key] = default
        return default


# MutableMapping.register(dict)


# dict属于mapping类型
a = {}  # 字典a不是继承MutableMapping，而是实现了MutableMapping的魔法函数
print(isinstance(a, MutableMapping))  # False
print(isinstance(a, Mapping))  # True


"""
__slots__理解：

首先了解动态语言与静态语言的不同
动态语言：可以在运行的过程中，修改代码
静态语言：编译时已经确定好代码，运行过程中不能修改
如果我们想要限制实例的属性怎么办？比如，只允许对Person实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

一旦在类中使用了_slots_，那么该类所创建的对象将会失去__dict__ , 即失去名称空间，失去名称空间就代表着不能添加除了_slots_以外的新属性了。
"""


class Person(object):
    __slots__ = ("name", "age")


P = Person()
P.name = "老王"
P.age = 20
# P.score = 100  # AttributeError: 'Person' object has no attribute 'score'


# 注意:使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
class Test(Person):
    pass


t = Test()
t.score = 100
print(t.score)  # 100
