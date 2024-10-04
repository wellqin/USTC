#给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。 
#
# 示例 1: 
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#输出: true
# 
#
# 示例 2: 
#
# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#输出: false 
# Related Topics 字符串 动态规划



#leetcode submit region begin(Prohibit modification and deletion)
# 递归+双指针, 超时===>加个cache就可以了
from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache(None)
        def helper(i, j):
            if i == len(s1) and j == len(s2):
                return True
            res = False
            if i < len(s1) and s1[i] == s3[i+j]:
                res = helper(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                res = helper(i, j+1)
            return res
        return helper(0, 0)
        
#leetcode submit region end(Prohibit modification and deletion)
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(Solution().isInterleave(s1, s2, s3))

"""
思路 2 - 时间复杂度: O(m * n)- 空间复杂度: O(m * n)******

dp[i][j]代表s1的前i个字符和s2的前j个字符合起来是否能够组成s3的前i+j个字符

自底向上动态方程:

用dp[i][j]表示s1的前i元素和s2前j元素是否交错组成s3前i+j元素

所以有动态方程:
dp[i][j] = (dp[i-1][j] && s3[i+j-1] == s1[i-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1])

注意:针对第一行,第一列要单独考虑

"""
class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:  # 前面都不符合了，后面肯定不符合了
                break
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
        return dp[-1][-1]

print(Solution1().isInterleave(s1, s2, s3))
