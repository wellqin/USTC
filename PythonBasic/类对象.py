# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        类对象
Description :   
Author :          wellqin
date:             2020/2/9
Change Activity:  2020/2/9
-------------------------------------------------
"""


def maxProfit():
    nums = [5, 1, 8, 4, 6, 3, 2, 4]
    prevs = [0, 0, 0, 1, 0, 2, 3, 5]

    dp = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        dp[i] = max(dp[i - 1], nums[i - 1] + dp[prevs[i - 1]])
        print(dp)
    return dp[-1]


max_profit = maxProfit()
print(max_profit)
