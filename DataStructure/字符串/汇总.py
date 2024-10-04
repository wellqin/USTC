# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        汇总
Description :   
Author :          wellqin
date:             2019/8/5
Change Activity:  2019/8/5
-------------------------------------------------
"""

"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。

输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        1.一个字符串如果符合要求，则该字符串至少由2个子串组成。例：b b / abc abc
        2.s+s以后，则该字符串至少由4个子串组成 bb+bb / abcabc+abcabc
        3.截去首尾各一个字符s[1:-1] （注：只截一个是为了判断类似本例，重复子串长度为1的情况。
          当重复子串长度大于1时，任意截去首尾小于等于重复子字符串长度都可）
        4.由于s+s组成的4个重复子串被破坏了首尾2个，则只剩下中间两个 bc abcabc ab。
          此时在判断中间两个子串组成是否等于s，若是，则成立。       

        """
        str1 = (s + s)[1:-1]  # (s*2)
        return s in str1