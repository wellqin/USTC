#编写一个函数来查找字符串数组中的最长公共前缀。 
#
# 如果不存在公共前缀，返回空字符串 ""。 
#
# 示例 1: 
#
# 输入: ["flower","flow","flight"]
#输出: "fl"
# 
#
# 示例 2: 
#
# 输入: ["dog","racecar","car"]
#输出: ""
#解释: 输入不存在公共前缀。
# 
#
# 说明: 
#
# 所有输入只包含小写字母 a-z 。 
#
import os

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        dp = [strs[0]] * len(strs)
        for i in range(1, len(strs)):
            while not strs[i].startswith(dp[i-1]):
                dp[i-1] = dp[i-1][:-1]
            dp[i] = dp[i-1]
        return dp[-1]

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)
ll = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(ll))
print(Solution().longestCommonPrefix1(ll))
print(Solution().longestCommonPrefix2(ll))
