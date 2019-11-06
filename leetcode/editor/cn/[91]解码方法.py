#一条包含字母 A-Z 的消息通过以下方式进行了编码： 
#
# 'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
# 
#
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。 
#
# 示例 1: 
#
# 输入: "12"
#输出: 2
#解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
#
# 示例 2: 
#
# 输入: "226"
#输出: 3
#解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# Related Topics 字符串 动态规划

"""
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(N)******

dp[i]代表s[:i]可以有几种解码方式

例：

s=        "1221"
index      0123


dp[0] = 1  [[1]]
dp[1] = 2  [[1,2], [12]]

判断 dp[i] 时，它有两种可能的组合方式：
1. 自身解码
    - 如果当前字符不是'0'，那么dp[i]的组合可以为dp[i-1]的所有组合方式后面都加上当前字符
    - 如果当前字符是'0'，那么dp[i]在这种情况下没有符合的组合方式
2. 和它前面的一个字符一起解码
    - 如果10 <= int(s[i-1:i+1]) <= 26, 那么dp[i]的组合可以为dp[i-2]的所有组合方式后面都加上s[i-1:i+1]
    - 如果int(s[i-1:i+1]) < 10 或者 int(s[i-1:i+1]) > 26，那么dp[i]在这种情况下没有符合的组合方式

dp[2] = 3  [[1,2,2], [12,2], [1,22]]
dp[3] = 5  [[1,2,2,1], [12,2,2], [1,22,2], [1,2,21], [12,21]]


注意 dp[0] 与 dp[1] 的处理，
"""



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '0':
            return 0
        elif len(s) == 1 and s[0] != '0':
            return 1

        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '0' else 0

        if 10 <= int(s[:2]) <= 26:
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = dp[0]
        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
        
#leetcode submit region end(Prohibit modification and deletion)
