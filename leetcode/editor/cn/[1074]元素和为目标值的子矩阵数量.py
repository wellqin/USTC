# 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。 
# 
#  子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。 
# 
# 
#  如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵
# 也不同。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# 输出：4
# 解释：四个只含 0 的 1x1 子矩阵。
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,-1],[-1,1]], target = 0
# 输出：5
# 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= matrix.length <= 300 
#  1 <= matrix[0].length <= 300 
#  -1000 <= matrix[i] <= 1000 
#  -10^8 <= target <= 10^8 
#  
#  Related Topics 数组 动态规划 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


def numSubmatrixSumTarget(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    res = []
    for i in range(0, row):
        for j in range(0, col):
            for p in range(i, row):
                for q in range(j, col):
                    total = 0
                    # 就算从i,j到p,q矩阵数值和
                    for x in range(i, p + 1):
                        for y in range(j, q + 1):
                            total = matrix[x][y] + total
                    res.append(total)

    return res.count(target)


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for x in range(1, m):
            for y in range(n):
                matrix[x][y] += matrix[x - 1][y]
        for up in range(m):
            for down in range(up, m):
                hashmap = collections.defaultdict(int)
                hashmap[0] = 1
                cur = 0
                for y in range(n):
                    if up > 0:
                        cur += matrix[down][y] - matrix[up - 1][y]
                    else:
                        cur += matrix[down][y]
                    ans += hashmap[cur - target]
                    hashmap[cur] += 1
        return ans

    def numSubmatrixSumTarget1(self, matrix: List[List[int]], target: int) -> int:
        sum = [[0 for _ in range(len(matrix) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            t = 0
            for j in range(len(matrix[i])):
                t += matrix[i][j]
                sum[i + 1][j + 1] = t + sum[i][j + 1]
        print(sum)


# leetcode submit region end(Prohibit modification and deletion)
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
target = 3
print(Solution().numSubmatrixSumTarget1(grid, target))

hello = [[0, 0, 0, 0],
         [0, 1, 3, 6],
         [0, 5, 12, 21],
         [0, 12, 27, 45]
         ]
