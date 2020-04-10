# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        差值列表最小
Description :   
Author :          wellqin
date:             2019/9/16
Change Activity:  2019/9/16
-------------------------------------------------
"""

def solution12(lists):
    if not lists:
        return 0
    list1 = list(lists)
    list1.sort()
    list2 = []
    n = len(list1)
    total = sum(list1)
    half_total = total/2
    s = 0
    for i in range(n-1, -1, -1):
        ns = s + list1[i]
        if ns > half_total:
            continue
        else:
            s += list1[i]
            list2.append(list1[i])
            list1.pop(i)
            if abs(s - half_total) < list1[0]:
                break
    return list1, list2
n = int(input())
li = map(int, input().split())
a, b = solution12(li)
# print(abs(sum(a) - sum(b)))
if a or b:
    print(sum(a) or sum(b))
elif a and b:
    print(abs(sum(a) - sum(b)))
else:
    print(0)