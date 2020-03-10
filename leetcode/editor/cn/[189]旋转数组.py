# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1: 
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
# 说明: 
#
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
# 要求使用空间复杂度为 O(1) 的 原地 算法。 
# 
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return
        if k == len(nums): return
        if k > len(nums):
            k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate1(self, nums: List[int], k: int) -> None:
        # 不写切片相当于nums修改的地址重新指向右边的临时地址，
        # 写切片相当于按着切片下标修改值，前者在线上判定里无法AC，线上判定只判定原地地址的情况，
        # 不写切片的nums只在函数内有效。
        nums[:] = nums[-k % len(nums):] + nums[: -k % len(nums)]
        return nums

# leetcode submit region end(Prohibit modification and deletion)
nums = [1,2,3,4,5,6,7]
k = 2
print(Solution().rotate(nums, k))
