# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2020/3/12
Change Activity:  2020/3/12
-------------------------------------------------
"""
import random


def insertSort(nums):
    pass


# def partition(nums, l, r):
#     randInt = random.randint(l, r)
#     nums[randInt], nums[r] = nums[r], nums[randInt]
#
#     x = nums[r]
#     i = l - 1
#     for j in range(l, r):
#         if nums[j] < x:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#     i += 1
#     nums[i], nums[r] = nums[r], nums[i]
#     return i


# def partition(nums, l, r):
#     randInt = random.randint(l, r)
#     nums[randInt], nums[l] = nums[l], nums[randInt]
#     x = nums[l]
#     i = l + 1
#     j = r
#
#     while True:
#         while i <= r and nums[i] < x:
#             i += 1
#         while j >= l + 1 and nums[j] > x:
#             j -= 1
#         if i > j:
#             break
#
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j -= 1
#
#     nums[l], nums[j] = nums[j], nums[l]
#     return j


def partition(nums, l, r):
    randInt = random.randint(l, r)
    nums[randInt], nums[l] = nums[l], nums[randInt]
    x = nums[l]
    lt, gt = l, r + 1
    i = l
    while i < gt:
        if nums[i] < x:
            nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
            lt += 1
            i += 1
        elif nums[i] > x:
            nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
            gt -= 1
        else:
            i += 1

    nums[l], nums[lt] = nums[lt], nums[l]

    return lt, gt


def quickSort(nums, l, r):
    if not nums:
        return []
    # if l - l < 15:
    #     insertSort(nums)
    #     return nums
    if l < r:
        lt, gt = partition(nums, l, r)
        quickSort(nums, l, lt - 1)
        quickSort(nums, gt, r)
    return nums


list = [-99, 19, 2, 13, 8, 34, 25, 7]
print(quickSort(list, 0, len(list) - 1))
