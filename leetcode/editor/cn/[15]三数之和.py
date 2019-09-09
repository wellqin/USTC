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

class Solution:
    def threeSum(self, nums):
        # for num in nums:
        #     two_num = target - num
        res = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and j != i and k != j and k != i:
                        curRes = [nums[i], nums[j], nums[k]]
                        if curRes not in res:
                            res.append(curRes)

        return res

"""
清晰的思路：

排序
固定左边，如果左边重复，继续
左右弄边界，去重，针对不同的左右边界情况处理
"""

class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:   # 因为i=0这个元素会直接往下执行
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif tmp > 0:
                    r -= 1
                else:
                    l += 1
        return res

print(Solution().threeSum(nums = [-1, 0, 1, 2, -1, -4]))