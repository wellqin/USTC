# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例: 
#
# 输入: [1,2,3]
# 输出:
# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
# ]
#

# 无重复元素全排列问题 N 个数字的全排列一共有 N!这么多个
from typing import List


class Solution(object):
    # def backtrack(self,nums):
    #     if not nums:
    #         return []
    #     res = []
    #
    #     # res用来存储所有的返回所有排列，templist用来生成每个排列
    #     def helper(res, templist, nums):
    #         if (len(templist) == len(nums)):
    #             res.append(templist[:])
    #         else:
    #             for i in nums:
    #                 if i in templist:  # 如果在当前排列中已经有i了，就continue，相当于分支限界，即不对当前节点子树搜寻了
    #                     continue
    #                 templist.append(i)
    #                 helper(res, templist, nums)
    #                 templist.pop()  # 把结尾的元素用nums中的下一个值替换掉，遍历下一颗子树
    #
    #     helper(res, [], nums)
    #     return res

    def backtrackSelf(self, nums):
        if not nums:
            return []
        n = len(nums)
        res = []

        def helper(nums, temp_list):
            # 触发结束条件
            if len(temp_list) == n:
                res.append(temp_list[:])  # res.append(temp_list)会出错。因为引用传递
                return
            for i in range(len(nums)):
                # 排除不合法的选择
                if nums[i] in temp_list:
                    continue

                temp_list.append(nums[i])  # 做选择
                helper(nums, temp_list)  # 进入下一层决策树
                temp_list.remove(nums[i])  # 取消选择

        helper(nums, [])  # 此处[]赋给temp_list，而res=[]会导致temp_list与res指向同一片区域，在temp_list.remove时，会同时变更res
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                print(nums[:i] + nums[i + 1:], tmp + [nums[i]])
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


    def permuteswap(self, nums: [int]) -> [[int]]:
        def recursive(count, res):
            if count == len(nums):
                res.append(nums.copy())

            for i in range(count, len(nums)):
                nums[i], nums[count] = nums[count], nums[i]
                recursive(count + 1, res)
                nums[i], nums[count] = nums[count], nums[i]

        res = []
        recursive(0, res)
        return res


nums = [1, 2, 3]
# print(Solution().backtrack(nums))
print(Solution().backtrackSelf(nums))
print(Solution().permute(nums))
