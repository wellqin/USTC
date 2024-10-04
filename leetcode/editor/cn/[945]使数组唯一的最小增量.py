# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。 
# 
#  返回使 A 中的每个值都是唯一的最少操作次数。 
# 
#  示例 1: 
# 
#  输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。 
# 
#  示例 2: 
# 
#  输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 40000 
#  0 <= A[i] < 40000 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        # 将（一般）单调序列变为严格单调序列

        if not A or len(A) == 1:
            return 0
        A.sort()  # [1,1,2,2,3,7]
        ans = 0
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:  # 已经严格单调不处理
                continue
            else:
                ans += A[i - 1] + 1 - A[i]  # 后者比前者大1需要的操作次数
                A[i] = A[i - 1] + 1  # 否则，后者比前者大1即可
        return ans

    def minIncrementForUnique1(self, A):
        count = collections.Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans


# leetcode submit region end(Prohibit modification and deletion)
A = [3, 2, 1, 2, 1, 7]  # [1,1,2,2,3,7]
print(Solution().minIncrementForUnique1(A))
