# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        括号匹配
Description :   
Author :          wellqin
date:             2020/3/24
Change Activity:  2020/3/24

1. 给定一个只包括 '('，')'的字符串，判断字符串是否有效。
    思路：遇到 "(" 就让它入栈，遇到 ")" 就判断下栈里面有没有 "("
    （1）如果有，则把处于栈顶的 "("  弹出，相当于和 ")" 进行匹配，然后继续往后遍历字符串
    （2）如果没有，则匹配失败。相当于字符串的最前面出现了 ")"，显然这是不合理的。

2. LT20：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效
-------------------------------------------------
"""

class Solution:
    def isValid(self, s):
        # 时间，空间复杂度是 O(n)
        if not s:
            return True
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return stack == []

    def isValid1(self, s):
        # 时间O(n)，空间O(1)
        # 由于我们栈里面存放的都是**同一种字符 **"(" ，其实我们可以用一个变量来取代栈的，
        # 这个变量就记录 "(" 的个数，遇到 "(" 变量就加 1，遇到 ")" 变量就减 1，栈为空就相当于变量的值为 0。
        if not s:
            return True
        total = 0
        for i in s:
            if i == "(":
                total += 1
            else:
                if total == 0:
                    return False
                else:
                    total -= 1
        return total == 0

    # --------------------------------------------------------------------------------
    # 2. LT20：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效
    # --------------------------------------------------------------------------------
    def isValidMu(self, s):
        # 1. 取巧方法，直接消除有效的括号直到为空，不为空则存在无效
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
        return len(s) == 0

    def isValidMu1(self, s):
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
                # 与栈中元素进行匹配，匹配不上则为False
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []

    def isValidSelfMu2(self, s):
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = []  # 栈里面只保存待匹配的左括号
        for i in s:
            if stack and i in lookup:  # 如果栈不为空 同时 当前的为右括号
                if stack[-1] == lookup[i]:  # 如果栈中存在与右括号匹配的左括号
                    stack.pop()  # 则匹配到最小括号对，栈中进行删除
            else:
                stack.append(i)
        return not stack

s = "(()))"
print(Solution().isValid1(s))