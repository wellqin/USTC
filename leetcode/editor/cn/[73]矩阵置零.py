# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。 
# 
#  示例 1: 
# 
#  输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#  
# 
#  示例 2: 
# 
#  输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ] 
# 
#  进阶: 
# 
#  
#  一个直接的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。 
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。 
#  你能想出一个常数空间的解决方案吗？ 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def setZeroes(self, matrix):
        stack = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    stack.append([i, j])

        while stack:
            i, j = stack.pop()
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
            for k in matrix:
                k[j] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:

        flag_line = False
        flag_row = False
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                flag_row = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                flag_line = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_row:
            for i in range(m):
                matrix[i][0] = 0
        if flag_line:
            for i in range(n):
                matrix[0][i] = 0


# leetcode submit region end(Prohibit modification and deletion)
A = [
    [0, 1, 2, 0],
    [3, 4, 0, 2],
    [1, 3, 1, 5]
]
print(Solution().setZeroes1(A))
