# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划


"""
时间复杂度：O(n)
空间复杂度：O(n)
"""


def climbStairs_best(n: int) -> int:
    dp = [0] * (n + 1)  # 1. 初试化dp=[0,...,0]，长度为n+1
    if n < 2:
        return dp[n]  # 2. 若n<2，返回1
    dp[1] = 1
    dp[2] = 2  # 3. 初始化dp[1]=1,dp[2]=2
    for i in range(3, n + 1):  # 4. 遍历，遍历区间[3,n+1)
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


    def climbStairs1(self, n: int) -> int:
        i = 1    # 爬到1台阶仅有1种方法
        j = 2    # 爬到2台阶有2种方法
        for _ in range(3, n+1):         # 自底向上递推 F(n)=F(n-1)+F(n-2)
            i, j = j, i + j                    # 每次仅保留前两个值，依次往后推算
        return j if n > 2 else n  # 注意当n=1,n=2时的情况



sss = Solution()
print(sss.climbStairs(4))
print(sss.climbStairs1(4))
