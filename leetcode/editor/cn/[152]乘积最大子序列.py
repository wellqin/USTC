# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。 
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxdp = [1] * (n + 1)
        mindp = [1] * (n + 1)
        ans = float('-inf')

        for i in range(1, n + 1):
            maxdp[i] = max(maxdp[i - 1] * nums[i - 1],
                           mindp[i - 1] * nums[i - 1], nums[i - 1])
            mindp[i] = min(maxdp[i - 1] * nums[i - 1],
                           mindp[i - 1] * nums[i - 1], nums[i - 1])
            ans = max(ans, maxdp[i])
        return ans

    def maxProduct1(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1  # 当or左边的值为0的时候会传递右边的值
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


# leetcode submit region end(Prohibit modification and deletion)
nums = [2, -1, 3, -2, 4, -1]
nums1 = [2, -1, 1, 1]
print(Solution().maxProduct(nums))
print(Solution().maxProduct1(nums))
