# 给出两个图像 A 和 B ，A 和 B 为大小相同的二维正方形矩阵。（并且为二进制矩阵，只包含0和1）。 
# 
#  我们转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的重叠是指两个图像都具有 1 的位置的数目。 
# 
#  （请注意，转换不包括向任何方向旋转。） 
# 
#  最大可能的重叠是什么？ 
# 
#  示例 1: 
# 
#  输入：A = [[1,1,0],
#           [0,1,0],
#           [0,1,0]]
#      B = [[0,0,0],
#           [0,1,1],
#           [0,0,1]]
# 输出：3
# 解释: 将 A 向右移动一个单位，然后向下移动一个单位。 
# 
#  注意: 
# 
#  
#  1 <= A.length = A[0].length = B.length = B[0].length <= 30 
#  0 <= A[i][j], B[i][j] <= 1 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        将A数组与B数组中1出现的位置坐标分别存储在A_num,B_num中，
        然后遍历A_num,B_num中的位置坐标两两作差当作字典ser的键，最终键值最大的数即为所求。
        """
        n = len(A)
        A_num = set()
        B_num = set()
        ser = {}
        res = 0
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    A_num.add((i, j))
                if B[i][j] == 1:
                    B_num.add((i, j))
        for i in A_num:
            for j in B_num:
                tmp = (i[0] - j[0], i[1] - j[1])
                ser[tmp] = ser.get(tmp, 0) + 1
        if list(ser.values()):
            res = max(list(ser.values()))
        return res


# leetcode submit region end(Prohibit modification and deletion)
A = [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 0]]
B = [[0, 0, 0],
     [0, 1, 1],
     [0, 0, 1]]
print(Solution().largestOverlap(A, B))
