# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
#
# 
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。 
#
# 说明：m 和 n 的值均不超过 100。 
#
# 示例 1: 
#
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
#
from typing import List

# obstacleGrid = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]
obstacleGrid = [[0, 0],
                [1, 1],
                [0, 0]]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] != 0:
            return 0
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):  # 行
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                break                         # 如果遇到障碍物，说明此路不通，后面的也没必要看了

        for j in range(1, len(obstacleGrid[0])):  # 列
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
                break
        print(dp)

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        """
        [[1, 1, 1], 
         [1, 0, 0], 
         [1, 0, 0]]

        """
        return dp[-1][-1]


    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        if obstacleGrid[0][0] == 1:   # 堵住出口了
            return 0

        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break  # 如果遇到障碍物，说明此路不通，后面的也没必要看了
            dp[i][0] = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        print(dp)

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


ss = Solution()
print(ss.uniquePathsWithObstacles(obstacleGrid))
print(ss.uniquePathsWithObstacles1(obstacleGrid))
