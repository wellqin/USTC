#根据逆波兰表示法，求表达式的值。 
#
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。 
#
# 说明： 
#
# 
# 整数除法只保留整数部分。 
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。 
# 
#
# 示例 1： 
#
# 输入: ["2", "1", "+", "3", "*"]
#输出: 9
#解释: ((2 + 1) * 3) = 9
# 
#
# 示例 2： 
#
# 输入: ["4", "13", "5", "/", "+"]
#输出: 6
#解释: (4 + (13 / 5)) = 6
# 
#
# 示例 3： 
#
# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#输出: 22
#解释: 
#  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#= ((10 * (6 / (12 * -11))) + 17) + 5
#= ((10 * (6 / -132)) + 17) + 5
#= ((10 * 0) + 17) + 5
#= (0 + 17) + 5
#= 17 + 5
#= 22 
#

"""
实际上这里有一个很奇（sha）怪（bi）的地方，看到了么，除法➗处，如果我不这么做，就是错的，
这是python 2 和 python 3 的除法不一致导致的，所以最终我这样做了才能得到正确答案。
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l) / r))
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    # if l*r < 0 and l % r != 0:
                    #     stack.append(l/r+1)
                    # else:
                    #     stack.append(l/r)
        return stack.pop()
ll = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(ll))