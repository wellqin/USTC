# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1: 
#
# 输入: [1,2,0]
# 输出: 3
# 
#
# 示例 2: 
#
# 输入: [3,4,-1,1]
# 输出: 2
# 
#
# 示例 3: 
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 
#
# 说明: 
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。 
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 判断taInt是否在nums里这个操作本身的时间复杂度是O(n),所以算法是O(n*2)
        if not nums:
            return 1
        taInt = 1
        for i in range(len(nums)):
            if taInt in nums:
                taInt += 1
            else:
                return taInt
        return taInt

    # 对于任意的数组长度为n，则缺失的第一个正数肯定是在[1, ...,n+1]中；
    # nums.append(0) 保证数组的长度为n+1，实际上最终在数组index [1,...,n]中做判断；
    # 统计频率 nums[i]%n；
    # 依次对 index [1, ...,n]的值做判断；
    # 若nums[i] < n 则说明i从未出现过；

    def firstMissingPositive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        print('nums1', nums)

        for i in range(len(nums)):
            nums[nums[i] % n] += n  # 统计频率
        print('nums2', nums)

        for i in range(1, len(nums)):
            if nums[i] // n == 0:  # 表明i这个数从来没有出现过，以为nums[i] < n
                return i
        return n

        # leetcode submit region end(Prohibit modification and deletion)


nums = [-3, 1, 8, 2, 3, 4, -2]
print(Solution().firstMissingPositive1(nums))
