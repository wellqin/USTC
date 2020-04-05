# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1: 
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
#
# 示例 2: 
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        lookup = {")": "("}
        stack = []
        flag = False
        if s == ")" or s == "))":
            return res
        while s.startswith(")") and len(s) >= 2:
            s = s[1:]
        for i in s:
            if stack and i in lookup:
                if lookup[i] == stack[-1]:
                    stack.pop()
                    res += 2

            else:
                stack.append(i)
        return res

    # 暴力[32]最长有效括号
    def longestValidParentheses1(self, s: str) -> int:
        maxnum = 0
        stack = [-1]  # 为了就是判断长度。因为符合条件的()都会相互抵消掉，不计入)的下标的话不知道抵消了多长的()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                if stack: maxnum = max(maxnum, i - stack[-1])
        return maxnum

    def longestValidParenthesesDp(self, s: str) -> int:
        maxans = 0
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[i] == ")":
                # 避免python负数的从后往前取值
                if i - 1 < 0:
                    continue
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                maxans = max(maxans, dp[i])
        return maxans


# leetcode submit region end(Prohibit modification and deletion)
s =  "())(())"
s1 = "()(()"  # 为2，不是4

print(Solution().longestValidParentheses1(s))
