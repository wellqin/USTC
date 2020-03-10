# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。 
# 
#  找到所有出现两次的元素。 
# 
#  你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？ 
# 
#  示例： 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [2,3]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # 使用了O(n)空间，在O(n)时间复杂度内
        # lookup = {}
        # for i in range(len(nums)):
        #     lookup[nums[i]] = lookup.get(nums[i], 0) + 1
        # return [x for x in lookup.keys() if lookup[x] > 1]
        lookup = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in lookup:
                lookup[nums[i]] = i
            else:
                res.append(nums[i])
        return res

    def findDuplicates1(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            else:
                res.append(num)
        return res




# leetcode submit region end(Prohibit modification and deletion)
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDuplicates(nums))
