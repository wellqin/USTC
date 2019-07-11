#! coding:utf8
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
#
# 示例: 
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
#因为 nums[0] + nums[1] = 2 + 7 = 9
#所以返回 [0, 1]
# 
#
#! coding:utf8
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j]) == target:
#                     return [i, j]
#         return [0, 0]
#
#     def twoSum2(self, nums, target):
#         dict_info = {}
#         for index, num in enumerate(nums):
#             if target - num in dict_info:  # Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
#                 return [dict_info[target - num], index]
#             else:
#                 dict_info[num] = index
#     def twoSum3(self, nums, target):
#     n = len(nums)
#     for x in range(n):
#         b = target-nums[x]
#         if b in nums:
#             y = nums.index(b)
#             if y!=x:
#                 return x,y
# nums = [2, 7, 11, 15]
# print(Solution().twoSum(nums, 9))

from collections import defaultdict


class TwoSum(object):
    def __init__(self, nums: [int], target: int):
        self.nums = nums
        self.target = target

    def scan_nums(self):
        memoize = defaultdict(list)
        for index, num in enumerate(self.nums):
            memoize[num].append(index)

        return memoize

    def _find_set(self, memoize):
        for index, num in enumerate(self.nums):
            difference = self.target - num
            if memoize[difference] and index != memoize[difference][0]:
                memoize[difference].append(index)
                return sorted(memoize[difference])

    def _sum_from_indecies(self, indecies):
        return sum([self.nums[i] for i in indecies])

    def solve(self) -> [int]:
        memoize = self.scan_nums()

        for indices in memoize.values():
            if len(indices) == 2 and self._sum_from_indecies(indices) == self.target:
                return sorted(indices)

        return self._find_set(memoize)


# -------------------------------------------------------------------------------
#    Main Leetcode Input Driver
# -------------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        return TwoSum(nums, target).solve()


# -------------------------------------------------------------------------------
#    Unit Test
# -------------------------------------------------------------------------------

import unittest


class TestSolution(unittest.TestCase): # 继承unittest.TestCase

    def test_1_2_3(self):
        nums = [1, 2]
        target = 3
        ans = [0, 1]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_1_1_2(self):
        nums = [1, 1]
        target = 2
        ans = [0, 1]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_many(self):
        nums = [1, 2, 30, 4, 5, 6, 7, 8, 9]
        target = 36
        ans = [2, 5]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_0_1_1(self):
        nums = [0, 2, 1]
        target = 1
        ans = [0, 2]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = [0, 1]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_dont_duplicate_index(self):
        nums = [3, 2, 4]
        target = 6
        ans = [1, 2]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_negative(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        ans = [2, 4]
        self.assertEqual(Solution().twoSum(nums, target), ans)

    def test_duplicate(self):
        nums = [1, 1, 2, 2, 3, 3, 7, 10]
        target = 17
        ans = [6, 7]
        self.assertEqual(Solution().twoSum(nums, target), ans)


unittest.main()  # #运行所有的测试用例