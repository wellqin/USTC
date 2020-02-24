# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
#
# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是） 
#
# 示例 1: 
#
# 输入: S = "rabbbit", T = "rabbit"
# 输出: 3
# 解释:
#
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
#
# 示例 2: 
#
# 输入: S = "babgbag", T = "bag"
# 输出: 5
# 解释:
#
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
# Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @staticmethod
    def numDistinct0(s: str, t: str) -> int:
        """
        进阶：空间复杂度 O(N×M) -> O(N)。
        思路：先想办法降维，再减少重复计算
        """
        # 预处理
        # 48ms
        set_t = set(t)
        string = ''
        for i in s:
            if i in set_t:
                string += i
        lens, lent = len(string), len(t)
        dp = [1] + [0] * lent
        for i in range(lens):
            for j in range(lent - 1, -1, -1):
                if string[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]

    @staticmethod
    def numDistinct1(self, s: str, t: str) -> int:
        # 逆序，俩行变一行
        # 76ms
        lens, lent = len(s), len(t)
        dp = [1] + [0] * lent
        for i in range(lens):
            for j in range(lent - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]

    @staticmethod
    def numDistinct2(self, s: str, t: str) -> int:
        # 每次迭代时，dp矩阵中真正能用到的只有俩行。
        # 124ms
        lens, lent = len(s), len(t)
        dp = [[1] * (lens + 1), [0] * (lens + 1)]
        for i in range(lent):
            for j in range(lens):
                if t[i] == s[j]:
                    dp[1][j + 1] = dp[0][j] + dp[1][j]
                else:
                    dp[1][j + 1] = dp[1][j]
            dp[0] = dp[1]
            dp[1] = [0] * (lens + 1)
        return dp[0][-1]

    @staticmethod
    def numDistinct(self, s: str, t: str) -> int:
        # 180ms
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)
