# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        right = 0
        match = 0
        window = {}
        needs = dict((i, p.count(i)) for i in p)

        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left == len(p):  # 找到 s 中所有是 p 的字母异位词的子串，注意是所有，所以== len(p)
                    res.append(left)
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
S = "cbaebabacd"
T = "abc"
print(Solution().findAnagrams(S, T))
