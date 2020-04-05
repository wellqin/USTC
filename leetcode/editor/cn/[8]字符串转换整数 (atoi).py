# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。 
#
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。 
#
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。 
#
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。 
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。 
#
# 说明： 
#
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，请返回 INT_MAX (231 − 1) 或 INT_MIN (−231) 。 
#
# 示例 1: 
#
# 输入: "42"
# 输出: 42
# 
#
# 示例 2: 
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 
#
# 示例 3: 
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 
#
# 示例 4: 
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#     因此无法执行有效的转换。 
#
# 示例 5: 
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。
# 
# Related Topics 数学 字符串


from typing import *
import re


# leetcode submit region begin(Prohibit modification and deletion)
# python3的int就是长整型，且没有大小限制，受限于内存区域的大小
class Solution1:
    def myAtoi(self, str):
        if not str:
            return 0

        res = 0
        i = 0
        # 第一步，跳过前面若干个空格
        string = str.lstrip()
        # 如果字符串全是空格直接返回
        if i == len(string):
            return 0

        # 第二步，判断正负号
        flag = True if string[i] == '-' else False

        # 如果是正负号，还需要将指针i，跳过一位
        if string[i] in ('-', '+'):
            i += 1
        # 第三步，循环判断字符是否在 0~9之间
        while i < len(string) and '0' <= string[i] <= '9':
            # '0'的ASCII码是48，'1'的是49，这么一减就从就可以得到真正的整数值
            tmp = ord(string[i]) - ord('0')  # 返回字符对应的 ASCII 数值

            # 判断是否大于 最大32位整数
            if not flag and (res > 214748364 or (res == 214748364 and tmp >= 7)):
                return 2147483647
            # 判断是否小于 最小32位整数
            if flag and (-res < -214748364 or (-res == -214748364 and tmp >= 8)):
                return -2147483648
            res = res * 10 + tmp
            i += 1
        # 如果有负号标记则返回负数
        return -res if flag else res

    def myAtoi1(self, s):
        """
        ^：匹配字符串开头
        [\+\-]：代表一个+字符或-字符
        ?：前面一个字符可有可无
        \d：一个数字
        +：前面一个字符的一个或多个
        \D：一个非数字字符
        *：前面一个字符的0个或多个
        max(min(数字, 2**31 - 1), -2**31) 用来防止结果越界

        为什么可以使用正则表达式？如果整数过大溢出怎么办？

        题目中描述： 假设我们的环境只能存储 32 位大小的有符号整数

        首先，这个假设对于 Python 不成立，Python 不存在 32 位的 int 类型。其次，即使搜索到的字符串转32位整数可能导致溢出，我们也可以直接通过字符串判断是否存在溢出的情况（比如 try 函数 或 判断字符串长度 + 字符串比较），聪明的你应该会解决这个问题吧？

        """
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


# leetcode submit region end(Prohibit modification and deletion)

class Solution(object):
    def myAtoi(self, str):
        string = str.strip()
        strNum = 0
        if len(string) == 0:
            return strNum

        flag = True
        if string[0] == '+' or string[0] == '-':
            if string[0] == '-':
                flag = False
            string = string[1:]

        for char in string:
            if '0' <= char <= '9':
                strNum = strNum * 10 + int(char)  # ord(char) - ord('0')
                print(ord(char), ord('0'))
                # 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值 ord('a') = 97
            if char < '0' or char > '9':
                break

        if strNum > 2147483647:
            return -2147483648 if not flag else 2147483647

        return -strNum if not flag else strNum


str = "4193 with words"
print(Solution().myAtoi(str))
print(ord('0'))  # 48
