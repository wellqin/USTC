# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        缺失的正数
Description :   
Author :          wellqin
date:             2019/8/3
Change Activity:  2019/8/3
-------------------------------------------------
"""
"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

"""

class Solution1:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

    def missingNumber1(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    def missingNumber2(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missingNumber3(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum






"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i < length:
            # 将value移动到相应index的位置
            if 0 < nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                # 交换后还需重新检查
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                # 对于小于0的元素或者大于length的元素不做处理
                i += 1
        for i in range(length):
            # 查找下标index不为value值的位置
            if nums[i] != i + 1:
                return i + 1
        # 所有位置的value值和索引index相同，则为长度+1
        return length + 1

    def firstMissingPositive1(self, nums):
        num = 1
        for i in range(len(nums)):
            if num in nums:
                num += 1
        return num