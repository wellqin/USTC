# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。 
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。 
#
# 示例 1: 
# s = "abc", t = "ahbgdc"
#
# 返回 true. 
#
# 示例 2: 
# s = "axc", t = "ahbgdc"
#
# 返回 false. 
#
# 后续挑战 : 
#
# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？ 
#
# 致谢: 
#
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。 
#
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 判断 s 是否为 t 的子序列
        if not s:
            return True
        if not t:
            return False
        if s == t:
            return True
        # dp创建是如果s, t位置调换则出错
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1] == len(s)

    def isSubsequence1(self, s, t):
        if not s:
            return True
        if not t:
            return False
        if s == t:
            return True
        s = list(s)
        t = list(t)
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        res = 0
        while i < m and j < n:
            if s[i] == t[j]:
                res += 1
                i += 1
            j += 1
        return res == m

    def isSubsequence2(self, s, t):
        # 判断 s 是否为 t 的子序列。
        if not s:
            return True
        for i in s:
            res = t.find(i)
            if res == -1:
                return False
            else:
                t = t[res + 1:]
        return True


s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
print(Solution().isSubsequence1(s, t))
print(Solution().isSubsequence2(s, t))
