# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。 
#
# 示例: 
#
# 输入: [1,2,2]
# 输出:
# [
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
# ]
#
from typing import List

c1 = 0
c2 = 0


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()

        # 思路1
        def helper1(idx, n, temp_list):
            global c1
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                c1 += 1
                helper1(i + 1, n, temp_list + [nums[i]])

        # 思路2
        def helper2(idx, n, temp_list):
            global c2
            res.append(temp_list)
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                c2 += 1
                helper2(i + 1, n, temp_list + [nums[i]])

        def helper3(idx, temp_list):
            if idx == len(nums):
                if temp_list not in res:
                    res.append(temp_list)
                    # return here is wrong 如果出现重复的将不会return
                return  # 要保证return回去，不能在向下走了，此处肯定return
            helper3(idx + 1, temp_list + [nums[idx]])
            helper3(idx + 1, temp_list)

        # helper3(0, [])
        # print(res)
        # reList = list(set([tuple(t) for t in res]))
        # reList = [list(v) for v in reList]

        def helper4(idx, temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                helper4(i + 1, temp_list + [nums[i]])

        helper4(0, [])

        return res


nums = [1, 1, 2]
# print(Solution().subsetsWithDup(nums))
# print(c2)

# print(Solution().subsetsWithDup(nums))
# print(c1)


from collections import Counter


class Solution1:
    # 刚开始我们只有空集一个答案，循环所有可能的数字，每次循环我们对当前答案的每一种情况考虑加入从1到上限次该数字并更新答案即可
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        res = [[]]
        for i, v in dic.items():
            temp = res.copy()
            for j in res:
                temp.extend(j + [i] * (k + 1) for k in range(v))
            res = temp
        return res

    # def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
    #     if not nums:
    #         return []
    #     nums.sort()
    #     res = [[]]
    #     pos = 0
    #
    #     for i in range(len(nums)):
    #         if i >= 1 and nums[i] == nums[i - 1]:
    #             pos = len(res)
    #             res = res + [[nums[i]] + num for num in res[pos:]]
    #         else:
    #             res = res + [[nums[i]] + num for num in res]
    #         pos = len(res)
    #
    #     return res

    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def dfs(deepth, temp_list):
            res.append(temp_list)
            for i in range(deepth, n):
                if i > deepth and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, temp_list + [nums[i]])

        dfs(0, [])
        return res


# nums1 = [4, 4, 4, 1, 4]

# print(Solution1().subsetsWithDup(nums))
print(Solution1().subsetsWithDup1(nums))
