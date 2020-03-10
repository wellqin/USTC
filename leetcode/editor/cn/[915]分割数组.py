# 给定一个数组 A，将其划分为两个不相交（没有公共元素）的连续子数组 left 和 right， 使得： 
# 
#  
#  left 中的每个元素都小于或等于 right 中的每个元素。 
#  left 和 right 都是非空的。 
#  left 要尽可能小。 
#  
# 
#  在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
#  
# 
#  示例 2： 
# 
#  输入：[1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 30000 
#  0 <= A[i] <= 10^6 
#  可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。 
#  
# 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lmaxv = A[0]
        maxv = A[0]
        l = 0
        for i in range(len(A)):
            if A[i] < lmaxv:
                lmaxv = maxv
                l = i
            elif A[i] > maxv:
                maxv = A[i]
        return l + 1

    def partitionDisjoint1(self, A: List[int]) -> int:
        l_max = [0 for i in range(len(A))]
        r_min = [0 for i in range(len(A))]
        l_max[0] = A[0]
        r_min[-1] = A[-1]
        for i in range(1, len(A)):
            l_max[i] = max(A[i], l_max[i-1])
        for i in range(len(A)-2, -1, -1):
            r_min[i] = min(A[i], r_min[i+1])

        for i in range(1, len(A)):
            if l_max[i-1] <= r_min[i]:
                return i


        
# leetcode submit region end(Prohibit modification and deletion)
A = [5,0,3,8,6]
print(Solution().partitionDisjoint(A))