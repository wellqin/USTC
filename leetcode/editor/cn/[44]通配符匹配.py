# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
#
# 两个字符串完全匹配才算匹配成功。 
#
# 说明: 
#
# 
# s 可能为空，且只包含从 a-z 的小写字母。 
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。 
# 
#
# 示例 1: 
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2: 
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
#
# 示例 3: 
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
#
# 示例 4: 
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
#
# 示例 5: 
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
#


class Solution:
    def isMatch(self, s, p):
        s_len, p_len = len(s), len(p)
        i, j, star, i_index = 0, 0, -1, 0
        while i < s_len:
            if j < p_len and (p[j] == '?' or p[j] == s[i]):  # 判断i和j所指向的元素是不是相同，如果是的话我们i++;j++
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':  # j指向*，但i和j所指向的元素不相等
                star = j  # star记录下p中*的位置
                j += 1  # j++判断下一个位置
                i_index = i  # i_index记录下是s中此时i的位置
            elif star != -1:  # j既没有指向*，i和j所指向的元素又不相等
                # 这时要回过头来看*，我们此时是知道*的位置的，所以我们直接i++即可，也就是*此时匹配两次
                j = star + 1
                i_index += 1
                i = i_index
            else:
                return False

        # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])

    def isMatchDp(self, s, p):
        # dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp = [[0] * (len(p) + 1) for _ in range(len(s) + 1)]
        print(dp)
        dp[0][0] = 1  # 什么都没有,所以为true,第一列dp[i][0],当然全部为False(默认)
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]  # s为空,与p匹配,所以只要p开始为*才为true

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # dp[i - 1][j], 表示 * 代表是空字符, 例如ab, ab *
                    # dp[i][j - 1], 表示 * 代表非空任何字符（多个字符）, 例如abcd, ab *
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]



s = "adceb"
p = "*a*b"
print(Solution().isMatch(s, p))
print(Solution().isMatchDp(s, p))
