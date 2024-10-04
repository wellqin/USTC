# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组

# [
#  [1],
#  [1,1],
#  [1,2,1],
#  [1,3,3,1],
#  [1,4,6,4,1]
# ]


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # nums = [[] for _ in range(numRows)]
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]

        nums = [[1], [1, 1]]
        for i in range(2, numRows):
            s = [1] * (i + 1)
            for j in range(1, len(nums[i - 1])):
                s[j] = nums[i - 1][j - 1] + nums[i - 1][j]
            nums.append(s)
        return nums

    def generate1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result, pre = [], []
        for i in range(numRows):
            now = [1] * (i + 1)
            if i >= 2:
                for n in range(1, i):
                    now[n] = pre[n - 1] + pre[n]
            result += [now]
            pre = now
        return result

    def generate2(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = self.generate2(numRows - 1)
        res.append([1] + [res[-1][i - 1] + res[-1][i] for i in range(1, numRows - 1)] + [1])
        return res


# leetcode submit region end(Prohibit modification and deletion)

numRows = 5
print(Solution().generate(numRows))
