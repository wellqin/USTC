#给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
#
# candidates 中的每个数字在每个组合中只能使用一次。 
#
# 说明： 
#
# 
# 所有数字（包括目标数）都是正整数。 
# 解集不能包含重复的组合。 
# 
#
# 示例 1: 
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
#所求解集为:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]
# 
#
# 示例 2: 
#
# 输入: candidates = [2,5,2,1,2], target = 5,
#所求解集为:
#[
#  [1,2,2],
#  [5]
#] 
#
"""
Combination
Sum
已经AC，做了minor
change.

递归取了当前这个数的时候idx也要从idx + 1
开始了
要判断combo not in res才append到res中去
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(remain, combi, idx):
            if remain < 0:
                return
            if remain == 0 and combi not in res:
                res.append(combi)
                return
            if idx >= len(candidates):
                return
            helper(remain, combi, idx + 1)
            helper(remain - candidates[idx], combi + [candidates[idx]], idx + 1)

        res = []
        candidates.sort()
        helper(target, [], 0)
        return res

    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target: break
                if j > i and candidates[j] == candidates[j - 1]: continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])

        backtrack(0, 0, [])
        return res
candidates =[2,5,2,1,2]
target =5
print(Solution().combinationSum(candidates, target))