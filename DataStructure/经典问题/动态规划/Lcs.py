# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        Lcs
Description :
Author :          wellqin
date:             2019/7/20
Change Activity:  2019/7/20
-------------------------------------------------
"""

class Solution:
    def PrintBUCutRod(self, s1, s2):
        # write code here
        lens1, lens2 = len(s1), len(s2)  # lens1 列 ；lens2 行

        # 生成字符串长度加1的0矩阵，c用来保存对应位置匹配的结果
        c = [[0 for col in range(lens1+1)] for row in range(lens2+1)]

        # d用来记录转移方向
        d = [[None for x in range(lens1+1)] for y in range(lens1+1)]

        for i in range(lens1+1):
            c[0][i] = 0
        for j in range(lens2+1):
            c[j][0] = 0
        for i in range(1, lens2+1):
            for j in range(1, lens1+1):
                if s1[j-1] == s2[i -1]:
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j],c[i][j-1])
        return c[lens2][lens1]

x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']
print(Solution().PrintBUCutRod(x, y))



import numpy

def find_lcseque(s1, s2):
     # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
    m = [ [ 0 for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]
    # d用来记录转移方向
    d = [ [ None for x in range(len(s2)+1) ] for y in range(len(s1)+1) ]

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:            #字符匹配成功，则该位置的值为左上方的值加1
                m[i][j] = m[i-1][j-1]+1
                d[i][j] = 'ok'

            elif m[i][j-1] > m[i-1][j]:  # 左值大于上值，则该位置的值为左值，并标记回溯时的方向
                m[i][j] = m[i][j-1]
                d[i][j] = 'left'

            else:                           # 上值大于左值，则该位置的值为上值，并标记方向up
                m[i][j] = m[i-1][j]
                d[i][j] = 'up'
    (i, j) = (len(s1), len(s2))
    print(numpy.array(d))
    print(m[len(s1)][len(s2)])

    s = []
    while m[i][j]:    #不为None时
        c = d[i][j]
        if c == 'ok':   #匹配成功，插入该字符，并向左上角找下一个
            s.append(s1[i-1])
            i-=1
            j-=1
        if c =='left':  #根据标记，向左找下一个
            j -= 1
        if c == 'up':   #根据标记，向上找下一个
            i -= 1
    s.reverse()
    return ''.join(s)

print(find_lcseque('abdfg','abcdfg'))


# 计算LCS长度算法    算法 改进    只用 一行 和 一个 额外空间 求得长度   空间复杂度由O(m*n)降低为O(n)
# 空间优化。观察状态转移方程，计算的F[i,j]时只和F[i-1,j-1]，F[i,j-1]，F[i-1,j]三个元素直接相关。
# 仔细分析一下，在递推F[i]这一行的子问题时，只需要知道F[i-1]一行的值和当前计算的F[i,j]的前一个元素的值f[i,j-1]即可，于是空间复杂度由O(m*n)降低为O(n)。
# 核心思想

# 初始化一个长m+1全0的序列base[]，一个为0的递推前导front和一个当前计算元素pre(意义上的F[i,j])，
# 每次计算完F[i,j]后，front的值更新到base[j-1]上，然后把pre更新到front上，然后向后扫描……注意一行最后一个元素的更新！
# 这样迭代n次，最后base[m]的值即LCS的值！

def lcsLength(x, y):
    m = len(x) + 1
    n = len(y) + 1
    length = min(m, n)
    # 存放箭头方向
    base = [0 for i in range(length)]
    # 已经全部初始化为 0 了   上↑  左←  左上↖
    for i in range(1, m):
        # 进入下一行时 front = 0
        front = 0
        for j in range(1, n):
            # 数组第一个 元素 下标为 0     front值上移成为下一行的上方值   pre值前移成为下一个的front值
            if x[i-1] == y[j-1]:
                pre = base[j-1] + 1
                base[j - 1] = front
                front = pre
            elif base[j] >= front:
                pre = base[j]
                base[j - 1] = front
                front = pre
            else:
                pre = front
                base[j - 1] = front
                front = pre
            # 因为base最后一个元素在判断中没被更新，所以一行循环结束时，单独把base末尾元素更新
            if j == n-1:
                base[j] = front
                print("base", base)
    return base[length - 1]


x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']
count = lcsLength(x, y)
print("===========================")
print("其最长公共子序列长度为：", count)


"""
最长公共子串
最长公共子串：两个字符串中连续相等的最长子串。
动态规划
"""

class LongestSubstring:
    def findLongest(self, s1, s2):
        n, m = len(s1), len(s2)
        c = [[0 for i in range(n+1)] for j in range(m+1)]
        max_ = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s2[i-1] == s1[j-1]:
                    # if i>0 and j >0:
                    #     c[i][j]=c[i-1][j-1] +1
                    # else:
                    #     c[i][j] = 1
                    c[i][j] = c[i - 1][j - 1] + 1
                    if c[i][j] > max_:
                        max_ = c[i][j]
        print(numpy.array(c))
        return max_

x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']
print(LongestSubstring().findLongest(x, y))