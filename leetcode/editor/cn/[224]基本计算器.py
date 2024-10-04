# 实现一个基本的计算器来计算一个简单的字符串表达式的值。 
# 
#  字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格 。 
# 
#  示例 1: 
# 
#  输入: "1 + 1"
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: " 2-1 + 2 "
# 输出: 3 
# 
#  示例 3: 
# 
#  输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23 
# 
#  说明： 
# 
#  
#  你可以假设所给定的表达式都是有效的。 
#  请不要使用内置的库函数 eval。 
#  
#  Related Topics 栈 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        栈和不反转字符串
        思路：遇到"("，就把之前的操作符和result进栈，然后对"()"中的表达式进行计算；
             遇到")"，就把操作符和原result出栈
        """
        stack = []  # 保存括号状态
        operator = 1  # 加减操作符
        res = 0  # 结果
        num = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(res)  # 把“(”前的结果和操作符保存起来
                stack.append(operator)
                res = 0
                operator = 1
                num = 0

            elif s[i] == ')':
                res = res + num * operator  # 此处res是()中计算的结果
                operator = stack.pop()
                res = stack.pop() + res * operator  # 将之前的结果与现在汇总
                num = 0
                operator = 1

            elif s[i] == '+':
                res = res + num * operator
                num = 0
                operator = 1
            elif s[i] == '-':
                res = res + num * operator
                num = 0
                operator = -1

            elif s[i] != ' ':
                num = num * 10 + int(s[i])
        res = res + num * operator
        return res


# leetcode submit region end(Prohibit modification and deletion)
s = "(1+(4+5+2)-3)+(6+8)"
print(Solution().calculate(s))
