# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例: 
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
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
        :type nums: List[int] [10, 9, 2, 5, 3, 7, 101, 18]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def lengthOfLIS1(self, nums):  # 用二分查找来搜索当前元素应放置的位置
        """
        :type nums: List[int]
        :rtype: int
        只能把点数小的牌压到点数比它大的牌上。如果当前牌点数较大没有可以放置的堆，
        则新建一个堆，把这张牌放进去。如果当前牌有多个堆可供选择，则选择最左边的堆放置

        按照上述规则执行，可以算出最长递增子序列，牌的堆数就是我们想求的最长递增子序列的长度
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
            if nums[i] < tails[0]:
                # new smallest value
                tails[0] = nums[i]
                print(tails)
            elif nums[i] > tails[length - 1]:
                # A[i] wants to extend
                # largest subsequence
                tails[length] = nums[i]
                length += 1
                print(tails)
            else:
                # A[i] wants to be current
                # end candidate of an existing
                # subsequence. It will replace
                # ceil value in tailTable
                tails[binarySearch(tails, 0, length - 1, nums[i])] = nums[i]
                print(tails)

        return length

    """
    [10, 9, 2, 5, 3, 7, 101, 18]
    
    [10, 0, 0, 0, 0, 0, 0, 0, 0]   初始化
    [9, 0, 0, 0, 0, 0, 0, 0, 0]    步骤1 ：新元素比当前小--替代
    [2, 0, 0, 0, 0, 0, 0, 0, 0]    步骤1
    [2, 5, 0, 0, 0, 0, 0, 0, 0]    步骤2 ：largest subsequence
    [2, 3, 0, 0, 0, 0, 0, 0, 0]    步骤3 ：取代
    [2, 3, 7, 0, 0, 0, 0, 0, 0]    步骤2
    [2, 3, 7, 101, 0, 0, 0, 0, 0]  步骤2
    [2, 3, 7, 18, 0, 0, 0, 0, 0]   步骤3
    """

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

    def lengthOfLISSelf(self, nums):
        # [10, 9, 2, 5, 3, 7, 101, 18]
        if not nums or len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        print(dp)  # [1, 1, 1, 2, 2, 3, 4, 4]
        return max(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS1([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLISSelf([10, 9, 2, 5, 3, 7, 101, 18]))
