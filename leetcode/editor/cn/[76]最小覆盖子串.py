# 给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
#
# 示例： 
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
#
# 说明： 
#
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。 
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。 
# 
#


"""
滑动窗口算法的思路是这样：
1、我们在字符串 S 中使用双指针中的左右指针技巧，初始化 left = right = 0，把索引闭区间 [left, right] 称为一个「窗口」。
2、我们先不断地增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
3、此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串不再符合要求
  （不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果。
4、重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头。

这个思路其实也不难，第 2 步相当于在寻找一个「可行解」，然后第 3 步在优化这个「可行解」，最终找到最优解。
左右指针轮流前进，窗口大小增增减减，窗口不断向右滑动。

一个哈希表 needs 记录字符串 t 中包含的字符及出现次数，用另一个哈希表 window 记录当前「窗口」中包含的字符及出现的次数，
如果 window 包含所有 needs 中的键，且这些键对应的值都大于等于 needs 中的值，那么就可以知道当前「窗口」符合要求了，
可以开始移动 left 指针了

"""


class Solution:
    # def minWindow1(self, s: str, t: str) -> str:
    #     N = len(s)
    #     left = 0
    #     res = ''
    #     min_val = N
    #     match = 0
    #     needs = {}  # 最小子串需要哪些元素，即将T中元素进行统计
    #     windows = {}  # 维持needs中元素的窗口
    #
    #     for i in t:
    #         needs[i] = needs.get(i, 0) + 1  # dict((i, p.count(i)) for i in p)
    #
    #     match_N = len(needs)
    #
    #     for right in range(N):
    #         if s[right] in needs:
    #             windows[s[right]] = windows.get(s[right], 0) + 1
    #             if windows[s[right]] == needs[s[right]]:
    #                 match += 1
    #             while match == match_N:  # 当windows中包含了needs中的所有元素，windows可能有重复的
    #                 # 此while循环，直到窗口中的字符串不再符合要求，left 不再继续移动
    #                 this_time_val = right - left
    #                 if this_time_val < min_val:  # 每次找到比min_val更小的this_time_val区间时，更新区间
    #                     res = s[left:right + 1]
    #                     min_val = this_time_val
    #
    #                 if s[left] in needs:
    #                     windows[s[left]] = windows[s[left]] - 1  # 去除边界的重复值
    #                     if windows[s[left]] < needs[s[left]]:  # 如果去重复值后，窗口中的字符串不再符合要求，则match自减，while结束
    #                         match -= 1
    #                 left += 1
    #     return res

    def minWindow(self, s: str, t: str) -> str:
        start = 0
        minLen = float('inf')  # 不会超过
        left = 0  # 等右指针所在的位置之前的字符串包含t以后，左指针开始移动
        right = 0  # 右指针
        window = {}
        needs = dict((i, t.count(i)) for i in t)
        match = 0

        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):  # # 当windows中包含了needs中的所有元素，windows可能有重复的
                # 此while循环，直到窗口中的字符串不再符合要求，left 不再继续移动
                if right - left < minLen:  # 每次找到比minLen更小的区间时，更新区间
                    start = left
                    minLen = right - left
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1  # 去除边界的重复值
                    if window[c2] < needs[c2]:  # 如果去重复值后，窗口中的字符串不再符合要求，则match自减，内部while结束
                        match -= 1
                left += 1
        return '' if minLen == float('inf') else s[start:start + minLen]


# S = "ABBECODEBANC"
# T = "ABC"
# print(Solution().minWindow(S, T))
