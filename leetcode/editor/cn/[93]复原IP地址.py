#给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
#
# 示例: 
#
# 输入: "25525511135"
#输出: ["255.255.11.135", "255.255.111.35"] 
# Related Topics 字符串 回溯算法

"""
首先，我们s的长度必须在4到12之间才可以，不然这个ip不可能合法

然后再写一个check ip是否合法的函数

然后对于我们的s，选择三个位置插入3个'.'构造一个ip，合法的ip放入结果中
"""
from typing import *
#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12 or len(s) < 4:
            return []
        self.count = 0
        def isValid(ip):
            self.count += 1
            if ip.count('.') != 3:
                return False
            lst = ip.split('.')
            for num in lst:
                if not num or int(num) > 255 or (len(num) > 1 and num[0] == '0'):
                    return False
            return True

        self.res = []

        def helper(cur, idx, cnt):
            if cnt == 3:
                if isValid(cur):
                    self.res.append(cur)
                return
            if idx > len(cur) - 1:
                return
            helper(cur[:idx] + '.' + cur[idx:], idx + 2, cnt + 1)
            helper(cur, idx + 1, cnt)

        helper(s, 0, 0)
        return self.res, self.count
        
#leetcode submit region end(Prohibit modification and deletion)
s = "25525511135"
print(Solution().restoreIpAddresses(s))


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
                        print(tmp1, tmp2, tmp3, tmp4)
                        # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
                        if all(map(helper, [tmp1, tmp2, tmp3, tmp4])):
                            res.append(tmp1 + "." + tmp2 + "." + tmp3 + "." + tmp4)
        return res
print(Solution1().restoreIpAddresses(s))
# 回溯法
"""
这个其实也是划分，划分的次数已经确定了，那就是分为 4 部分。那么就直接用回溯的思想，
第一部分可能是 1 位数，然后进入递归。第一部分可能是 2 位数，然后进入递归。第一部分可能是 3 位数，然后进入递归。
很好理解，直接看代码理解吧。

"""
class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
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

    def restoreIpAddresses1(self, s: str) -> List[str]:
        if not s:
            return []

        def restore(s, remain):  # 从s里恢复几个ip段
            if remain == 1:  # 结束条件，仅当剩的数在[0,255]且不存在'01','022'这种情况时返回
                if -1 < int(s) < 256 and str(int(s)) == s:
                    return [s]
                return []  # 否则返回空
            res = []
            if remain <= len(s) <= 3 * remain - 2:
                # 除掉1位后剩余至少remain-1个字符，至多3*(remain-1)个字符
                for i in restore(s[1:], remain - 1):
                    res.append(s[:1] + '.' + i)
            if int(s[:2]) > 9 and remain + 1 <= len(s) <= 3 * remain - 1:
                # 除掉2位（真正的两位数）后剩余至少remain-1个字符，至多3*(remain-1)个字符
                for i in restore(s[2:], remain - 1):
                    res.append(s[:2] + '.' + i)
            if 99 < int(s[:3]) < 256 and remain + 2 <= len(s) <= 3 * remain:
                # 除掉3位（真正的三位数）后剩余至少remain-1个字符，至多3*(remain-1)个字符
                for i in restore(s[3:], remain - 1):
                    res.append(s[:3] + '.' + i)
            return res

        return restore(s, 4)


print(Solution2().restoreIpAddresses(s))
print(Solution2().restoreIpAddresses1(s))



# class RestoreIpAddress(object):
#
#     def __init__(self, s):
#         """
#         output为最终符合要求的列表
#         segments为存储符合要求的截取部分的列表
#         """
#         self._s = s
#         self.length = len(s)
#         self.output, self.segments = [], []
#
#     def is_valid(self, segment):
#         """
#         1. 截取的部分的整数必须小于或者等于255
#         2. 截取部分除非是0否则不可以以0开头
#         3. 返回bool
#         """
#         return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
#
#     def update_output(self, curr_pos):
#         """
#         :param curr_pos:
#         :return:
#         """
#         # 最后一个点放置完成后，针对剩余截取部分是curr_pos+1开始
#         segment = self._s[curr_pos + 1:self.length]
#         # 判断最后剩余部分是否符合
#         if self.is_valid(segment):
#             self.segments.append(segment)
#             print(self.segments)
#             self.output.append(".".join(self.segments))
#             # 将最后部分删除，然后移动curr_pos，这里需要很好的理解递归
#             self.segments.pop()
#         # 最后一部分验证不合格，则最为一种递归出口
#
#     def backtrack(self, pre_pos=-1, dots=3):
#         """
#         1. 有限制条件可知，'.'符号不可以放在头部或尾部之后或者距离上一个'.'三个字符以上，
#         所以range(pre_pos + 1, min(self.length - 1, pre_pos + 4))
#
#         """
#         for curr_pos in range(pre_pos + 1, min(self.length - 1, pre_pos + 4)):
#             segment = self._s[pre_pos + 1:curr_pos + 1]
#             if self.is_valid(segment):
#                 self.segments.append(segment)
#                 # 这个点为最后一个点则判断是output否可以更新
#                 if dots - 1 == 0:
#                     self.update_output(curr_pos)
#                 else:
#                     # 递归，尝试放入下一个"."
#                     self.backtrack(curr_pos, dots - 1)
#                 # 1. 当update_output中最后一部分验证失败时，回溯时删除截取的部分
#                 # 2. 在backtrack中验证失败，回溯时，删除截取的部分
#                 self.segments.pop()
#
#     def result(self):
#         self.backtrack()
#         return self.output
