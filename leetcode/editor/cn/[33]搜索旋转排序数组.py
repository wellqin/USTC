# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
#
# 你可以假设数组中不存在重复的元素。 
#
# 你的算法时间复杂度必须是 O(log n) 级别。 
#
# 示例 1: 
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
#
# 示例 2: 
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
"""

直接用二分，O(lg(n))

如果是mid，return mid
如果mid在绿色线上，就对绿色线进行二分
如果mid在红色线上，就对红色线进行二分
都没找到，return -1
"""
from typing import *


class Solution1(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)  # 没有>>2速度快
            if nums[mid] == target:
                return mid

            # 当nums[mid] < nums[right]，我们可以认为数组从nums[mid]到nums[high]是升序的，
            # 那么如果target在[nums[mid],nums[right]]之间，我们令low=mid+1;否则令high=mid-1
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # 当nums[mid] >= nums[right]，我们可以认为数组从nums[low]到nums[mid-1]是升序的，
            # 那么如果target在[nums[mid],nums[right]]之间，我们令high=mid-1;否则令low=mid+1
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if (nums[0] == target) else -1

        def find_rotateindex(left, right):
            if nums[left] < nums[right]:  # 没旋转
                return 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < nums[mid - 1]:
                    return mid
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        rotateindex = find_rotateindex(0, n - 1)

        def find(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if rotateindex == 0:
            return find(0, n - 1)  # 没旋转，直接二分查找
        if target >= nums[0]:
            return find(0, rotateindex)
        else:
            return find(rotateindex, n - 1)

    def searchSelf(self, nums: List[int], target: int) -> int:
        # 数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )
        # 先找到旋转点

        # 特判
        if not nums or len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0 if (nums[0] == target) else -1

        def findCicle(nums):
            left = 0
            right = len(nums) - 1
            while nums[left] > nums[right]:
                right -= 1
            return right + 1

        point = findCicle(nums)

        nums1 = nums[:point]
        nums2 = nums[point:]

        def find(nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if nums1 and nums1[0] <= target <= nums1[-1]:  # 防止数组为空
            res = find(nums1)
            return res if res != -1 else -1
        elif nums2 and nums2[0] <= target <= nums2[-1]:
            res = find(nums2)
            return point + res if res != -1 else -1
        else:
            return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

nums1 = [1, 3]
target1 = 2
print(Solution().searchSelf(nums1, target1))
print(Solution1().search(nums, target))
