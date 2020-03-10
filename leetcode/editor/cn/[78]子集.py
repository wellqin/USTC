# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。 
#
# 示例: 
#
# 输入: nums = [1,2,3]
# 输出:
# [
#  [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
from typing import List


class Solution:
    def subsets(self, nums):  # dfs or 回溯
        if not nums:
            return []
        res = []
        n = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                # if len(temp_list + [nums[i]]) == 2:
                #     res.append(temp_list + [nums[i]])
                #     continue
                helper(i + 1, temp_list + [nums[i]])

        helper(0, [])
        return res

    def subsets1(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def subsets2(self, nums):  # 回溯
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def search(tmp_res, idx):
            if idx == len(nums):
                res.append(tmp_res)
                return

            search(tmp_res + [nums[idx]], idx + 1)
            search(tmp_res, idx + 1)

        search([], 0)
        return res


nums = [1, 1, 2]
print(Solution().subsets(nums))
# print(Solution().subsets1(nums))
