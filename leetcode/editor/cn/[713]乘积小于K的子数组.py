# 给定一个正整数数组 nums。 
# 
#  找出该数组内乘积小于 k 的连续的子数组的个数。 
# 
#  示例 1: 
# 
#  
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
#  
# 
#  说明: 
# 
#  
#  0 < nums.length <= 50000 
#  0 < nums[i] < 1000 
#  0 <= k < 10^6 
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        N = len(nums)
        count = 0
        for i in range(N):
            res = 1
            for j in range(i, N):
                res *= nums[j]
                if res < k:
                    count += 1
                if res >= k:
                    break
        return count


    def numSubarrayProductLessThanK1(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        l, r = 0, 0
        tmp, res = 1, 0
        while r < len(nums):
            tmp *= nums[r]
            while tmp >= k and l < len(nums):
                tmp /= nums[l]
                l += 1
            if r >= l: res += (r - l + 1)
            r += 1
        return res



# leetcode submit region end(Prohibit modification and deletion)
nums = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))
print(Solution().numSubarrayProductLessThanK1(nums, k))
