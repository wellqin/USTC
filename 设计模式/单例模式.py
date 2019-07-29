# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        单例模式
Description :   
Author :          wellqin
date:             2019/7/28
Change Activity:  2019/7/28
-------------------------------------------------
"""
"""
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。

当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。
如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，
这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。
事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

在 Python 中，我们可以用多种方法来实现单例模式
"""

# 1.使用模块
"""
其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，
而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。


# class Singleton(object):
#     def foo(self):
#         pass
# singleton = Singleton()

将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
from a import singleton

"""
from 设计模式.mysingleton import singleton
singleton.foo()


# 2.使用装饰器

"""
将类A传入单例修饰器中，如果该类还未生成实例(instances中不存在该类)，那么就生成一个新的实例返回，并记录在instances中。
如果已经instances中已经存在该类，那么直接返回实例instances[cls]。

可变参数 (Variable Argument) 的方法：
使用*args和**kwargs语法。其中，*args是可变的positional arguments列表，
**kwargs是可变的keyword arguments列表。并且，*args必须位于**kwargs之前.

def test_kwargs(first, *args, **kwargs):
   print 'Required argument: ', first
   for v in args:
      print 'Optional argument (*args): ', v
   for k, v in kwargs.items():
      print 'Optional argument %s (*kwargs): %s' % (k, v)
test_kwargs(1, 2, 3, 4, k1=5, k2=6)

# results:
# Required argument:  1
# Optional argument (*args):  2
# Optional argument (*args):  3
# Optional argument (*args):  4
# Optional argument k2 (*kwargs): 6
# Optional argument k1 (*kwargs): 5
"""

def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton



@Singleton
class A(object):

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(a1 == a2) # True












