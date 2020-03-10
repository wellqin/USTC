# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。 
# 
#  在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，而当 i >= 0 时 
# C[i+A.length] = C[i]） 
# 
#  此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, 
# k2 <= j 其中 k1 % A.length = k2 % A.length） 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#  
# 
#  示例 2： 
# 
#  输入：[5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#  
# 
#  示例 3： 
# 
#  输入：[3,-1,2,-1]
# 输出：4
# 解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
#  
# 
#  示例 4： 
# 
#  输入：[3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#  
# 
#  示例 5： 
# 
#  输入：[-2,-3,-1]
# 输出：-1
# 解释：从子数组 [-1] 得到最大和 -1
#  
# 
#  
# 
#  提示： 
# 
#  
#  -30000 <= A[i] <= 30000 
#  1 <= A.length <= 30000 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # 数组拼接+控制长度
        if not A:
            return 0
        dp = [A[0] for _ in range(2 * len(A))]
        nusm = A + A
        queue = len(A)
        for i in range(1, len(nusm)):
            dp[i] = max(dp[i - 1] + nusm[i], nusm[i])

        return max(dp)

    def maxSubarraySumCircular1(self, A: List[int]) -> int:
        l = len(A)
        A = A + A
        ans = A[0]
        s = [0] * (2 * l)
        q = [0]
        for i in range(1, 2 * l):
            s[i] = s[i - 1] + A[i - 1]
            while q and q[0] < i - l:
                q.pop(0)
            ans = max(ans, s[i] - s[q[0]])
            while q and s[q[-1]] > s[i]:
                q.pop()
            q.append(i)
        return ans

    def maxSubarraySumCircular2(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]

        # DP求连续子数组最大和
        ans = sum(A)
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        ans = max(dp[0], ans)
        for i in range(1, len(A)):
            dp[i] = dp[i - 1] + A[i] if dp[i - 1] > 0 else A[i]
            ans = max(dp[i], ans)

        # DP求连续子数组最小和
        dp = [0 for _ in range(len(A))]
        dp[0] = A[0]
        total = sum(A)
        ans = max(total - dp[0], ans)
        for i in range(1, len(A) - 1):
            dp[i] = dp[i - 1] + A[i] if dp[i - 1] < 0 else A[i]
            ans = max(total - dp[i], ans)

        # DP没法判断以最后一个数字结尾的最小连续子数组和是不是把所有元素全部选完了， 所以单独处理
        val = 0
        for i in range(len(A) - 1, 0, -1):
            val += A[i]
            ans = max(ans, total - val)

        return ans

    def maxSubarraySumCircular3(self, A: List[int]) -> int:
        ans = cur = fans = fcur = 0
        for i in A:
            cur = i + max(cur, 0)
            ans = max(ans, cur)  # 不跨边界
            fcur = i + min(fcur, 0)
            fans = min(fans, fcur)  # 最小子数组和
        return max(ans, sum(A) - fans) if ans else max(A)
        # sum(A) - fans可得到跨越边界情况下的子数组最大和
        # if ans else max(A)考虑全负数，全负数时，ans为负值，小于初始值
        # 此时ans最大值也为负数，但是却是默认值，这不合理


# leetcode submit region end(Prohibit modification and deletion)
A = [5, -3, 5]
print(Solution().maxSubarraySumCircular1(A))
