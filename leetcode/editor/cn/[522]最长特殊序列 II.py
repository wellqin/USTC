#  给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
# 
#  子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。 
# 
#  输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。 
# 
#  
# 
#  示例： 
# 
#  输入: "aba", "cdc", "eae"
#  输出: 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  所有给定的字符串长度不会超过 10 。 
#  给定字符串列表的长度将在 [2, 50 ] 之间。 
#  
# 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution(object):
    def findLUSlength(self, strs):
        # front: 前面的单词
        # behind: 后面的单词
        def subseq(behind, front):
            # 判断后面单词是不是前面单词的子序列
            if behind == front:
                return True
            index = 0
            for i in front:
                if index < len(behind) and behind[index] == front[i]:
                    index += 1
            return index == len(behind)

        # Couter()、sorted()、all()、enumerate()需要同学们自己查询用法
        from collections import Counter
        count = Counter(strs)  # 给单词统计频数
        strs_1 = sorted(count.keys(), key=len, reverse=True)  # 按单词频数，从高到低排序
        # 得到的是排好序的单词列表

        for i, w in enumerate(strs_1):  # 该单词只出现一次
            if count[w] == 1 and all(not subseq(w, front) for front in strs_1[:i]):
                return len(w)  # all()该单词不是前面所有单词的子序列
        return -1

    def findLUSlength1(self, strs: List[str]) -> int:
        def is_sub(a, b):
            """判断a是否是b的子串"""
            i = j = 0
            al, bl = len(a), len(b)
            if bl < al:
                return False
            # al - i <= bl - j这个条件不满足时表示的是b已经不够长度匹配a了可以直接结束循环,再移位后得到下面这个条件,
            # 这样直接比较的是一个变量和常量的值,应该会更快点
            while i < al and j < bl:
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        # 统计字符串出现次数
        count = Counter(strs)
        # 将键即字符串按长度排序
        strs = sorted(count.keys(), key=len, reverse=True)

        for i, s in enumerate(strs):
            # 只判断出现1次的
            if count[s] == 1:
                for bs in strs[:i]:
                    if len(bs) == len(s):
                        return len(s)

                    if is_sub(s, bs):
                        break
                else:
                    return len(s)
        return -1

# leetcode submit region end(Prohibit modification and deletion)
str1 = ["ba", "cdc", "eae", "eae", "cdc"]
print(Solution().findLUSlength1(str1))
