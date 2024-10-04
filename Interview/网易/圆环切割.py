# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        圆环切割
Description :   
Author :          wellqin
date:             2019/9/21
Change Activity:  2019/9/21
-------------------------------------------------
"""
n = int(input())
li = []
for j in range(n):
    length = int(input())
    print(length)
    for i in range(n):
        li.append(list(map(int, input().split())))

# li = [1,2,3,4,5,6]
# for i in range(len(li)):
#     if sum(li[:1]) == sum(li[1:]):
#         print("YES")
#     else:
#         print("NO")

# for i in range(len(li)-1, -1, -1):
#     if sum(li[:1]) == sum(li[1:]):
#         print("YES")
#     else:
#         print("NO")
