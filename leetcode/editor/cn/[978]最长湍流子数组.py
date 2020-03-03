# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组： 
# 
#  
#  若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]； 
#  或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。 
#  
# 
#  也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。 
# 
#  返回 A 的最大湍流子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#  
# 
#  示例 2： 
# 
#  输入：[4,8,12,16]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：[100]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 40000 
#  0 <= A[i] <= 10^9 
#  
#  Related Topics 数组 动态规划 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
import operator
from typing import List


# cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块,但只能一个个判断
class Solution(object):
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        left = 0
        right = 1
        while right < N:
            # for right in range(1, N):
            c = self.cmp(A[right - 1], A[right])
            if right == N - 1 or c * self.cmp(A[right], A[right + 1]) != -1:  # 不满足交替出现时，更新窗口
                if c != 0:
                    ans = max(ans, right - left + 1)
                left = right
            right += 1
        return ans

    def cmp(self, a, b):
        a, b = int(a), int(b)
        if a > b:
            return 1
        return 0 if a == b else -1


# leetcode submit region end(Prohibit modification and deletion)
nums = [9, 4, 2, 10, 7, 8, 8, 1, 9]
nums1 = [1, 2, 1, 2, 3, 1, 2, 1, 1]
nums2 = [2, 3, 1, 2, 2]
print(Solution().maxTurbulenceSize(nums2))
