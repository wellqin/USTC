# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1: 
#
# 输入:
# [
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
#
# 示例 2: 
#
# 输入:
# [
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]

            """
            zip(*matrix) 将matrix[[4, 5, 6],[7, 8, 9]]进行解包为[(4,7), (5,8), (6,9)]
            map(list, zip(*matrix)) 将解包内容的元祖转换成列表[[4,7], [5,8], [6,9]]
            此时还是一个map对象，需要list()函数变成数组
            最后[::-1]进行逆序，为 [[6, 9], [5, 8], [4, 7]]
            完成了二维数组的逆序转置
            """
            # matrix = [*zip(*matrix)][::-1]
            print(matrix)

        return res

    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []

        while up <= down and left <= right:
            # 从左到右
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down: break

            # 从上到下
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right: break

            # 从右到左
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1

            # 从下到上
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


# leetcode submit region end(Prohibit modification and deletion)
nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().spiralOrder1(nums))
