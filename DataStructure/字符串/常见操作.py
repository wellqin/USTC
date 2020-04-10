# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        常见操作
Description :   
Author :          wellqin
date:             2019/8/1
Change Activity:  2019/8/1
-------------------------------------------------
"""

#  1.大小写转换
print('ab XY'.lower())  # ab xy
print('ab XY'.upper())  # AB XY

"""
S.title()
S.capitalize()
前者返回S字符串中所有单词首字母大写且其他字母小写的格式，后者返回首字母大写、其他字母全部小写的新字符串。
"""
print('ab XY AB aB abXY'.title())  # Ab Xy Ab Ab Abxy
print('ab XY AB aB abXY'.capitalize())       # Ab xy ab ab abxy

# swapcase()对S中的所有字符串做大小写转换(大写-->小写，小写-->大写)。
print('abc XYZ'.swapcase())   # ABC xyz


L2=['py','th','o','n']
print(''.join(L2))       # python
print('.'.join(L2))       # py.th.o.n

print("a good  example".split())    # ['a', 'good', 'example']
print("a good  ,  example".split(','))    # ['a good  ', '  example']
print("  a good   example  ".split())    # ['a', 'good', 'example']

print(''.join("  a good   example  ".split()))  # agoodexample
print(''.join("  a,good   example  ".split()))  # agoodexample


print(''.join("  a good   example  ".split()).strip())  # agoodexample
print(' '.join("  a good   example  ".split()).strip())  # a good example
print(''.join("  a good   example  ".split()[::-1]).strip())  # examplegooda


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1]).strip()
str = "    a good   example     "
str1 = "  hello   world!  "
print(Solution().reverseWords(str))
print(Solution().reverseWords(str1))

