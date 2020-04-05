# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1: 
#
# 
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
# 
#
# 示例 2: 
#
# 
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
# 
#
# 注意：数组长度不会超过10000。 
#

class Solution:
    def findLengthOfLCISS(self, nums):
        if not nums: return 0
        if len(set(nums)) == 1: return 1
        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max()

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(set(nums)) == 1: return 1

        dp = [1 for _ in range(len(nums))]
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = 1 + dp[i - 1]
            res = max(dp[i], res)

        return res


print(Solution().findLengthOfLCIS([1, 3, 5, 4, 7]))
