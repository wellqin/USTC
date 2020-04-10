# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        binary_search
Description :   
Author :          wellqin
date:             2019/8/28
Change Activity:  2019/8/28
-------------------------------------------------
"""
"""
#给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 你可以假设 nums 中的所有元素是不重复的。
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 确定查找的上下界
        left, right = 0, len(nums) - 1
        while left <= right:  # 当low == high时还剩下最后一个值需要进行检验
            # mid = (low + high) // 2
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1  # +1是因为mid已经验证过不符合条件，新的区间又mid+1开始
            elif nums[mid] > target:
                right = mid - 1 # 这里+1同上面原因相同
            else:
                return mid
        return -1  # 执行结束但是没有找到


nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))

nums1 = [-1,0,3,5,9,12]
target1 = 2
print(Solution().search(nums1, target1))


"""
#给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
"""
class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def searchInsert1(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        left = 0
        # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度
        right = size
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                # assert nums[mid] >= target
                # [1,5,7] 2
                right = mid
        # 调试语句
        print('left = {}, right = {}, mid = {}'.format(left, right, mid))
        return left


    # 对于是否接在原有序数组后面单独判断，不满足的时候，再在候选区间的索引范围 [0, size - 1] 内使用二分查找法进行搜索。
    def searchInsert2(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判 1
        if size == 0:
            return 0
        # 特判 2：如果比最后一个数字还要大，直接接在它后面就可以了
        if target > nums[-1]:
            return size

        left = 0
        right = size - 1
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target  # 检查条件，不符合就终止程序
                right = mid
        return left


nums = [-1,0,3,5,9,12]
target = 9
print(Solution1().searchInsert(nums, target))
print(Solution1().searchInsert1(nums, target))

nums1 = [-1,0,3,5,9,12]
target1 = 2
print(Solution1().searchInsert(nums1, target1))
print(Solution1().searchInsert1(nums1, target1))