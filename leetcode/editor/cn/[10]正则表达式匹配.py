# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
#
# 说明: 
#
# 
# s 可能为空，且只包含从 a-z 的小写字母。 
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
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
#
# 示例 2: 
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
#
# 示例 3: 
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
#
# 示例 4: 
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
#
# 示例 5: 
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# Related Topics 字符串 动态规划 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s and len(p) == 1: return False

        nrow = len(s) + 1
        ncol = len(p) + 1
        # dp[i][j] 表示 s 的前 i 个是否能被 p 的前 j 个匹配
        dp = [[False for _ in range(ncol)] for _ in range(nrow)]

        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for r in range(1, nrow):
            i = r - 1
            for c in range(1, ncol):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False

        return dp[nrow - 1][ncol - 1]

    def isMatch1(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False
        # dp[i][j]表示 s 的前 i 个是否能被 p 的前 j 个匹配
        # 注意初始化长度要到 len(str) + 1
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # [0, 0] 代表空串，两空串必定匹配
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if i - 2 >= 0 and p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # 当前s == p，或p为.时匹配成功，状态为 True && dp[i-1][j-1]
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # 当前p为*，需要往前看
                if p[j - 1] == '*':
                    if j - 2 >= 0:
                        # 如果*前面一个p和s匹配了, 有3种情况
                        # 1. 当前模式继续匹配前一个s，dp[i-1][j]
                        # 2. 进入下一个模式，dp[i-1][j-2]
                        # 3. 忽略当前模式，因为s可能会与后面的模式匹配，dp[i][j-2]
                        if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 2] or dp[i][j - 2]
                        # 没有匹配，需要看是不是忽略*这个模式的情况
                        else:
                            dp[i][j] = dp[i][j - 2]
        return dp[len(s)][len(p)]


# leetcode submit region end(Prohibit modification and deletion)
