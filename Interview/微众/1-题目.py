# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1-题目
Description :   
Author :          wellqin
date:             2019/9/19
Change Activity:  2019/9/19
-------------------------------------------------
"""
# 求询问次数
# 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
def func(n):
    if not n:
        return
    count = 0
    for x in range(2**n):
        for t in range(2**n):
            if t & x == t:
                count += 1
                print(x, t)
    print(count)


func(3)

# print("===========================")
# for i in range(2**3):
#     if i % 1000003 == 6:
#         print(i)  # 6
# n = 3
# print(((2**n)-2) % 1000003)

COUNT = 0
def perm(n, begin, end):
    global COUNT
    if begin >= end:
        print(n)
        COUNT += 1
    else:
        i = begin
        for num in range(begin, end):
            n[num], n[i] = n[i], n[num]
            perm(n, begin + 1, end)
            n[num], n[i] = n[i], n[num]


n = [1, 2, 3, 4]
perm(n, 0, len(n))
print(COUNT)


