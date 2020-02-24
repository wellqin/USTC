# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。 
#
# 示例 1: 
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 
#
# 示例 2: 
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 
#
# 示例 3: 
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 
#
# 示例 4: 
#
# 输入: [1,3,5,6], 0
# 输出: 0

# 【1, 3, 5, 6】，target=2， nums[mid]=3, 终于想明白了：当nums[mid]>target,
# 表明nums[mid]可能是解，所以右边间right =mid 先保留nums[mid]得到【1,3】, 再明确排除1之后，
# 最后 left=right退出时，剩下那一个可能的解【3】，就一定是解，所以直接return left, 有点绕
#


class Solution(object):
    def searchInsertN(self, nums, target):
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                return i
        return i

    def searchInsert1(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def searchInsert(self, nums, target):  # 排序数组和一个目标值
        if not nums or len(nums) == 0:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:  # 此部分可以去除，本题不存在重复相等情况
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


nums = [1, 3, 5, 6]
target = 2
print(Solution().searchInsert(nums, target))
