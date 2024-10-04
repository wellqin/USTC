# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。 
# 
#  一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。 
# 
#  返回一对观光景点能取得的最高分。 
# 
#  
# 
#  示例： 
# 
#  输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 50000 
#  1 <= A[i] <= 1000 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        if not A:
            return 0

        l = 0
        r = len(A) - 1
        res = 0
        tmp = 0
        while l < r:
            if tmp < res:
                tmp = A[l] + A[r] + l - r
                res = max(res, tmp)
                r -= 1
            l += 1

        return res

    def maxScoreSightseeingPair1(self, A):
        # A[i] + A[j] + i - j
        res = 0
        pre_max = A[0] + 0  # 初始值
        for k in range(1, len(A)):
            res = max(res, pre_max + A[k] - k)  # 判断能否刷新res
            pre_max = max(pre_max, A[k] + k)  # 判断能否刷新pre_max， 得到更大的A[i] + i
        return res


# leetcode submit region end(Prohibit modification and deletion)
A = [8, 1, 5, 2, 6]
print(Solution().maxScoreSightseeingPair1(A))
