# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        硬币找零
Description :   
Author :          wellqin
date:             2019/7/20
Change Activity:  2019/7/20
-------------------------------------------------
"""

"""
题目描述：给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，
返回 -1。（你可以认为每种硬币的数量是无限的。）

解法：动态规划
对于一个金额，与它的差值为硬币库（coins）中硬币面值的数都是它一步就可以到达的，
这里一步到达是指只需要一个硬币就能解决。因此，对于一个金额，能够满足题目要求的硬币数为所有能够
一步到达这个它的金额所需的硬币数加1。
"""
class Solution:
    def coinChange(self, coins, amount):
        dp = [float("inf") for i in range(amount+1)] # 初始化dp数组
        dp[0] = 0                                    # 当amount=0时，硬币所需数为0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]
coins = [1, 2, 5]
amount = 10
print(Solution().coinChange(coins, amount))



"""
题目描述：给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成[1, amount]中所有面值所需的
最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。（你可以认为每种硬币的数量是无限的。

这种情况比上面情况稍微复杂一点，因为要组成所有范围内的面值。
"""
from turtle import *
class Solution1:
    def coinChange(self, coins, amount):
        dp = [float("inf") for i in range(amount+1)] #  初始化dp数组
        dp[0] = 0                                    #  当amount=0时，硬币所需数为0
        if 1 not in coins:                           #  如果硬币里面没有面值为1的硬币，则无法组成所有的硬币
            return -1
        dp[1] = 1
        for i in range(2, amount+1):
            min_ = dp[i]
            for j in range(1, i):
                if j in coins and j <= i - j + 1:        # 如果另一部分直接可以用一个硬币代替
                    min_ = min(min_, dp[i-j] + 1)
                else:
                    min_ = min(min_, dp[i-j] + dp[j])
            dp[i] = min_
        return dp[-1]
print(Solution1().coinChange(coins, amount))












