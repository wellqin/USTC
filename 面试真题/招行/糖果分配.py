# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        糖果分配
Description :   
Author :          wellqin
date:             2019/7/28
Change Activity:  2019/7/28
-------------------------------------------------
"""
"""
题目描述
假设你是一位很有爱的幼儿园老师，想要给幼儿园的小朋友们一些小糖果。但是，每个孩子最多只能给一块糖果。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的糖果的最小尺寸；并且每块糖果 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个糖果 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
注意：
你可以假设胃口值为正。
一个小朋友最多只能拥有一块糖果。

输入描述:
第一行输入每个孩子的胃口值
第二行输入每个糖果的尺寸
孩子数和糖果数不超过1000
输出描述:
能满足孩子数量的最大值
示例1
输入
复制
1 2 3
1 1
输出
复制
1
说明
python内置函数map()，下面就python中输入多个数字这一问题用map()函数解决如下：
nums = list(map(int, input().split()))
"""
child = sorted(list(map(int, input().split())))
candy = sorted(list(map(int, input().split())))
print("child", child)
print("candy", candy)

i, j, num = 0, 0, 0
while i < len(child) and j < len(candy):
    if candy[j] >= child[i]:
        num += 1
        i += 1
        j += 1
    else:
        j += 1
print(num)


# if __name__ == "__main__":
#     # sys.stdin = open("input.txt", "r")
#     g = list(map(int, input().strip().split()))
#     s = list(map(int, input().strip().split()))
#     g.sort()
#     s.sort()
#     i = len(g) - 1
#     j = len(s) - 1
#     ans = 0
#     while i >= 0 and j >= 0:
#         if s[j] >= g[i]:
#             ans += 1
#             j -= 1
#         i -= 1
#     print(ans)

