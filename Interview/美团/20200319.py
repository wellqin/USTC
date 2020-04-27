# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        20200319
Description :   
Author :          wellqin
date:             2020/3/19
Change Activity:  2020/3/19
-------------------------------------------------
"""
# >>> import locale
# >>> locale.setlocale(locale.LC_ALL, '')
# 'en_US.utf8'
# >>> locale.currency(123.2342343234234234)
# '$123.23'
# >>> locale.currency(123.2342343234234234, '')  # the second argument controls the symbol
# '123.23'

# -*- coding: utf-8 -*-
import sys
try:
    while True:
        line1 = sys.stdin.readline().strip()
        if line1 == '':
            break
        # line2 = sys.stdin.readline().strip()
        a = int(line1)
        # l = list(map(int, line2.split()))
        # b = [int(n) for n in line2.split()]
        print(a)
        # print(l)
        # print(b)
except:
    pass

"""
题目描述：
扎金花是一种非常受欢迎的纸牌游戏。而在游戏界有一种于扎金花类似的玩法，叫做扎银花。
相比于扎金花的牌型多变，扎银花就简单多了，虽然同样是三张牌比大小，在扎银花的规则里只需要把三张牌的点数相加再进行大小比较即可，点数大的人获胜。

今天我们玩的不是扑克牌，而是一种取值范围在1-10^9以内的简单牌，两个人一开始各自有n张牌，他们会想办法组合出最大的牌，
请你计算出获胜的一方的三张牌的点数之和。

输入
输入第一行仅包含一个正整数n，代表双方掌握的牌的数量。(1<=n<=20000)
接下来有2行,每行有n个数字，分别代表双方可选的n张牌。

输出
输出仅包含一个正整数，即获胜的一方的最大牌型的点数之和，当然是可能有平局的，此时答案也是唯一的。

样例输入
5
1 2 3 4 5
1 2 3 4 6
样例输出
13
"""
# n = int(input())
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
#
# if n < 3:
#     print(0)
#
# list1.sort()
# list2.sort()
#
# total1 = sum(list1[-3:])
# total2 = sum(list2[-3:])
#
#
# print(total1 if total1 > total2 else total2)


"""
题目描述：
给出一个长度为n的由正整数构成的序列，你需要从中删除一个正整数，很显然你有很多种删除方式，
你需要对删除这个正整数以后的序列求其最长上升子串，请问在所有删除方案中，最长的上升子串长度是多少。

这里给出最长上升子串的定义：即对于序列中连续的若干个正整数，满足a_{i+1}>a_i，则称这连续的若干个整数构成的子串为上升子串，
在所有的上升子串中，长度最长的称为最长上升子串。

输入
输入第一行仅包含一个正整数n，表示给出的序列的长度。(1<=n<=100000)
接下来一行有n个正整数，即这个序列，中间用空格隔开。(1<=a_i<=100000)

输出
输出仅包含一个正整数，即删除一个数字之后的最长上升子串长度。


样例输入
5
2 1 3 2 5
样例输出
3
"""
# N = 5
# nums = [2, 1, 3, 2, 5]
# # N = int(input())
# # nums = list(map(int, input().split()))
#
#
#
# def func(list, N):
#     if not list:
#         return 0
#     if len(set(list)) == 1:
#         return 1
#
#     dp, res = [1 for _ in range(N)], 1
#     for i in range(1, N):
#         if list[i] > list[i - 1]:
#             dp[i] = 1 + dp[i - 1]
#         res = max(dp[i], res)
#     return res
#
#
# def find(list, N):
#     if not list:
#         return 0
#     if len(set(list)) == 1:
#         return 1
#     res, res1 = 1, 1
#     nums = []
#     for i in range(N):
#         if i == 0:
#             nums = list[1:]
#             res1 = func(nums, len(nums))
#         elif i == N - 1:
#             nums = list[:-1]
#             res1 = func(nums, len(nums))
#         else:
#             nums = list[:i] + list[i + 1:]
#             res1 = func(nums, len(nums))
#
#         res = max(res, res1)
#
#     return res
#
#
# print(find(nums, N))


Nms = list(map(int, input().split()))
n = Nms[0]
m = Nms[1]
start = Nms[2]

li = []
for i in range(n):
    aa = list(map(int, input().split()))
    li.append(aa)

k = int(input())

import heapq

"""
题目描述：
晨晨是个爱跑步的孩子，这一天，他准备跑正好k米。他所在的城市的道路可以看做n个点，m条无向边组成的图，每条边有一个固定的长度。
晨晨有强迫症，他跑步前往一个目的地一定要走最短路（当然有多条最短路就可以随意选择了）。
晨晨希望知道，他正好跑k米能走到的目的地的个数。注意，目的地可能在图中的点和边上，且该目的地距离晨晨的起点的最短路正好k米。
若k大于所有路径之和自然不存在这样的目的地，输出结果自然为0。

第一行输入三个数,n,m,s代表图中的点数，边数，以及晨晨的起点的编号
接下来m行，每行3个数u,v,w描述一条无向边，代表点u到点v有一条无向边，长度为w。
接下来一行一个数k，描述晨晨希望跑的距离。

输出一个数，代表不同的目的地个数。

3 3 1
1 2 2
2 3 3
1 3 4
4

例如：晨晨希望跑4米，他可以沿着第三条边直接跑向3号节点，此时跑步距离为4。他也可以先跑第一条边2米，再跑第二条边2米，
停在第二条边的中间2/3的位置。可以证明，这两个目的地到1号节点的最短路都为4
"""


class Solution:
    def __init__(self):
        self.G = {}

    def add(self, s, end, dis):
        self.G.setdefault(s, {})
        self.G[s][end] = dis

    def func(self, s, k, G):
        queue = []
        heapq.heappush(queue, (0, s))  # 出发点

        used = set()
        dist = {s: 0}
        res = 0

        while queue:
            dis, node = heapq.heappop(queue)
            if node > k:
                break
            used.add(node)
            if node not in G.keys():
                continue

            for i, j in G[node].items():
                newDist = dis + j
                if (i not in dist) or (newDist < dist[i]):
                    dist[i] = newDist
                    heapq.heappush(queue, (newDist, i))
                    res += 1
        return res


ss = Solution()
for i in li:
    ss.add(*i)
# print(ss.G)  # {1: {2: 2, 3: 4}, 2: {3: 3}}
print(ss.func(start, k, ss.G))


"""
题目描述：
某个序列的最长不下降子序列的定义为将这个序列去除最少的数，使得剩下的每一个数都大于等于他自身前面的数。
比如，1,0,0,1,1的最长不下降子序列为0,0,1,1，其中去除了第一个1，剩下的数0,0,1,1后面的数都大于等于前面的数。
现在有一个特殊的序列，这个序列中所有的数都是0或者1。你需要按照题目所给的顺序完成两种任务：

1.将某段区间的0变为1,1变为0
2.询问整段序列的最长不下降子序列长度。

每一个操作进行后都会对序列造成改变，这意味着整个序列会不停的发生变化。

输入
第一行2个数n,m，代表序列长度和询问次数
第二行n个数字，中间没有空格。每个数字为0或者1，第 i 个数代表序列中第i个数的大小
接下来m行，每行一个询问。其中，两个操作的询问方式如下：

1.c x y将区间[x,y]的0变为1,1变为0。
2.q 询问整段序列的最长不下降子序列长度。

注意，序列的第一个位置从开始标号，意思为整个序列的下标为1,2...n
1≤n≤100000 , 1≤m≤100000 , 1≤x≤y≤n

输出
对于第二种操作：q类型询问，输出整段序列的最长不下降子序列长度。


样例输入
5 5
10011
q
c 1 5
q
c 1 3
q

样例输出
4
3
4

提示
样例解释
1.第一次询问，原序列为10011，答案为0011
2.第二次修改，原序列为10011，修改后为01100
3.第三次询问，原序列为01100，答案为011或者000
4.第四次修改，原序列为01100，修改后为10000
5.第五次询问，原序列为10000，答案为0000
"""


"""
题目描述：
现在一共有n个任务可以完成。对于每个任务，都有k个子任务可以做。并且第 i 个子任务需要花费的时间是 ti 。
我们可以认为一个子任务需要的时间只和这个子任务是第几个子任务有关，而不和这是属于哪个任务有关。也就是说n个任务的第 i 个子任务需要的时间都是一样的。
每个任务都只可以完成一次，同时每个子任务也只能完成一次，任何任务都不能重复完成。

每当你完成一个子任务你会获得p分，而当你完成一个任务的k个子任务后，你会获得额外的q分，也就是说你会获得pk+q分。
现在你一共有m的时间，你需要求出最大的得分。

输入
第一行三个整数n，k，m。(1≤n≤100),(1≤k≤100),(0≤m≤2e9)
第二行两个整数p，q。(1≤p,q≤100)
第三行k个整数表示每个子任务需要的时间。(1≤ ti≤1e6)

输出
输出在m的时间内能获得的最大得分。

样例输入
3 2 8
3 1
9 5
样例输出
3

提示
输入样例
2 2 3
1 2
1 1

输出样例
5
"""