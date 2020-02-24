# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1: 
#
# 输入: [1,3,4,2,2]
# 输出: 2
# 
#
# 示例 2: 
#
# 输入: [3,1,3,4,2]
# 输出: 3
# 
#
# 说明： 
#
# 
# 不能更改原数组（假设数组是只读的）。 
# 只能使用额外的 O(1) 的空间。 
# 时间复杂度小于 O(n2) 。 
# 数组中只有一个重复的数字，但它可能不止重复出现一次。 
# 
#
from typing import List


class Solution:
    # 思路一：集合  不符合空间
    def findDuplicate(self, nums: List[int]) -> int:
        lookup = {}  # 额外的 O(n) 的空间
        if not nums or len(nums) == 0:
            return 0

        # m = collections.Counter(nums)
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = 1
            else:
                lookup[nums[i]] += 1

        res = [k for k, v in lookup.items() if v >= 2]
        return res[0]

    # 思路二：排序
    # 如果对数字进行排序，则任何重复的数字都将与排序后的数组相邻

    # 思路三：弗洛伊德的乌龟和兔子（循环检测）
    # set(nums) 实际上隐式的占用了 O(n) 的空间复杂度
    # return (sum(nums)-sum(set(nums)))//(len(nums) - len(set(nums)))

    def findDuplicate1(self, nums: List[int]) -> int:  # 二分法
        left = 1
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return right


nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate1(nums))
