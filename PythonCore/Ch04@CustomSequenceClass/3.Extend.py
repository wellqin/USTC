# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.Extend
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------

1.3、list中extend方法区别
序列的+、+=和extend的区别：

+ : 产生一个新的list,加号的两边必须同一类型才能相加
+=: 原地加,加号的两边不是同一类型也能相加，可以为任意（序列类型）序列的特性就是可以利用for循环进行遍历，即可迭代


源码分析：+=本质调用extend
def __iadd__(self, values):
    self.extend(values)
    return self

def extend(self, values):
    # S.extend(iterable) -- extend sequence by appending elements from the iterable
    for v in values:
        self.append(v)

def append(self, value):
    # S.append(value) -- append value to the end of the sequence
    self.insert(len(self), value)


extend是传入可迭代的对象，没有返回值。内部源码中，extend会在内部做for循环，加入元素
append是将传入的参数当成一个值，内部不会for循环，直接当成整体插入到尾部。
"""

# +
a = [1, 2]  # 加号的两边必须同一类型才能相加
b = a + [3, 4]
print(b)  # [1, 2, 3, 4]


# +=
a += [5, 6]  # += 可以相加（序列类型）
print(a)  # [1, 2, 5, 6]
a += (7, 8)  #
print(a)  # [1, 2, 5, 6, 7, 8]


a.extend(range(3))  # iterable  extend是传入可迭代的对象
print(a)  # [1, 2, 5, 6, 7, 8, 0, 1, 2]
a.append([1, 2])  # append是将传入的参数当成一个值
print(a)  # [1, 2, 5, 6, 7, 8, 0, 1, 2, [1, 2]]
