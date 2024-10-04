# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例: 
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
#
# 进阶: 
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#
import sys
from typing import List


class Solution(object):
    """
    思路 1 - 时间复杂度: O(N^2)- 空间复杂度: O(1)******
    从i开始，计算i到n，存比较大的sum，会超时
    """

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = float('-inf')
        for i in range(n):
            s = 0
            for j in range(i, n):
                s = s + nums[j]
                m = max(m, s)
        return m

    """
    思路 2 - 时间复杂度: O(NlgN)- 空间复杂度: O(N)******
    参见clrs 第71页，用divide and conquer，有伪码
    最大的subarray sum有三个可能，左半段或者右半段，或者跨越左右半段,
    速度比较慢，AC代码，复杂度O(NlogN)
    """

    def maxSubArray1(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)

    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum)




    """
    思路
    3 - 时间复杂度: O(N) - 空间复杂度: O(N) ** ** **

    动态规划（只关注：当然值和当前值 + 过去的状态，是变好还是变坏，一定是回看容易理解）
    dp[i] = max(dp[i - 1] + nums[i], nums[i])
    到i处的最大值两个可能，一个是加上nums[i], 另一个从nums[i]起头，重新开始。可以AC
    """

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [nums[0] for _ in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    """
    思路 4 - 时间复杂度: O(N)- 空间复杂度: O(1)******

    Kadane’s Algorithm wikipedia可以查到,然后一般的是负的可以还回0，这里需要稍作修改，参考

    http://algorithms.tutorialhorizon.com/kadanes-algorithm-maximum-subarray-problem/

    start:
        max_so_far = a[0]
        max_ending_here = a[0]

    loop i= 1 to n
        (i) max_end_here = Max(arrA[i], max_end_here+a[i]);
        (ii) max_so_far = Max(max_so_far,max_end_here);

    return max_so_far

    """

    def maxSubArray3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, max_end = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_end = max(max_end + nums[i], nums[i])
            max_sum = max(max_sum, max_end)
        return max_sum

    def maxSubArraySelf(self, nums):
        dp = nums[0]
        res = float("-inf")
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            res = max(res, dp)
        return res

    def maxSubArraySelf1(self, nums):
        n = len(nums)
        sum = 0
        res = float("-inf")
        for i in range(n):
            sum += nums[i]
            if sum > res:
                res = sum
            if sum <= 0:
                sum = 0

        return res


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray3([2, 3, -6, 2, 4]))
print(Solution().maxSubArraySelf1([2, 3, -6, 2, 4]))
print(Solution().maxSubArraySelf([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
