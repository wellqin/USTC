# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为： 
#
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
# 
# Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        elif n == 2:
            return ["()()", "(())"]
        result = []
        for i in range(n):  # 动态规划思想dp[i] = "(" + dp[j] + ")" + dp[i- j - 1]
            j = n - 1 - i   # j为剩下的括号对数，i为可能的括号对数 i+j=n-1
            temp1 = self.generateParenthesis(i)
            temp2 = self.generateParenthesis(j)
            result.extend(["(%s)%s" % (p, q) for p in temp1 for q in temp2])
        return result
    # result = ['()()()', '()(())', '(())()', '(()())', '((()))']

    def generateParenthesisDfs(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res

    def generateParenthesisDp(self, n: int) -> List[str]:
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):  # dp[i] = "(" + dp[j] + ")" + dp[i- j - 1]
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]
    # [[''], ['()'], ['()()', '(())'], ['()()()', '()(())', '(())()', '(()())', '((()))']]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().generateParenthesis(3))
