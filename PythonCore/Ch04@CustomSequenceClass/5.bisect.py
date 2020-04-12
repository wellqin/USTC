# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        5.bisect
Description :   
Author :          wellqin
date:             2020/4/12
Change Activity:  2020/4/12
-------------------------------------------------

1.5、bisect维护已排序序列

bisect / bisect_left / bisect_right 返回该元素插入的index （只用于查找 index， 不进行实际的插入）
bisect.bisect和bisect.bisect_right返回该元素插入有序队列的index，遇到重复的往右边插入
bisect.bisect_left返回返回该元素插入有序队列的index，遇到重复的往左边插入

insort / insort_left / insort_right 把这个元素插入到序列里（实际插入）
bisect.insort和bisect.insort_right表示将该元素插入有序队列，遇到重复的往右边插入
bisect.insort_left表示将该元素插入有序队列，遇到重复的往左边插入
"""

# 在开发中，插入的数据进行排序（序列类型），直接可以利用bisect.insort(inter_list,1)进行插入
import bisect
from collections import deque

# 用来处理已排序的序列，用来维持已排序的序列， 升序
# 二分查找（效率高）
inter_list = deque()  # 序列类型都可以
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

print(inter_list)  # deque([1, 2, 3, 5, 6])
# 查找我们插入的数据（3）将要插入序列的位置是什么
print(bisect.bisect(inter_list, 3))  # 3
print(bisect.bisect_right(inter_list, 3))  # 3
# 某些一样的值我们人为排序更精确例如：90-100：A，80-90：B这样我们可以将成绩按照升序排序
print(bisect.bisect_left(inter_list, 3))  # 2
# 学习成绩
print(inter_list)  # deque([1, 2, 3, 5, 6])


"""Bisection algorithms.源码分析"""


def insort_right(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.
    If x is already in a, insert it to the right of the rightmost x.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    将x插入列表a，并假设对a进行排序，使其保持排序。
    如果x已经在a中，则将其插入最右边x的右侧。
    可选的参数 lo（默认为0）和hi（默认为len（a））绑定了要搜索的slice
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    a.insert(lo, x)


insort = insort_right  # backward compatibility  向后兼容


def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


bisect = bisect_right  # backward compatibility


def insort_left(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the left of the leftmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    a.insert(lo, x)


def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Overwrite above definitions with a fast C implementation
try:
    from _bisect import *
except ImportError:
    pass
