#给定一个无序的整数数组，找到其中最长上升子序列的长度。 
#
# 示例: 
#
# 输入: [10,9,2,5,3,7,101,18]
#输出: 4 
#解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
#
# 说明: 
#
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
# 你算法的时间复杂度应该为 O(n2) 。 
# 
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#
import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarySearch(nums, l, r, target):
            while l <= r:
                mid = l + ((r - l) >> 1)
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        if not nums or len(nums) == 0:
            return 0

        tails = [0 for i in range(len(nums) + 1)]
        tails[0] = nums[0]
        # always points empty slot
        length = 1
        for i in range(1, len(nums)):
            if (nums[i] < tails[0]):
                # new smallest value
                tails[0] = nums[i]
            elif (nums[i] > tails[length - 1]):
                # A[i] wants to extend
                # largest subsequence
                tails[length] = nums[i]
                length += 1
            else:
                # A[i] wants to be current
                # end candidate of an existing
                # subsequence. It will replace
                # ceil value in tailTable
                tails[binarySearch(tails, 0, length - 1, nums[i])] = nums[i]

        return length

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        lis = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                # 要用bisect_left，因为如果插入到右边就相当于多append了一个，而不再是replace了
                lis[bisect.bisect_left(lis, nums[i])] = nums[i]

        return len(lis)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS1([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS2([10,9,2,5,3,7,101,18]))