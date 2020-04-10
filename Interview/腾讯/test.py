# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/9/20
Change Activity:  2019/9/20
-------------------------------------------------
"""
# li = []
# for i in range(n):
#      li.append(list(map(int, input().split())))
c = 2
li = [9] * c
li.insert(0, 3)
print(li)

b = [str(i) for i in li]
print(b)
print(''.join(b))

