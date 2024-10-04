# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例: 
#
# 
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
#
# 说明: 
#
# 
# 给定数组的长度不会超过15。 
# 数组中的整数范围是 [-100,100]。 
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。 
# 
#

class Solution:
    # 回溯法
    def findSubsequences_hs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []  # 一组解
        incsq = [0]  # 一个解（n元0-1数组）

        def backtrack(t):
            if t == n:
                return
            incsq.append(0)
            s = {}
            for i in range(t + 1, n):  # 遍历第 t + 1~n-1 列（即n个状态)
                if nums[i] >= nums[t] and nums[i] not in s:  # 同一层循环不能有重复数
                    s[nums[i]] = 1
                    incsq[-1] = nums[i]
                    res.append(incsq[:])  # 保存（一个解），注意incsq[:]
                    backtrack(i)
            incsq.pop()  # 回溯，出栈

        # 第一个数单独遍历，避免加入单个数
        s = {}
        for i in range(n):
            if nums[i] not in s:
                s[nums[i]] = 1
                incsq[0] = nums[i]
                backtrack(i)
        return res

    def findSubsequences_dfs(self, nums):
        res = set()
        n = len(nums)

        def helper(loc, tmp):
            if len(tmp) > 1 and tmp not in res:
                res.add(tmp)
                print(loc, tmp)
            for i in range(loc + 1, n):
                if tmp[-1] <= nums[i]:
                    helper(i, tmp + (nums[i],))

        for i in range(n):
            helper(i, (nums[i],))
        return [list(i) for i in res]


# print(Solution().findSubsequences_hs([4, 6, 7, 7]))
print(Solution().findSubsequences_dfs([4, 6, 7, 7]))
