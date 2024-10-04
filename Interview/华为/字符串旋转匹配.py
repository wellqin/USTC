# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        字符串旋转匹配
Description :   
Author :          wellqin
date:             2019/8/5
Change Activity:  2019/8/5
-------------------------------------------------
"""

def next_arr(s):
    """
    计算 《部分匹配表》
    https://www.cnblogs.com/dahu-daqing/p/9302668.html
    http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
    :param s:
    :return:
    """

    def calc(p):
        if len(p) > 1:

            # "前缀"指除了最后一个字符以外，一个字符串的全部头部组合
            prefix_com = [p[:i + 1] for i in range(len(p) - 1)]
            # "后缀"指除了第一个字符以外，一个字符串的全部尾部组合
            suffix_com = [p[i + 1:] for i in range(len(p) - 1)]

            common_has_len = 0  # 共有元素的长度

            for i in prefix_com:
                for j in suffix_com:
                    if i == j:
                        common_has_len = len(j)
            return common_has_len
        else:
            return 0

    tmp = []
    for i in range(len(s)):
        t = s[:i + 1]
        tmp.append(calc(t))
    return tmp


def bf(s: str, p: str) -> int:
    ret = -1
    """
    朴素的字符串匹配方法
    :param s: 目标串
    :param p: 模式串
    :return:
    最简单的办法就是蛮力的一个字符一个字符的匹配，但那样的时间复杂度会是O(m*n)
    """
    if len(s) < len(p):
        return ret

    k = 0
    k_end = len(p)

    while k <= len(s) - len(p):
        ts = s[k:k_end]
        if ts == p:
            ret = k
            break
        else:
            k += 1
            k_end += 1

    return ret


def kmp(s, p):
    """
    # kmp算法保证了时间复杂度为O(m+n)
    # next是部分匹配表  比如本例[0, 0, 0, 0, 1, 2, 0]
    """
    next = next_arr(p)

    ret = -1
    flag = False

    sl = list(s)
    pl = list(p)

    if len(sl) < len(pl):
        return ret

    start = 0

    while start <= len(sl) - len(pl):

        eq_num = 0  # 已匹配的字符数
        for i in range(len(pl)):
            if pl[i] != sl[start + i]:
                break
            else:
                eq_num += 1

        if eq_num == 0:
            start += 1
        elif eq_num == len(pl):
            # 全部匹配成功
            ret = start
            flag = True
            break
        else:
            # 模式串不匹配字符的前一个字符
            next_num = next[eq_num - 1]
            # 移动位数 = 已匹配的字符数 - 对应的部分匹配值
            start += (eq_num - next_num)

    return flag


def rotateString(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    maxStep = len(A)
    if A == B:
        return True
    while maxStep:
        A = A[1:] + A[0]
        # flag = kmp(A, B)
        # flag = kmp(A+A, B)

        if flag:
            break
        maxStep -= 1
    return 1 if maxStep > 0 else 0


if __name__ == '__main__':
    s = "BBC ABCDAB ABCDABCDABDE"
    p = "ABCDABD"
    n = len(s)
    print("s = ", s)
    # print(kmp(s, p))
    # print(bf(s, p))
    # print("ABCDABD" in "BBC ABCDAB ABCDABCDABDE"+"BBC ABCDAB ABCDABCDABDE")
    #
    # s = s[1:] + s[0]
    # print("s = ", s)



    print(rotateString(s, p))
