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


def is_sub(a, b):
    al = len(a)
    bl = len(b)
    res = ''
    for i in range(al):
        if i < bl and a[i] == b[i]:
            res += a[i]
            continue
        break

    return res

print("abc", "deaebc"[:-1])
print(is_sub("flower", "flow"))













