#给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
#
# 说明：解集不能包含重复的子集。 
#
# 示例: 
#
# 输入: [1,2,2]
#输出:
#[
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
#] 
#

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

        helper2(0, n, [])
        return res
nums = [1,2,2]
print(Solution().subsetsWithDup(nums))
print(c2)

# print(Solution().subsetsWithDup(nums))
# print(c1)


from collections import Counter
class Solution1:
    def subsets(self, nums):  # dfs or 回溯
        if not nums:
            return []
        res = []
        n = len(nums)
        counter = Counter(nums)

        def helper(res, temp_list, nums, n):

            res.append(temp_list)

            for i in nums:
                if counter[i] == 0:
                    continue
                counter[i] -= 1
                temp_list.append(i)
                helper(res, temp_list, nums, n)
                counter[i] += 1
                temp_list.pop()

        helper(res, [], list(set(nums)), n)
        return res

print(Solution1().subsets(nums))