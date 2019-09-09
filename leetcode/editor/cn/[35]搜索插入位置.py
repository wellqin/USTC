#给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
#
# 你可以假设数组中无重复元素。 
#
# 示例 1: 
#
# 输入: [1,3,5,6], 5
#输出: 2
# 
#
# 示例 2: 
#
# 输入: [1,3,5,6], 2
#输出: 1
# 
#
# 示例 3: 
#
# 输入: [1,3,5,6], 7
#输出: 4
# 
#
# 示例 4: 
#
# 输入: [1,3,5,6], 0
#输出: 0
# 
#

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int] 排序数组
        :type target: int
        :rtype: int
        """
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                return i
        return i

    def searchInsert1(self, nums, target):
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
        