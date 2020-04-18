# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.原理
Description :   
Author :          wellqin
date:             2020/4/16
Change Activity:  2020/4/16
-------------------------------------------------

递归是一种解决问题的有效方法，在递归过程中，函数将自身作为子例程调用

你可能想知道如何实现调用自身的函数。
诀窍在于，每当递归函数调用自身时，它都会将给定的问题拆解为子问题。递归调用继续进行，直到到子问题无需进一步递归就可以解决的地步。

为了确保递归函数不会导致无限循环，它应具有以下属性：
    一个简单的基本案例（basic case）（或一些案例） —— 能够不使用递归来产生答案的终止方案。
    一组规则，也称作递推关系（recurrence relation），可将所有其他情况拆分到基本案例。

注意，函数可能会有多个位置进行自我调用。
"""

# 从一个简单编程问题开始：以相反的顺序打印字符串
from typing import List

"""
首先，我们可以将所需的函数定义为 printReverse(str[0...n-1])，其中 str[0] 表示字符串中的第一个字符。然后我们可以分两步完成给定的任务：
    printReverse(str[1...n-1])：以相反的顺序打印子字符串 str[1...n-1] 。
    print(str[0])：打印字符串中的第一个字符。

请注意，我们在第一步中调用函数本身，根据定义，它使函数递归。
"""


class Solution:
    def __init__(self):
        self.num = []

    def reverseStr(self, strList: str) -> str:
        if not strList or len(strList) == 1:  # 1.终止条件
            return strList
        stre = self.reverseStr(strList[1:])  # 2.递归形式
        """
        (stre, strList)
        8 78
        87 678
        876 5678
        8765 45678
        87654 345678
        876543 2345678
        8765432 12345678
        87654321
        """
        return stre + strList[0]  # 返回值
        # return "" if not strList or len(strList) == 0 else reverseStr(strList[1:]) + strList[0]

    def reverseStrList(self, strList: list) -> list:
        if not strList or len(strList) == 1:
            return strList
        stre = self.reverseStrList(strList[1:])
        return stre + [strList[0]]  # 加[],否则为list+str类型报错

    def reverseString(self, strList: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # 此思路无法处理切片时的新变量，即无法原地翻转，是对切片的翻转
        # n = len(strList) - 1
        # if not strList or n == 0:
        #     return
        # strList[0], strList[n] = strList[n], strList[0]
        # self.reverseString(strList[1:n])
        #
        # print(strList)

        # 内层函数辅助
        self.helper(strList, 0, len(strList) - 1)
        # return strList  # ['o', 'l', 'l', 'e', 'h']
        return

    def helper(self, sList, l, r):
        """
        时间复杂度：O(n)。执行了n/2次的交换。
        空间复杂度：O(n)，递归过程中使用的堆栈空间。
        """
        if l >= r:
            return
        # 在递去的过程中解决问题
        sList[l], sList[r] = sList[r], sList[l]
        l += 1
        r -= 1

        self.helper(sList, l, r)


strings = "12345678"
strings1 = ["h", "e", "l", "l", "o"]
# print(Solution().reverseStr(strings))
# print(Solution().reverseStrList(strings1))
print(Solution().reverseString(strings1))
