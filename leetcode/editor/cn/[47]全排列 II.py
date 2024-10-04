# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例: 
#
# 输入: [1,1,2]
# 输出:
# [
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
# ]
#

# 无重复元素全排列问题
"""
这里我们应该使用计数器记录nums中每个元素出现的次数，如果当前元素超过次数则返回，
但是这里还有一个问题就是可能会出现同样的排列多次，这里的解决办法就是同一层不许出现重复元素，
这里有两种解决办法，一种是直接传入distinct的数组，还有一种是使用一个集合记录当前层已使用的元素。
"""
from typing import List


class Solution(object):
    def backtrack(self, nums):
        if not nums:
            return []
        res = []
        nums.sort()
        # 先排序，然后判断和前一个是否重复
        # res用来存储所有的返回所有排列，templist用来生成每个排列
        def helper(res, templist):
            if len(templist) == len(nums):
                res.append(templist[:])
            else:
                for i in range(len(nums)):
                    if nums[i] in templist:  # 如果在当前排列中已经有i了，就continue，相当于分支限界，即不对当前节点子树搜寻了
                        continue


                    templist.append(nums[i])
                    helper(res, templist)
                    templist.pop()  # 把结尾的元素用nums中的下一个值替换掉，遍历下一颗子树

        helper(res, [])
        return res


nums = [1, 1, 2]
print(Solution().backtrack(nums))

from collections import Counter


class Solution1(object):

    def backtrack(self, nums):

        res, tmplist = [], []
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        length = len(nums)

        def helper(res, tmplist, counter, nums, length):
            if len(tmplist) == length:  # 回溯点
                res.append(tmplist[:])
                return

            for i in nums:  # 横向遍历
                if counter[i] == 0:  # 分支限界
                    continue

                counter[i] -= 1
                tmplist.append(i)
                helper(res, tmplist, counter, nums, length)  # 纵向遍历
                counter[i] += 1
                tmplist.pop()

        # 同一层不许出现重复元素,使用一个集合记录当前层已使用的元素。直接传入distinct的数组
        helper(res, tmplist, counter, list(set(nums)), length)

        return res

    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack1([], nums, check)
        return self.res

    def backtrack1(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack1(sol + [nums[i]], nums, check)
            check[i] = 0

print(Solution1().backtrack(nums))
print(Solution1().permuteUnique1(nums))
