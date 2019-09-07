#给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
#
# 你的算法时间复杂度必须是 O(log n) 级别。 
#
# 如果数组中不存在目标值，返回 [-1, -1]。 
#
# 示例 1: 
#
# 输入: nums = [5,7,7,8,8,10], target = 8
#输出: [3,4] 
#
# 示例 2: 
#
# 输入: nums = [5,7,7,8,8,10], target = 6
#输出: [-1,-1] 
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
        l, r = 0, len(nums) - 1
        # search for left bound
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                res.append(mid)
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if not res:
            return [-1, -1]

        # search for right bound, now we don't need to reset left pointer
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                res.append(mid)
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                # 这里直接返回res是因为前面如果判断左边界没返回的话就说明我们判断右边界的时候一定会append元素
        return res

nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums, target))