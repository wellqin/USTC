# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        matrix
Description :   
Author :          wellqin
date:             2020/2/13
Change Activity:  2020/2/13
-------------------------------------------------
"""


# # matrix = [[0 for _ in range(4)] for _ in range(3)]
# # print(matrix)
# # li = [[0, 0, 0, 0],
# #       [0, 0, 0, 0],
# #       [0, 0, 0, 0]]
# n = 3
# m = 7
# dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
# print(dp)
# dp = [[1, 1, 1],
#       [1, 0, 0],
#       [1, 0, 0],
#       [1, 0, 0],
#       [1, 0, 0],
#       [1, 0, 0],
#       [1, 0, 0]]
uppercase = ['A', 'B', 'C']
lowercase = ['a', 'b', 'c']

print(zip(uppercase, lowercase))  # <zip object at 0x00000161C9974EC8>
for x in zip(uppercase, lowercase):
    print(x)  # ('A', 'a') ('B', 'b') ('C', 'c')
