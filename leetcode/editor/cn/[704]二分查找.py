# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 
#
# 示例 2: 
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
# 
#
# 
#
# 提示： 
#
# 
# 你可以假设 nums 中的所有元素是不重复的。 
# n 将在 [1, 10000]之间。 
# nums 的每个元素都将在 [-9999, 9999]之间。 
# 
#
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        return nums[left] == target if left else -1

    def search1(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchLeft(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        left = 0
        right = len(nums)  # 注意
        while left < right:  # 注意
            mid = left + ((right - left) >> 1)
            if target == nums[mid]:
                right = mid
            elif target < nums[mid]:
                right = mid  # 注意
            else:
                left = mid + 1
        if left == right: return -1
        return nums[left] == target if left else -1

    def findRight(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        print("left - 1", left - 1)
        return left - 1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # 确定查找的上下界
#         low, high = 0, len(nums) - 1
#         while low <= high:  # 当low == high时还剩下最后一个值需要进行检验
#             mid = (low + high) // 2
#             if nums[mid] < target:
#                 low = mid + 1  # +1是因为mid已经验证过不符合条件，新的区间又mid+1开始
#             elif nums[mid] > target:
#                 high = mid - 1 # 这里+1同上面原因相同
#             else:
#                 return mid
#         return -1  # 执行结束但是没有找到


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search1(nums, target))

nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 2
print(Solution().search1(nums1, target1))

nums2 = [1, 2, 2, 2, 3]
target2 = 0
print(Solution().searchLeft(nums2, target2))

nums3 = [1, 2, 2, 2, 3]
target3 = 3
print(Solution().findRight(nums3, target3))
