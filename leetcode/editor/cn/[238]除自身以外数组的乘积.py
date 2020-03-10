#  给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之
#  外其余各元素的乘积。
#  示例: 
# 
#  输入: [1,2,3,4]
#  输出: [24,12,8,6]
#  提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。 
# 
#  说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  进阶： 
#  你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
#  Related Topics 数组
"""
[1, 2, 3, 4]
[1, 2, 6,24]
[24,24,12,4]

[24,12,8, 6]
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res, left, right = [1] * len(nums), 1, 1
        # 先令res[i] = left存储从左到右当前元素之前的元素乘积，即res[i]为nums[i - 1:]的乘积
        # [1,1,2,6]
        for i in range(len(nums)):
            # print(left) [1,1,2,6]
            res[i] = left
            left *= nums[i]
        print(res)

        # 动态计算左侧乘积和答案
        # right 存储从右到左当前元素之后的元素乘积：[1,4,12,24]
        # 此时res[i] *= right：即左右乘积前缀相乘，动态更新值
        for i in range(len(nums) - 1, -1, -1):
            # print(right)  [1,4,12,24]
            res[i] *= right
            right *= nums[i]

        return res

    def productExceptSelf0(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]
        right = nums[-1]
        for j in range(length - 2, -1, -1):
            res[j] *= right
            right *= nums[j]
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        res, left, right = [1] * len(nums), 1, 1

        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], left = res[i] * left, left * nums[i]
            res[j], right = res[j] * right, right * nums[j]
        return res

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res1 = []  # 从左到右，连续乘积
        res2 = []  # 从右到左，连续乘积
        res = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            left *= nums[i]
            res1.append(left)

        for i in range(len(nums)-1, -1, -1):
            right *= nums[i]
            res2.insert(0, right)

        for i in range(len(nums)):
            if i - 1 >= 0 and i <= len(nums) - 2:
                res[i] = res1[i-1] * res2[i+1]
            elif i == 0:
                res[i] = res2[i+1]
            elif i == len(nums) - 1:
                res[i] = res1[i-1]
        return res

    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        head = [1]
        tail = [1]

        for i in range(len(nums) - 1):
            head.append(nums[i] * head[i])
            tail.append(nums[-i - 1] * tail[i])

        res = []
        for j in range(len(nums)):
            res.append(head[j] * tail[-j - 1])

        return res





# leetcode submit region end(Prohibit modification and deletion)
nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
