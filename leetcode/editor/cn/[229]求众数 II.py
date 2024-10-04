# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 
# 
#  说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。 
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: [3] 
# 
#  示例 2: 
# 
#  输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2] 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = lookup.get(nums[i], 0) + 1
        return [x for x in lookup.keys() if lookup[x] > len(nums) // 3]

    # 摩尔投票法
    def majorityElement1(self, nums):
        res1, res2 = 0, 0  # 次数大于该数组长度1/3的值最多只有两个
        num1, num2 = 0, 0  # 两个变量出现的次数
        for num in nums:
            if num == res1:
                num1 += 1
                continue
            if num == res2:
                num2 += 1
                continue
            if num1 == 0:
                res1 = num
                num1 += 1
                continue
            if num2 == 0:
                res2 = num
                num2 += 1
                continue
            num2 -= 1
            num1 -= 1

        res = []
        if nums.count(res1) > len(nums) // 3:
            res.append(res1)
        if nums.count(res2) > len(nums) // 3 and res1 != res2:
            res.append(res2)
        return res


# leetcode submit region end(Prohibit modification and deletion)
nums = [1, 1, 1, 3, 3, 2, 2, 2]
print(Solution().majorityElement1(nums))
