# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        卡中心
Description :   
Author :          wellqin
date:             2019/9/15
Change Activity:  2019/9/15
-------------------------------------------------
"""
# n = int(input())
# a = list(map(int, input().split()))  # 各个城市怪物个数列表
# b = list(map(int, input().split()))   # 怪物之和
#
# print(n)
# print(a)
# print(b)

n = 2
a = [3, 5, 2]
b = [4, 5]

# n = 2
# a = [1, 2, 2]
# b = [4, 1]


# def total_num(n, a, b):
#     if n == 0:
#         return a[0]
#     res = []
#     ans = []
#     for k in range(n+1):
#         if k == 0:
#             res.append(a[0])
#         else:
#             res.append(a[k-1] + a[k])
#     res.pop(0)
#     print(res)
#     for i in range(len(b)):
#         flag = False
#         if int(res[i]) > int(b[i]):
#             flag = True
#             if flag is True:
#                 ans.append(int(b[i]))
#         else:
#             ans.append(int(b[i]))
#     return sum(ans)
#
#
# print(total_num(n, a, b))

def fun(n, a, b):
    dp = [0]*n
    for i in range(n):
        dp[i] = min(a[i]+a[i+1], b[i])
        if a[i] < b[i]:
            a[i+1] -= min(a[i+1]+a[i]-b[i], 0)
    print(sum(dp))

fun(n,a,b)

























































# b = [2020, 2040]
#
# res = 2019
# if not b:
#     print(0)
#
# for i in range(b[0], b[1]):
#     for j in range(b[0]+1, b[1]):
#         ans = (i * (i+1)) % 2019
#         res = min(res, ans)
# print(res)

