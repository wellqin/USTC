# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。 
# 
#  注意: 
# 数组长度 n 满足以下条件: 
# 
#  
#  1 ≤ n ≤ 1000 
#  1 ≤ m ≤ min(50, n) 
#  
# 
#  示例: 
# 
#  
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 
# 输出:
# 18
# 
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#  
#  Related Topics 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            sums, cnt = 0, 1  # 表示目前的和，目前的组数，且cnt变量记录分组数
            for i in nums:  # 遍历这个数组
                if sums + i > mid:  # 让sums加上这个遍历着的数，如果这个加起来的和比上限大，说明要分组了
                    cnt += 1
                    sums = i  # 那么cnt += 1，同时这个数作为新组的开头，即sums = 这个遍历的数
                else:
                    sums += i  # 如果这个加起来的和比上限要小，那么就遍历下一个
            if cnt <= m:  # 更新依据 排除右侧的条件
                right = mid
            else:
                left = mid + 1
        return left


# class Solution1(object):
#     def splitArray(self, nums, m):
#         # binary search for min_max
#         left, right = sum(nums) // m, sum(nums)
#         while left <= right:
#             mid = left + ((right - left) >> 1)
#             if self.valid_max(nums, m, mid) and (not self.valid_max(nums, m, mid - 1)):
#                 return mid
#             else:
#                 if not self.valid_max(nums, m, mid):
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#
#         return right
#
#     def valid_max(self, nums, k, max):
#         n = len(nums)
#         div = 1
#         sum = nums[0]
#         for i in range(1, n):
#             if sum > max:
#                 return False
#             if sum + nums[i] > max:
#                 div += 1
#                 sum = nums[i]
#             else:
#                 sum += nums[i]
#         # note that we have to ensure sum <= max
#         return (sum <= max) and (div <= k)


# leetcode submit region end(Prohibit modification and deletion)
nums = [7, 2, 5, 10, 8]
m = 2
print(Solution().splitArray(nums, 2))
# print(Solution1().splitArray(nums, 2))
