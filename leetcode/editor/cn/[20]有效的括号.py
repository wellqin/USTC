# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足： 
#
# 
# 左括号必须用相同类型的右括号闭合。 
# 左括号必须以正确的顺序闭合。 
# 
#
# 注意空字符串可被认为是有效字符串。 
#
# 示例 1: 
#
# 输入: "()"
# 输出: true
# 
#
# 示例 2: 
#
# 输入: "()[]{}"
# 输出: true
# 
#
# 示例 3: 
#
# 输入: "(]"
# 输出: false
# 
#
# 示例 4: 
#
# 输入: "([)]"
# 输出: false
# 
#
# 示例 5: 
#
# 输入: "{[]}"
# 输出: true
#

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
            print(s)
        return len(s) == 0

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = '([{'
        rightP = ')]}'
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []

    def isValidSelf1(self, s):
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = []  # 栈里面只保存待匹配的左括号
        for i in s:
            if stack and i in lookup:  # 如果栈不为空 同时 当前的为右括号
                if stack[-1] == lookup[i]:  # 如果栈中存在与右括号匹配的左括号
                    stack.pop()  # 则匹配到最小括号对，栈中进行删除
            else:
                stack.append(i)
        return not stack

    def isValid22(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack



s = "{()[()]}"
print(Solution().isValidSelf1(s))
