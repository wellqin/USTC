# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  # 暴力
        if not nums:
            return 0
        N = len(nums)
        count = 0
        for i in range(N):
            for j in range(i, N):
                res = 0
                for n in range(i, j + 1):
                    res += nums[n]
                if res == k:
                    count += 1
        return count

    def subarraySum1(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        N = len(nums)
        count = 0
        for i in range(N):
            pre = 0
            for j in range(i, N):
                pre += nums[j]
                if pre == k:
                    count += 1
        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        dict = {0: 1}
        count = 0
        sum = 0
        for num in nums:
            sum += num
            if sum - k in dict:
                count += dict[sum - k]
            dict[sum] = dict.get(sum, 0) + 1

        return count


# leetcode submit region end(Prohibit modification and deletion)
nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))
print(Solution().subarraySum1(nums, k))

nums1 = [1, 2, 3, 4, 5]
k1 = 9
print(Solution().subarraySum2(nums1, k1))
