# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.DictSubclass
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.3、dict的子类
不建议继承dict和list

__getitem__与__setitem__源码：
def __getitem__(self, key):
    if key in self.data:  # key存在
        return self.data[key]
    if hasattr(self.__class__, "__missing__"):  # key不存在，会去判断类中有没有__missing__，有的话调用__missing__
        return self.__class__.__missing__(self, key)
    raise KeyError(key)

def __setitem__(self, key, item): self.data[key] = item


def __missing__(self, key): # real signature unknown; restored from __doc__
    # __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
    # if self.default_factory is None: raise KeyError((key,))
    # self[key] = value = self.default_factory()
    # return value
    pass
"""

# class Mydict(dict):
#     def __setitem__(self, key, value):
#         super(Mydict, self).__setitem__(key, value * 2)
#
#
# my_dict = Mydict(one=1)
# print(my_dict)  # {'one': 1}  # 在某些情况下，用C语言写出来的python内置类型，它不会调用__setitem__方法
# my_dict["one"] = 1  # {'one': 2}，调用了__setitem__方法
# print(my_dict)

"""
在某些情况下，用C语言写出来的python内置类型，它不会调用__setitem__方法
因此我们想要继承dict的话，就去继承UserDict（例如下面）才不会出现上面状况
"""
from collections import UserDict


class Mydict1(UserDict):
    def __setitem__(self, key, value):
        super(Mydict1, self).__setitem__(key, value * 2)


my_dict = Mydict1(one=1)
print(my_dict)  # {'one': 2}
my_dict["one"] = 1  # {'one': 2}
print(my_dict)


from collections import defaultdict
# defaultdict重写了__missing__方法
# defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值

# dict =defaultdict( factory_function)
# 这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，
# 比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0
# dict1 = defaultdict(int)
# dict2 = defaultdict(set)
# dict3 = defaultdict(str)
# dict4 = defaultdict(list)
# dict1[2] ='two'
#
# print(dict1[1])  # 0
# print(dict2[1])  # set()
# print(dict3[1])  #
# print(dict4[1])  # []


my_dict = defaultdict(dict)
my_value = my_dict["lishun"]  # 按照正常情况会报错误
print(my_value)  # {}

my_dict1 = {}
my_value1 = my_dict1["lishun"]
print(my_value1)  # KeyError: 'lishun'
