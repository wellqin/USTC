
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
#
# 示例: 
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
#

# class Solution:
#     def twoSum(self, nums, target):
#         if not target:
#             return
#         lookup = dict()
#         for i in nums:
#             if target - i not in nums and target - i == i:
#                 continue
#             else:
#                 j = nums.index(target - i)
#                 return [nums.index(i), j]
#
# nums = [3, 2, 4]
# target = 6
# print(Solution().twoSum(nums, target))

"""
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
result = sorted(student_tuples, key=lambda student_tuples: student_tuples[2])
# result = sorted(student_tuples, key=lambda i: i[2])
print(result)
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        print(sorted_id)

        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for index, i in enumerate(nums):
            j = target - i
            if j in lookup:
                return [lookup[j], index]
            lookup[i] = index
        return None

    def two_sum(self, nums, target):
        """这样写更直观，遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i


nums = [2, 7, 11, 15, 3]
target = 5
print(Solution().two_sum(nums, target))

