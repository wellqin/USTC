#  给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
# 
#  示例 1: 
# 
#  输入: "aacecaaa"
#  输出: "aaacecaaa"
#  
# 
#  示例 2: 
# 
#  输入: "abcd"
#  输出: "dcbabcd"
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)


"""
解法二： 也可以翻转字符串，使用KMP做匹配，将剩余的串附加到翻转串的后面
输入: "aacecaaa"
逆序："aaacecaa"
利用KMP做匹配时：
 aacecaaa   # 原来串
aaacecaa    # 翻转串
将剩余的串附加到翻转串的后面：即a加到翻转串的后面，为：
aaacecaaa == aaacecaaa
"""

class Solution:
    """
    解法一：
    # 先逆序，然后截取逆序后的前i个字符拼接到原串上，取满足回文条件最小的i
    # 比较rs[i:len(s)]和s[0:len(s)-i]，当相同时，在s前面加上rs[0:i]
    """
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        rs = s[::-1]
        for i in range(len(s)):
            if s[:len(s) - i] == rs[i:]:
                return rs[:i] + s

    def shortestPalindromeBest(self, s: str) -> str:
        i = 0
        for j in range(len(s) - 1, -1, -1):
            if s[i] == s[j]:
                i += 1
        # 这里的i其实是一个上界
        # 解释: 如果存在j 使 shortestPalindrome = s[:j][::-1]+s
        # 那么, i 永远大于end-j
        # i==j 当且仅当 s是一个回文串
        # 且 i 永远大于 1
        if i == len(s):
            return s
        tmp = s[i:][::-1]
        return tmp + self.shortestPalindrome(s[:i]) + s[i:]
        
# leetcode submit region end(Prohibit modification and deletion)
