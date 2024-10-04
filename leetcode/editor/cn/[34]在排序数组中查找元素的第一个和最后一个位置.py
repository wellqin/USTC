# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。 
#
# 如果数组中不存在目标值，返回 [-1, -1]。 
#
# 示例 1: 
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2: 
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#

"""
二分法，先找target出现的左边界，判断是否有target后再判断右边界

找左边界：二分，找到一个index
    该index对应的值为target
    并且它左边index - 1 对应的值不是target（如果index为0则不需要判断此条件）
    如果存在index就将其append到res中

判断此时res是否为空，如果为空，说明压根不存在target，返回[-1, -1]

找右边界：二分，找到一个index（但是此时用于二分循环的l可以保持不变，r重置为len(nums) - 1，这样程序可以更快一些）
    该index对应的值为target
    并且它右边index + 1 对应的值不是target（如果index为len(nums) - 1 则不需要判断此条件）
    如果存在index就将其append到res中
AC
代码
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return [-1, -1]

        res = []
        left, right = 0, len(nums) - 1
        # search for left bound
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                res.append(mid)
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if not res:
            return [-1, -1]

        # search for right bound, now we don't need to reset left pointer
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                res.append(mid)
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                # 这里直接返回res是因为前面如果判断左边界没返回的话就说明我们判断右边界的时候一定会append元素
        return res

    # 采取while left < right形式
    def searchRangeSelf(self, nums, target):
        return [self.findLeft(nums, target), self.findRight(nums, target)]

    # find left
    def findLeft(self, nums, target):
        left = 0
        right = len(nums)  # 注意
        while left < right:  # 注意
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                right = mid  # 注意
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid  # 注意
        # if left == right: return -1
        # return nums[left] == target if left else -1
        # return left
        return left if not left == len(nums) and nums[left] == target else -1

    # find right
    def findRight(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                left = mid + 1  # 注意
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        # if left == 0: return -1
        # return nums[left - 1] == target if (left - 1) else -1
        # return left - 1  # 注意
        return left - 1 if left != 0 and nums[left - 1] == target else -1

    # 采取while left <= right形式
    def searchRangeEqual(self, nums, target):
        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def right_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right >= 0 and nums[right] == target:
            # 退出循环时，left比right大1，因为left = right时，left已经到边界，但还是left = mid + 1
            # 此时right所在位置就是右边界
            return right
        else:
            return -1

    def left_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left <= len(nums) - 1 and nums[left] == target:
            # 退出循环时，left比right大1，因为left = right时，right已经缩小边界到了左边界
            # 同时right = mid - 1退出循环，此时上一步left = right代表已经找到边界了
            # 所以返回的是left
            return left  # 注意判断最后一个元素
        else:
            return -1


# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# print(Solution().searchRangeSelf(nums, target))

nums1 = [8, 8, 8, 8, 8, 8, 8, 8]
target = 8
print(Solution().searchRangeSelf(nums1, target))
print(Solution().searchRangeEqual(nums1, target))
print(Solution().searchRange(nums1, target))

