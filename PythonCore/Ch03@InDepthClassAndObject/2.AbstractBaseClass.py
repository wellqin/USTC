# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        AbstractBaseClass
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------
1.2、抽象基类(abc)：abc模块，一般设计框架时很少使用
    python里边的抽象基类，是不能够实例化的。相当于Java中的接口
    python是动态语言，动态语言是没有变量的类型的。
    在python中变量只是一个符号而已，这个符号可以指向任何类型的对象。
    动态语言缺少编译时检查错误的环境，在python中编写代码是很难发现错误的，只有要运行解释器才能找到错误。
    这也是动态语言共有的一个缺陷--无法做类型检查。python信奉的是鸭子类型，鸭子类型贯穿于整个面向对象之中。

    抽象基类是什么意思？
    @在这个基础的类当中，设定好一些方法，然后所有的继承这个基类的类，都必须覆盖这个抽象基类里面的方法。
    @抽象基类是无法实例化的。

    注意：python实现不是靠继承，而是靠鸭子类型和魔法函数贯穿设计理念，完成实现某种类型的对象
         想要实现某种功能主要靠魔法函数，这时一种协议

    Why abc ?
    1. 判定某个对象的类型
    2. 利用抽象基类实现接口的 强制规定某些子类必须实现某些方法
"""

"""
在python当中已经实现了一些通用的抽象基类，放在 from collections.abc import *

抽象基类不是用来继承的，只是利用抽象基类来理解继承之间的关系，以及接口的定义，
我们去使用的时候一定要用我们的鸭子类型，如果一定要用接口的话，推荐使用mixin多继承的方式去实现它。
抽象基类使用的时候设计过度，反而不容易理解它。
"""


# 关于第一个原因，首先看两种场景
# 1. 去检查某个类是否有某种方法：hasattr可判断对象是否具有某种属性 -- 没有抽象基类时的做法
class Students(object):
    def __init__(self, student_list):
        self.student = student_list

    def __len__(self):
        return len(self.student)


students = Students(["lisha", "test", "python"])
print(hasattr(students, "__len__"))  # True
print(hasattr(students, "__getitem__"))  # False
print(hasattr(students, "__popitem__"))  # False

# 2. 判定某个对象的类型  -- 有抽象基类时的做法 Better
from collections.abc import Sized

print(isinstance(students, Sized))  # True


# 解析Sized源码：内部实现了__subclasshook__来判断有没有__len__属性
# 此外实现判定某个对象的类型功能，少不了isinstance，下一节详述


# 关于第二个原因
# 利用抽象基类实现接口的 强制规定
# 强制某些子类必须实现某些方法
# 实现了一个web框架，集成cache（redis，cache，memorychache）
# 需要设计一个抽象基类，指定子类必须实现某些方法
# 如何去模拟一个抽象基类呢？

# 首先看没有抽象基类的情况
class CacheBase:
    def get(self, key):
        raise NotImplementedError  # 子类没有实现父类要求一定要实现的接口

    def set(self, key, value):
        raise NotImplementedError


# 用户在实现这个抽象基类的子类时候，必须实现这里面的两个方法
# 在面向对象编程中，父类中可以预留一个接口不实现，要求在子类中实现。如果一定要子类中实现该方法，可以使用raise NotImplementedError报错。
# NotImplementedError具体实现方式：
# 如果子类没有实现父类中指定要实现的方法，则会自动调用父类中的方法，而父类方法又是raise将错误抛出。这样代码编写者就能发现是缺少了对指定接口的实现。
class RedisCache(CacheBase):
    pass


redis = RedisCache()  # 初始化没有抛出异常，这时不好的
# redis.get("key")  # 抛出异常raise NotImplementedError NotImplementedError


# 但这样做不好，我们需要刚初始化的时候就抛出异常，接下来就换成abc实现个人基类
# 再看看有抽象基类的情况
import abc


class Cache1Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 注意标记抽象基类方法
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache1(Cache1Base):
    pass


class RedisCache2(Cache1Base):
    def set(self, key, value):
        pass

    def get(self, key):
        pass


# 利用抽象基类直接初始化抛出异常
# redis_cache1 = RedisCache1()  # TypeError: Can't instantiate abstract class RedisCache1 with abstract methods get, set

redis_cache2 = RedisCache2()
redis_cache2.set("K", "V")  # 子类实现了就没问题了
