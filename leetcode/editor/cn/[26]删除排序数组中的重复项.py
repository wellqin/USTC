# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。 
#
# 示例 1: 
#
# 给定数组 nums = [1,1,2], 
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
#
# 示例 2: 
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 
#
# 说明: 
#
# 为什么返回数值是整数，但输出的答案是数组呢? 
#
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。 
#
# 你可以想象内部操作如下: 
#
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
# 
#
from typing import *


class Solution:
    # 1. 正向while循环法
    """
    这样用for循环就会衍生出一个问题: 在遍历列表/数组/切片等的过程中, 此时该列表/数组/切片等的长度会发生变化.
    这里代码用while loop而不用for loop是因为pop操作之后nums的长度会变化
    如：for i in range(len(nums)-1)实际上固定了range里面的值了，不会二次判断
    """

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if not nums:
    #         return 0
    #     idx = 0
    #     while idx < n-1:  # 这里的n固定了里面的值了，不会二次判断，写成len(nums)会每次判断
    #         if nums[idx] == nums[idx+1]:
    #             nums.pop(idx)
    #         else:
    #             idx += 1
    #     return len(nums)

    def removeDuplicates2(self, nums):
        idx = 0
        while idx < len(nums) - 1:  # 若为len(nums)，则list index out of range
            if nums[idx] == nums[idx + 1]:
                nums.pop(idx + 1)
            else:
                idx += 1
        return len(nums)

    # 2. 逆向
    # 反向遍历时间效率O(N^2)空间效率O(1)，逆遍历可以防止删除某个元素后影响下一步索引的定位。
    def removeDuplicates3(self, nums):
        for num_index in range(len(nums) - 1, 0, -1):
            if nums[num_index] == nums[num_index - 1]:
                nums.pop(num_index)
        return len(nums)

    """
    3. 快慢指针
    在上面首先注意数组是有序的，那么重复的元素一定会相邻。
    要求删除重复元素，实际上就是将不重复的元素移到数组的左侧。
    时间复杂度：O(n)，假设数组的长度是 n，那么 i 和 j 分别最多遍历 n 步。
    """

    def removeDuplicates4(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):  # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1 if nums else 0

    # 快慢指针方法对于无重复元素的优化
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):  # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
            if nums[j] != nums[i]:
                if (j - i) > 1:
                    nums[i + 1] = nums[j]
                i += 1
        return i + 1 if nums else 0


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates2(nums))
