# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。 
# 
#  编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。 
# 
#  示例 1: 
# 
#  输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false 
# 
#  进阶: 
# 
#  
#  这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。 
#  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？ 
#  
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

"""
对比33题可以发现，我们的改变只有下面几点：
1）把33题中的return mid和return -1分别改成了return True和return False，因为题目要求，没什么可说的。
2）去掉了33题elif nums[mid] >= nums[high]:中的等号，因为我们需要将等号成立的情况单独拿出来做判断。
3）加了下面的语句，这里的else也就是nums[mid] = nums[high]的情况，正如上面所说，如果该式成立，我们就让high自减1，相当于去掉了重复元素。
    else:
    high = high - 1

综上所述，其实本题我们实际的改变只有3)，只加了两行就可以从33题转换到81题。
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:  # (2) 去掉等号，因为我们需要将等号成立的情况单独拿出来做判断
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1  # nums[mid] = nums[high]时，自减1，相当于去掉了重复元素
        return False
# leetcode submit region end(Prohibit modification and deletion)
