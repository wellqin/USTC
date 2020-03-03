# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/12
Change Activity:  2019/7/12
-------------------------------------------------
"""

import collections

str1 = ['a', 'b', 'c', 'd', 'a', 'a', 'b', 'c']
m = collections.Counter(str1)
print(m)

# li = [1, 2, 3, 4, 5]
#
# for i in range(len(li)):
#     print(i, li[i])
#     for j in range(i+1, len(li)):
#         print(j, li[i])
#         # if li[i] + li[j] == 6:
#         #     print(li[i], li[j])


li = [1, 2, 3, 4, 5]
target = 6
lookup = {}  # 字典
for index, i in enumerate(li):  # index代表下标，i代表当前下标对应的值
    j = target - i              # 计算差值
    if j in lookup:             # 如果差值在列表中，就找到了
        print([lookup[j], index])
    lookup[i] = index           # 把列表元素加进字典

