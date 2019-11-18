#给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意： 
#
# 答案中不可以包含重复的四元组。 
#
# 示例： 
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
#满足要求的四元组集合为：
#[
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
#]
# 
#
from typing import *
import collections
"""
思想类似于 2SUM，先得到任意两个数字的和记入字典，然后再获得其余任意俩个数字，看看是否匹配。
2个 2SUM 相当于 4SUM。时间复杂度为 O(N^2)

1.用 combination 获得 nums 中任意两个不同索引的组合
2.用字典记录任意两个数字的和，dic =｛除了这两个数字之外还差多少：这俩个数字在 nums 中的索引｝
3.用 r 记录所有满足条件的索引序列，注意此时可能含有重复的索引
4.利用 len + set 保证 a，b，c，d 各不相等，用 set 删除重复的结果

"""

"""
Python的itertools库中提供了combinations方法可以轻松的实现排列组合
"""
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from itertools import combinations as com
        dic, l = collections.defaultdict(list), [*com(range(len(nums)), 2)]
        for a, b in l: dic[target - nums[a] - nums[b]].append((a, b))
        r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]
        return [*set(tuple(sorted(nums[i] for i in t)) for t in r if len(set(t)) == 4)]


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution1().fourSum(nums, target))
        