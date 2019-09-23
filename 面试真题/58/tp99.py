# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        tp99
Description :   
Author :          wellqin
date:             2019/9/21
Change Activity:  2019/9/21
-------------------------------------------------
"""

# import sys
# line = sys.stdin.readline().strip()
# name = line.split('@')[0]
# last = line.split('@')[1]
# mask = ['M','A', 'S', 'K']
# res = ''
# for i in range(len(name)):
#     res += name[i]
#     res += mask[i%4]
# res = res[:-1]
# res += '@'
# res += last
# print(res)


li = list(map(int, input().split()))
li.sort()
print(li[-3])