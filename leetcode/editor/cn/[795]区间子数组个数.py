# 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。 
# 
#  求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。 
# 
#  例如 :
# 输入: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# 输出: 3
# 解释: 满足条件的子数组: [2], [2, 1], [3].
#  
# 
#  注意: 
# 
#  
#  L, R 和 A[i] 都是整数，范围在 [0, 10^9]。 
#  数组 A 的长度范围在[1, 50000]。 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numSubarrayBoundedMax0(self, A: List[int], L: int, R: int) -> int:
        if not A or not L or not R:
            return 0
        nums = []
        res = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                nums.append(A[i:j + 1])
        for i in nums:
            if L <= max(i) <= R:
                res += 1
        return res

    def numSubarrayBoundedMax1(self, A: List[int], L: int, R: int) -> int:
        if not A or not L or not R:
            return 0
        pos1 = 0
        pos2 = 0

        for i in range(len(A)):
            if L <= A[i] <= R:
                pos1 += 1
            elif L > A[i]:
                pos1 += 1
            elif A[i] > R:
                pos2 = i
        pass

    def numSubarrayBoundedMax(self, A, L, R):
        def count(bound):
            ans = cur = 0
            for x in A:
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)


A = [2, 1, 4, 3]
L = 2
R = 3
print(Solution().numSubarrayBoundedMax(A, L, R))

# leetcode submit region end(Prohibit modification and deletion)
