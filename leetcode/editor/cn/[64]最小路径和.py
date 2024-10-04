# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。 
#
# 示例: 
#
# 输入:
# [
#   [1,3,1],
#  [1,5,1],
#  [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
#
from typing import List


class Solution(object):
    def minPathSum(self, grid):
        # 此数组用于记忆化搜索
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # 在起点的时候
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]

                # 在左边缘的时候
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]

                # 在上边缘的时候
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]

                # 普遍情况下
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        print(dp)
        return dp[len(grid) - 1][len(grid[0]) - 1]


grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
        ]
ss = Solution()
print(ss.minPathSum(grid))

dp = [[1, 4, 5],
      [2, 7, 6],
      [6, 8, 7]]


class Solution1:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue  # 在起点的时候
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
