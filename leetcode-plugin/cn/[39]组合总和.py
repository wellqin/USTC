#给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
#
# candidates 中的数字可以无限制重复被选取。 
#
# 说明： 
#
# 
# 所有数字（包括 target）都是正整数。 
# 解集不能包含重复的组合。 
# 
#
# 示例 1: 
#
# 输入: candidates = [2,3,6,7], target = 7,
#所求解集为:
#[
#  [7],
#  [2,2,3]
#]
# 
#
# 示例 2: 
#
# 输入: candidates = [2,3,5], target = 8,
#所求解集为:
#[
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
#] 
#
"""
此题可以用递归拆分为子问题求解。 每一个子问题（步），有两种情况需要考虑：

    跳过当前数字
    取当前数字并继续保留当前数字为 candidates

失败条件是 candidates 为空或 target 为负 或 idx >= len(cadidates)

beats 48.49%
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(target, combi, idx):
            if target < 0:
                return
            if target == 0:
                res.append(combi)
                return
            if idx >= len(candidates):
                return
            helper(target, combi, idx + 1)
            helper(target - candidates[idx], combi + [candidates[idx]], idx)

        res = []
        helper(target, [], 0)
        return res


    def backtrack(self, nums, target): # 回溯
        nums.sort()
        n = len(nums)
        res = []

        def helper(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + nums[j] > target:
                    continue
                helper(j, tmp_sum + nums[j], tmp + [nums[j]])

        helper(0, 0, [])
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []

        def helper(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                helper(candidates[i:], target - candidates[i], temp_list + [candidates[i]])

        helper(candidates, target, [])
        return res

candidates = [2,3,5]
target = 8
print(Solution().backtrack(candidates, target))