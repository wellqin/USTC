# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/9/16
Change Activity:  2019/9/16
-------------------------------------------------
"""
str = "asdad"
b = eval("asdad")
print(b)

n = int(input())
li = map(int, input().split())

def solution(A):
    res = 1
    l = len(A)
    dp = [[1]*20001 for i in range(l)]
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            d = A[i] - A[j]
            d += 10001
            dp[i][d] = max(dp[i][d], dp[j][d]+1)
            res = max(res, dp[i][d])
            return res
print(solution(li))