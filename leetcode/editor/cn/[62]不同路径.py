# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
#
# 问总共有多少条不同的路径？ 
#
# 
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？ 
#
# 说明：m 和 n 的值均不超过 100。 
#
# 示例 1: 
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
#
# 示例 2: 
#
# 输入: m = 7, n = 3
# 输出: 28
#


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        print(dp)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[-1][-1]

    # 优化1：空间复杂度O(2n)
    def uniquePaths1(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    # 优化2：空间复杂度O(n)
    def uniquePaths2(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


m = 7
n = 3
ss = Solution()
print(ss.uniquePaths(m, n))
print(ss.uniquePaths1(m, n))
print(ss.uniquePaths2(m, n))
