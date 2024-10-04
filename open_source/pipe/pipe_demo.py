# -*- coding:utf-8 -*-
import pprint

from pipe import *

"""
https://mp.weixin.qq.com/s/FuH-yy8jIkFQvez_jFNT6w
"""

print(range(5) | add)

print(range(5) | where(lambda x: x % 2 == 0) | add)

print(sum(range(5) | where(lambda x: x % 2 == 0)))

print([1, 2, 3] | first)
print(next(iter([1, 2, 3])))


