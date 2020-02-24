# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
#
# 请找出其中最小的元素。 
#
# 你可以假设数组中不存在重复元素。 
#
# 示例 1: 
#
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2: 
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
#
from typing import List


class Solution:
    def findMinSelf(self, nums: List[int]) -> int:  # O(n)效率低
        if not nums or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while nums[left] > nums[right]:
            right -= 1
        return nums[right + 1]

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
            if nums[mid] < nums[mid - 1]:  # [5,6,7,1,2,3,4]
                return nums[mid]
            elif nums[mid] > nums[right]:  # [5,6,7,1,2,3]
                left = mid + 1
            elif nums[mid] < nums[right]:  # [5,1,2,3,4]
                right = mid - 1
        return nums[left]


# nums = [4,5,6,7,0,1,2]
nums = [2, 1]
print(Solution().findMin(nums))
