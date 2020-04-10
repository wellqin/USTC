# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        电话号码
Description :   
Author :          wellqin
date:             2019/9/20
Change Activity:  2019/9/20
-------------------------------------------------
"""

# n = int(input())
# li = []
# for i in range(n):
#     b = str(input())
#     c = str(input())
#     li.append([b, c])
# print(li)
n = 2
li = [['11', '88888888888'], ['3', '000']]

for i in range(n):
    if not len(li[i][1]) or not li[i][0]:
        print('NO')
        break
    if li[i][0] == "11" and li[i][1].startswith('8') is True:
        print('YES')
    elif len(li[i][1]) >= 11 and li[i][1].startswith('8') is True:
        print('YES')
    elif len(li[i][1]) >= 11:
        idx = li[i][1].index('8')
        if len(li[i][1][idx:]) >= 11:
            print('YES')
        else:
            print('NO')
    elif len(li[i][1]) <= 11:
        print('NO')
