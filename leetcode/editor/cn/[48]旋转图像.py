# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。 
#
# 说明： 
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。 
#
# 示例 1: 
#
# 给定 matrix = 
# [
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]
# 
#
# 示例 2: 
#
# 给定 matrix =
# [
#  [ 5, 1, 9,11],
#  [ 2, 4, 8,10],
#  [13, 3, 6, 7],
#  [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#  [15,13, 2, 5],
#  [14, 3, 4, 1],
#  [12, 6, 8, 9],
#  [16, 7,10,11]
# ]
# 
#
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res = []
        matrix = list(map(list, zip(*matrix)))
        for i in matrix:
            res.append(list(reversed(i)))  # reversed 函数返回一个反转的迭代器
        return res

    # 五行代码原地实现原地旋转：转置和水平翻转两个步骤
    def rotate1(self, matrix) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
        print(matrix)

    # 先上下替换，然后再主对角线镜像对称替换翻转
    def rotate2(self, matrix: List[List[int]]) -> None:
        ml = len(matrix)
        # # 替换行
        # start = 0
        # end = ml - 1
        # while start < end:
        #     matrix[start], matrix[end] = matrix[end], matrix[start]
        #     start += 1
        #     end -= 1



        # 依次替换单个坐标
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


        print(matrix)

    # 图像旋转本质就是这4个数的相互交换
    def rotate3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):  # 求出层数
            for j in range(i, n - i - 1):  # # 需旋转的次数
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] = \
                    matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
        # print(matrix)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().rotate1(matrix))
