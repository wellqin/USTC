# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        数组分组差最小
Description :   
Author :          wellqin
date:             2019/9/20
Change Activity:  2019/9/20
-------------------------------------------------
"""

# n = int(input())
# li = []
# for i in range(n):
#     b = int(input())
#     li.append(list(map(int, input().split())))
#
# print(li)
li = [[5, 9, 4, 7], [9, 13, 18, 10, 12, 4, 18, 3]]

def func(arr):
    ll = list(arr)
    kk = list()
    total = sum(ll)
    htotal = total // 2
    s = 0
    n = len(ll)
    for i in range(-1, 0-n, -1):
        ns = s + ll[i]
        if ns > htotal:
            continue
        else:
            s += ll[i]
            kk.append(ll[i])
            ll.pop(i)
            if abs(s - htotal) <= ll[-1]:
                break
    return ll, kk




for i in range(len(li)):
    res = func(li[i])
    ll = sum(res[0])
    kk = sum(res[1])
    if ll > kk:
        print(kk, ll)
    else:
        print(ll, kk)
