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

# if __name__ == "__main__":
#     array = [1, 3, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]
#     quick_sort(array, 0, len(array) - 1)
#     print(array)

import random


def quicksort(arr, l, r):
    if l < r:
        q = random_partition(arr, l, r)
        quicksort(arr, l, q - 1)
        quicksort(arr, q + 1, r)


def partition(arr, l, r):
    i = l - 1
    for j in range(l, r):
        if arr[j] <= arr[r]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def random_partition(arr, l, r):
    i = random.randint(l, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, l, r)


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]

print("initial array:\n", arr)
quicksort(arr, 0, len(arr) - 1)
print("result array:\n", arr)
