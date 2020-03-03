# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。 
# 
#  珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后
# 这一小时内不会再吃更多的香蕉。 
# 
#  珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。 
# 
#  返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入: piles = [3,6,7,11], H = 8
# 输出: 4
#  
# 
#  示例 2： 
# 
#  输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
#  
# 
#  示例 3： 
# 
#  输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= piles.length <= 10^4 
#  piles.length <= H <= 10^9 
#  1 <= piles[i] <= 10^9 
#  
#  Related Topics 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
import math
from typing import List


class Solution(object):
    @staticmethod
    def minEatingSpeed(piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def isTrue(K):  # 判断当前值，是否满足要求
            return sum((p-1)//K + 1 for p in piles) <= H

        if len(piles) == 1:
            return ((sum(piles)-1)//H)+1

        low, high = ((sum(piles)-1)//H)+1, max(piles)  # 初始化上下界

        while low < high:  # 以low ，high 为上下界，二分搜索
            mid = (low + high) // 2
            if not isTrue(mid):
                low = mid + 1
            else:
                high = mid
        return low

    @staticmethod
    def minEatingSpeed1(piles: List[int], H: int) -> int:
        for k in range(math.ceil(sum(piles) / H), max(piles) + 1):
            if sum((p - 1) // k + 1 for p in piles) <= H: return k
# leetcode submit region end(Prohibit modification and deletion)
