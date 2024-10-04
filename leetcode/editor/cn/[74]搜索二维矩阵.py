# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchMatrix1(self, matrix, target):
        if not matrix:
            return False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix2(self, matrix, target):
        # 对每一行进行二分
        if len(matrix) == 0 or len(matrix[0]) == 0 or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) - 1
            while l <= r:
                mid = l + ((r - l) >> 1)
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                elif matrix[i][mid] > target:
                    r = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len((matrix[0]))
        # 从左下角开始遍历，判断target在哪一行
        while matrix[m - 1][0] > target and m > 1:
            m -= 1
        return target in matrix[m - 1]
        # 因为m为len(matrix)，最后定位的行为从1开始的，要以0下标开始则为[m - 1]

    # 二次二分
    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        # 矩阵为空则直接返回
        if not matrix or not matrix[0]:
            return False
        R = len(matrix)
        C = len(matrix[0])

        # 如果 target不在矩阵(最小值, 最大值)范围内，直接返回
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False
        r, c = -1, -1

        left, right = 0, R - 1
        while left <= right:
            # 取左中位数
            mid = (left + right) >> 1
            # 如果该行最小值大于 target，那么target不可能在较大的另一半区间内，可能在较小的另一半区间内
            if matrix[mid][0] > target:
                right = mid - 1
            # 如果该行最大值小于 target，那么target不可能在较小的另一半区间内，可能在较大的另一半区间内
            elif matrix[mid][-1] < target:
                left = mid + 1
            # 否则，target可能在当前行内
            else:
                # print(f'{matrix[mid][0]} <= {target} <= {matrix[mid][-1]}')
                r = mid
                break

        left, right = 0, C - 1
        while left < right:
            # 取右中位数
            mid = (left + right) + 1 >> 1
            # 如果右中值大于target，那么target一定不在右半区间
            if matrix[r][mid] > target:
                right = mid - 1
            else:
                left = mid
        c = left
        # 对最终结果值进行判断
        return matrix[r][c] == target




# leetcode submit region end(Prohibit modification and deletion)
nums = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
t = 11
print(Solution().searchMatrix3(nums, t))
