# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/17
Change Activity:  2019/7/17
-------------------------------------------------
"""
nums = [1,2,3,4,5,6]
for i in range(len(nums)-1, -1, -1):
    print(
        i
    )
# for i in reversed(nums):
#     print(i)

for i in range(1, 10):
    for j in range(i, 10):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print("")

