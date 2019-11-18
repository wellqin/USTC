#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。 
#
# 注意：答案中不可以包含重复的三元组。 
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
#满足要求的三元组集合为：
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]
# 
#
from typing import *
# print(list(range(5,5)))
# class Solution:
#     def threeSum(self, nums):
#         # for num in nums:
#         #     two_num = target - num
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0 and j != i and k != j and k != i:
#                         curRes = [nums[i], nums[j], nums[k]]
#                         if curRes not in res:
#                             res.append(curRes)
#
#         return res
import copy
# nums = [-1, 0, 1, 2, -1, -4]
# 二数之和改版，不过边界重复未处理
# class Solution:
#     def threeSum(self, nums):
#         res = []
#         for index in range(len(nums)):
#             target = 0 - nums[index]
#             lookup = {}
#
#             for i, val in enumerate(nums[:index] + nums[index+1:]):
#                 if target - i in lookup:
#                     res.append([nums[index], val, target - val])
#
#                 lookup[val] = i
#         return res

"""
清晰的思路：

排序
固定左边，如果左边重复，继续
左右弄边界，去重，针对不同的左右边界情况处理
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, res =len(nums), []
        if (not nums or n<3):
            return []
        nums.sort()

        for i in range(n):
            if (nums[i]>0):
                return res
            if (i>0 and nums[i] == nums[i-1]): # [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1]]
            # if (nums[i] == nums[i+1]):  [[-4, 2, 2], [-1, 0, 1]]
                continue
            L = i+1
            R = n-1
            while (L<R):
                cur_sum = nums[i] + nums[L] + nums[R]
                if (cur_sum == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L<R and nums[L] == nums[L+1]):
                        L = L+1
                    while (L<R and nums[R]==nums[R-1]):
                        R = R-1
                    L = L+1
                    R = R-1
                elif (cur_sum < 0):
                    L = L + 1
                else:
                    R = R-1
        return res

print(Solution().threeSum(nums = [-1, 0, 1, 1, 2, 2, -1, -4]))