# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1: 
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
#
# 示例 2: 
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
#
# 示例 3: 
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
#
from typing import *


class Solution:
    def lengthOfLongestSubstringSelf(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        lookup = []
        cur, res = 0, 0
        for i in range(n):
            if s[i] not in lookup:
                lookup.append(s[i])
                cur += 1
            else:  # [a, b, c, a]
                index = lookup.index(s[i])  # 找出重复字符的下标 [a, b, c]
                lookup = lookup[index + 1:]  # 滑动窗口删除旧重复字符[b, c]
                lookup.append(s[i])  # 增加新字符[b, c, a]
                cur = len(lookup)  # 更新长度
            if cur > res:
                res = cur
        return res

    def minWindow(self, s):
        right = 0
        res = 0
        left = 0
        window = {}

        while right < len(s):
            c1 = s[right]
            window[c1] = window.get(c1, 0) + 1
            right += 1
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1
            res = max(res, right - left)
        return res

    # 大佬解法
    def lengthOfLongestSubstring(self, s):
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


s = "abcabcbb"
s1 = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
