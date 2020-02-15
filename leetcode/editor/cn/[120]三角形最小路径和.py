# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形： 
#
# [
#     [2],
#    [3,4],
#   [6,5,7],
#  [4,1,8,3]
# ]
# 
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
#
# 说明： 
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#
from typing import List
import functools

triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]


# class Solution:
#     def minimumTotal(self, triangle):
#         for i in range(len(triangle) - 1, 0, -1):
#             for j in range(i):
#                 triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
#         return triangle[0][0]
class Solution(object):
    def __init__(self):
        self.res = 0

    def minimumTotal(self, triangle):  # 递归
        bottom = len(triangle) - 1
        width = len(triangle[-1])

        def recursion(i, j, total):
            total += triangle[i][j]
            if i == bottom:
                return total
            else:
                left = recursion(i + 1, j, total)
                right = recursion(i + 1, j + 1, total)
                return min(left, right)

        return recursion(0, 0, 0)

    def minimumTotal1(self, triangle: List[List[int]]) -> int:  # DFS,遍历所有从上到下的路径
        self.res = float("inf")
        row = len(triangle)

        # 遍历所有路径,所以会超时,所以我们采用带记忆的DFS(动态规划的自顶向下)
        @functools.lru_cache(None)
        def helper(level, i, j, tmp):
            if level == row:
                self.res = min(self.res, tmp)
                return
            if 0 <= i < len(triangle[level]):
                helper(level + 1, i, i + 1, tmp + triangle[level][i])
            if 0 <= j < len(triangle[level]):
                helper(level + 1, j, j + 1, tmp + triangle[level][j])

        # 层level, 访问下一层两个节点位置i,j , 目前总和tmp
        helper(0, -1, 0, 0)
        return self.res

    # 自底向上动态规划,用O(n^2)空间
    """
    dp[i][j] 表示到从上到下走到i,j位置最小路径的值.
    动态方程: dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + triangle[i][j]
    当然对于第一个和最后一个要单独考虑.
    """

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        # 建dp空间
        dp = [[0] * n for i in range(n)]
        dp[0][0] = triangle[0][0]
        # dp = triangle  # 这边的初始化真的是牛逼，不仅不需要把把上面两行特殊的情况考虑进去，而且为下面也做了铺垫。
        # n = len(dp)

        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        print(dp)
        return min(dp[-1])

    # 其实我们dp时候每次只用到上一层数据,如果我们倒着,从底向上可以优化成O(n)空间的
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = [0] * row
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        # print(dp) [4, 1, 8, 3]
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

    # 原地修改
    def minimumTotal4(self, triangle):
        if not triangle:
            return 0
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


ss = Solution()
print(ss.minimumTotal(triangle))
print(ss.minimumTotal1(triangle))
print(ss.minimumTotal2(triangle))
print(ss.minimumTotal3(triangle))
print(ss.minimumTotal4(triangle))
