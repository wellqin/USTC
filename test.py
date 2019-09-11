# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/31
Change Activity:  2019/7/31
-------------------------------------------------
"""


# def func(input_num):
#     # input_num每台价钱在（0-10之间） * N台 = M为整数  输出M，N，而且以空格分割,
#     # M = [0，1000]  # 之间
#     # N = 0
#     for i in range(1, 10000):
#         M = input_num * i  # i尽量小
#         while str(M).endswith("0"):
#             return M, i
#
# input_num = float(input())
#
# ll = func(input_num)
# lst = list(ll)
# print(int(lst[0]),int(lst[1]))



"""
AABCD
CDAA
AABCD
ABCD
AABCD
CFS
"""

# l1 = str(input())
# l2 = str(input())
#
# l3 = str(input())
# l4 = str(input())
#
# l5 = str(input())
# l6 = str(input())

# def helper(source, target):
#     m = n = 0
#     while (n < len(target)) and (m < len(source)):
#         if source[m] == target[n]:
#             m += 1
#             n += 1
#         else:
#             n += 1
#     if n == len(target):
#         return "1"
#     else:
#         return "0"
#
#
# # def func(l1,l2,l3,l4,l5,l6):
# def func(l1, l2, l3, l4, l5, l6):
#     # 旋转操作
#     r1 = helper(l1, l2)
#     r2 = helper(l3, l4)
#     r3 = helper(l5, l6)
#     print(r1+r2+r3)




# l1 = "AABCD"
# l2 = "CDAA"
#
# l3 = "AABCD"
# l4 = "ABCD"
#
# l5 = "AABCD"
# l6 = "CFS"
#
# func(l1,l2,l3,l4,l5,l6)
#
# """
# AABCD
# CDAA
# AABCD
# ABCD
# AABCD
# CFS
# """


# import sys
#
#
# def DFSTravel(node, graph, record, stack):
#     record[node] = True
#     stack.append(node)
#     if node in graph:
#         for n in graph[node]:
#             if n not in stack:
#                 if not record[n]:
#                     DFSTravel(n, graph, record, stack)
#             else:
#                 index = stack.index(n)
#                 for i in stack[index:]:
#                     return i
#                 return n
#
#     stack.pop(-1)
#
#
# def func():
#     graph = {}  # 临接字典
#     record = {}
#     stack = []
#     res = ''
#     info = int(sys.stdin.readline())
#     infos = []
#     for i in range(info):
#         l1, l2, l3, l4 = sys.stdin.readline()
#         infos.append([l1, l2, l3, l4])
#         if l1 not in graph:
#             graph[l1] = [l2]
#         elif l2 not in graph[l1]:
#             graph[l1].append(l2)
#         if l1 not in record:
#             record[l1] = False
#         if l2 not in record:
#             record[l2] = False
#
#     for node in record.keys():
#         if not record[node]:
#             res = DFSTravel(node, graph, record, stack)
#     print(res)
#
#
#
#
# infos = [[1,2,3,4], [1,2,2,4]]
# pp = sorted(infos,  key=lambda x: x[2])
# print(pp)




# -*- coding: UTF-8 -*-

import random

print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)








