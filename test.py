# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/31
Change Activity:  2019/7/31
-------------------------------------------------
"""
import math
from functools import reduce

print(list(map(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2), ([0, 2], [3, 4]))))  # [2.0, 5.0]
print(*map(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2), ([0, 2], [3, 4])))  # 2.0 5.0

print(reduce(lambda x, y: x + y, list(range(101))))  # 5050

from collections import Counter, defaultdict

texts = ['apple bear peach grape', 'grape orange pear']



from collections import Counter

texts = ['apple bear peach grape', 'grape orange pear']


def mp(text):
    words = text.split(' ')
    return Counter(words)

print(reduce(lambda x, y: x + y, map(mp, texts)))
# Counter({'grape': 2, 'pear': 1, 'peach': 1, 'bear': 1, 'orange': 1, 'apple': 1})
