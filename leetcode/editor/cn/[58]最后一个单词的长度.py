#给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。 
#
# 如果不存在最后一个单词，请返回 0 。 
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。 
#
# 示例: 
#
# 输入: "Hello World"
#输出: 5
# 
#
from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s1 = s.split()
        return len(s1[-1])

    def lengthOfLastWord1(self, s):
        s = s[::-1].strip()
        return s.find(' ') if s.find(' ') != -1 else len(s)

    def lengthOfLastWord2(self, s):
        lst = s.split()
        if len(lst) >= 1:
            return len(lst[-1])
        return 0

    def lengthOfLastWord3(self, s):
        return len(s.strip().split(" ")[-1])


s = "Hello World"
print(Solution().lengthOfLastWord(s))
print(Solution().lengthOfLastWord1(s))
print(Solution().lengthOfLastWord2(s))
print(Solution().lengthOfLastWord3(s))

ss = "a"
print(ss.split())
