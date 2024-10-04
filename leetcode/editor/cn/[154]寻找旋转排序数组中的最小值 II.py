# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
#
# 请找出其中最小的元素。 
#
# 注意数组中可能存在重复的元素。 
#
# 示例 1： 
#
# 输入: [1,3,5]
# 输出: 1
#
# 示例 2： 
#
# 输入: [2,2,2,0,1]
# 输出: 0
#
# 说明： 
#
# 
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
# 
#
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:  # 二分查找
        if not nums or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:  # 没有旋转
            return nums[left]

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[mid - 1]:   # [5,6,7,1,2,3,4]
                return nums[mid]
            elif nums[mid] > nums[right]:   # [5,6,7,1,2,3]
                left = mid + 1
            elif nums[mid] < nums[right]:   # [5,1,2,3,4]
                right = mid - 1
            elif nums[mid] == nums[right]:  # [5,6,1,1,1,1]
                right -= 1

        return nums[left]


nums = [2, 2, 2, 0, 1]
print(Solution().findMin(nums))
