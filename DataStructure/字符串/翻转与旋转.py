# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        翻转
Description :   
Author :          wellqin
date:             2019/8/5
Change Activity:  2019/8/5
-------------------------------------------------
reverse源码

nums = [1, 2, 3, 4, 5, 6]
n = len(nums)
for i in range(n // 2):
    nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
print(nums)

"""
# 用尽可能多的方法反转字符串,例如将s = "abcdef"反转成 "fedcba"
from functools import reduce

s = "abcdef"
# 第一种：使用字符串切片
result1 = s[::-1]

# 第二种：使用列表的reverse方法
l = list(s)
l.reverse()
result2 = "".join(l)
# 当然下面也行
l = list(s)
result3 = "".join(l[::-1])

# 第三种：使用reduce
result4 = reduce(lambda x, y: y + x, s)
result41 = ""
for i in s:
    result41 = i + result41
print("result41", result41)


# 第四种：使用递归函数
def func(s):
    if len(s) < 1:
        return s
    return func(s[1:]) + s[0]


result5 = func(s)


# 第五种：使用栈
def func(s):
    l = list(s)  # 模拟全部入栈
    result = ""
    while len(l) > 0:
        result += l.pop()  # 模拟出栈
    return result


result6 = func(s)


# 第六种：for循环
def func(s):
    result = ""
    max_index = len(s) - 1
    for index, value in enumerate(s):
        result += s[max_index - index]
    return result


result7 = func(s)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。
如果在若干次旋转操作之后，A 能变成B，那么返回True。
"""


def rotateString(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    return (len(A) == len(B)) and (B in A + A)


def rotateString1(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    maxStep = len(A)
    if len(A) != len(B):
        return False
    if A == B:
        return True

    while maxStep:
        A = A[1:] + A[0]
        if A == B:
            break
        maxStep -= 1
    return maxStep > 0


# 给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
"""
对于字符串 "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
"""


class Solution:
    """
    @param str: An array of char 字符串数组
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        if len(str) == 0 or offset == 0:
            return str
        for i in range(offset % len(str)):
            str.insert(0, str.pop())
