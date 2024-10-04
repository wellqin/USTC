# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例: 
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# Related Topics 字符串 回溯算法

"""
首先，我们s的长度必须在4到12之间才可以，不然这个ip不可能合法
然后再写一个check ip是否合法的函数
然后对于我们的s，选择三个位置插入3个'.'构造一个ip，合法的ip放入结果中
"""
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def __init__(self):
#         self.res = []
#         self.count = 0
#
#     def restoreIpAddresses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         if len(s) > 12 or len(s) < 4:
#             return []
#
#         def isValid(ip):
#             self.count += 1
#             if ip.count('.') != 3:
#                 return False
#             lst = ip.split('.')
#             for num in lst:
#                 if not num or int(num) > 255 or (len(num) > 1 and num[0] == '0'):
#                     return False
#             return True
#
#         def helper(cur, idx, cnt):
#             if cnt == 3:
#                 if isValid(cur):
#                     self.res.append(cur)
#                 return
#             if idx > len(cur) - 1:
#                 return
#             helper(cur[:idx] + '.' + cur[idx:], idx + 2, cnt + 1)
#             helper(cur, idx + 1, cnt)
#
#         helper(s, 0, 0)
#         return self.res, self.count
#
#
# # leetcode submit region end(Prohibit modification and deletion)
# s = "25525511135"
# print(Solution().restoreIpAddresses(s))


# 暴力法
class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        # 判读是否满足ip的条件
        def helper(tmp):
            if not tmp or (tmp[0] == "0" and len(tmp) > 1) or int(tmp) > 255:
                return False
            return True

        # 三个循环,把数字分成四份
        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if i < n and j < n and k < n:
                        tmp1 = s[:i + 1]
                        tmp2 = s[i + 1:j + 1]
                        tmp3 = s[j + 1:k + 1]
                        tmp4 = s[k + 1:]
                        print(i, j, k)
                        # print(tmp1, tmp2, tmp3, tmp4)
                        # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res


s = "25525511135"
print(Solution1().restoreIpAddresses(s))
# 回溯法
"""
这个其实也是划分，划分的次数已经确定了，那就是分为 4 部分。那么就直接用回溯的思想，
第一部分可能是 1 位数，然后进入递归。第一部分可能是 2 位数，然后进入递归。第一部分可能是 3 位数，然后进入递归。
很好理解，直接看代码理解吧。

"""


class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        回溯两个点：
        1.首先边界条件：ip的四个部分凑齐了
        2.其次：考虑每个部分必须0~255之间，同时第一位必须大于0除非整个该部分为0
        """

        def traceback(num: int, temp: str, s: str):
            if num == 4 and not s:
                res.append(temp[:-1])
                return
            for i in range(1, 4):
                if i <= len(s) and int(s[:i]) <= 255 and (s[0] > '0' or s[:i] == '0'):
                    traceback(num + 1, temp + s[:i] + '.', s[i:] if i < len(s) else "")

        res = []
        if len(s) <= 12:
            traceback(0, "", s)
        else:
            return []

        return res

    # 递归
    def restoreIpAddresses1(self, s: str) -> List[str]:
        """
        首先只能分成四份，所以记录一下n,如果n=4并且s为空，那么是符合条件的。
        其次在递归的时候判断一下是不是范围，是不是为0-255之间，如果不是，不进行递归
        """
        ans = []

        def findIp(s, pre, n):
            if not s and n == 4:
                ans.append(".".join(str(i) for i in pre))
                return
            if n == 4 and s:
                return
            if s and s[0] == "0":
                findIp(s[1:], pre + [s[:1]], n + 1)
            else:
                for i in range(min(len(s), 3)):
                    if s[:i + 1] and 0 <= int(s[:i + 1]) < 256:
                        findIp(s[i + 1:], pre + [s[:i + 1]], n + 1)

        findIp(s, [], 0)
        return ans

    def restoreIpAddresses2(self, s: str) -> List[str]:
        def backtrack(string, temp, count):
            if count == 0 and len(string) != 0:
                return
            if count == 0 and len(string) == 0:
                res.append(temp[1:])
            else:
                if not string:
                    return
                if string[0] == '0':
                    backtrack(string[1:], temp + ('.' + string[:1]), count - 1)
                else:
                    for i in range(1, len(string) + 1):
                        if 0 <= int(string[:i]) <= 255:
                            backtrack(string[i:], temp + ('.' + string[:i]), count - 1)
                        else:
                            break

        res = []
        backtrack(s, '', 4)
        return res

    def restoreIpAddresses3(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res


s1 = "25525511135"
print(Solution2().restoreIpAddresses(s1))
print(Solution2().restoreIpAddresses1(s1))
print(Solution2().restoreIpAddresses2(s1))
print(Solution2().restoreIpAddresses3(s1))
