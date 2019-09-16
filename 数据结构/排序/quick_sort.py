# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        quick_sort
Description :   
Author :          wellqin
date:             2019/9/15
Change Activity:  2019/9/15
-------------------------------------------------
"""

# 算法导论解法
# def partion(array, p, r):
#     x = array[r]
#     i = p - 1
#     for j in range(p, r):
#         if (array[j] < x):
#             i += 1
#             array[j], array[i] = array[i], array[j]
#     i += 1
#     array[i], array[r] = array[r], array[i]
#     return i
#
#
# def quick_sort(array, p, r):
#     if p < r:
#         q = partion(array, p, r)
#         quick_sort(array, p, q - 1)
#         quick_sort(array, q + 1, r)

def partition(alist, l, r):
    x = alist[r]
    i = l - 1
    for j in range(l, r):
        if (alist[j] < x):
            i += 1
            alist[j], alist[i] = alist[i], alist[j]
    alist[i+1], alist[r] = alist[r], alist[i+1]
    return i + 1


def quick_sort(alist, l, r):
    if l < r:
        q = partition(alist, l, r)
        quick_sort(alist, l, q-1)
        quick_sort(alist, q+1, r)



if __name__ == "__main__":
    array = [1, 3, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]
    quick_sort(array, 0, len(array) - 1)
    print(array)