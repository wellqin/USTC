#给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。 
#
# 示例 1： 
#
# 
#输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
#输出： True
#说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。 
#
# 
#
# 注意: 
#
# 
# 1 <= k <= len(nums) <= 16 
# 0 < nums[i] < 10000 
# 
# Related Topics 递归 动态规划

"""
总体思路就是不停的去凑够这个平均值，凑够一个减1，只要平均值为整数，凑到最后一个的时候所有未使用的的数加起来肯定为这个值。

避免重复考虑的情况则永远将数按从大到小来凑，如我们要凑5，[3,2]和[2,3]都能凑出5但明显是同一种情况，我们拿3凑了5以后，
只从比3小的数里考虑凑剩下的2即可避免掉这种重复。

"""
from typing import List
#leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k:  # 为空或不够分
            return False
        avg, mod = divmod(sum(nums), k)
        if mod:  # 不能整除
            return False
        nums.sort(reverse=True)  # 倒序排列
        if nums[0] > avg:  # 有超过目标的元素
            return False
        used = set()  # 记录已使用的数

        def dfs(k, start=0, tmpSum=0):  # 当前还需要凑的avg个数，当前从哪个数开始考虑，以及当前已凑够的和
            if tmpSum == avg:  # 如果已凑满一个
                return dfs(k - 1, 0, 0)  # 那么从最大数重新开始考虑，凑下一个
            if k == 1:  # 只剩最后一个，那么剩下的没使用的数加起来肯定凑满
                return True
            for i in range(start, len(nums)):  # 优先用大的数的凑
                if i not in used and nums[i] + tmpSum <= avg:  # 如果该数未使用并且可以用来凑
                    used.add(i)  # 使用该数
                    if dfs(k, i + 1, nums[i] + tmpSum):  # 继续用比该数小的数来凑
                        return True
                    used.remove(i)  # 没有得到可用方案，则换个数来凑
            return False

        return dfs(k)


        
#leetcode submit region end(Prohibit modification and deletion)
