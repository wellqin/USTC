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
    if not nums:
        return
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def quickSort(nums, l, r):
    # if r - l < 15:
    #     insertSort(nums)
    #     return
    if l < r:
        lt, gt = partitionRandom(nums, l, r)
        quickSort(nums, l, lt - 1)
        quickSort(nums, gt, r)


def partitionRandom(nums, l, r):
    randomInt = random.randint(l, r)
    nums[randomInt], nums[l] = nums[l], nums[randomInt]
    return partition(nums, l, r)


def partition(nums, l, r):
    # 二路快排
    # x = nums[l]
    # i = l + 1
    # j = r
    #
    # while True:
    #     while i <= r and nums[i] < x:
    #         i += 1
    #     while j >= l + 1 and nums[j] > x:
    #         j -= 1
    #     if i > j:
    #         break
    #     nums[i], nums[j] = nums[j], nums[i]
    #     i += 1
    #     j -= 1
    # nums[l], nums[j] = nums[j], nums[l]
    # return j

    # 三路快排
    x = nums[l]
    lt, gt = l, r + 1
    i = l
    while i < gt:
        if nums[i] < x:
            nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
            i += 1
            lt += 1
        elif nums[i] > x:
            nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
            gt -= 1
        else:
            i += 1
    nums[l], nums[lt] = nums[lt], nums[l]
    return lt, gt



nums = [1, 3, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]
quickSort(nums, 0, len(nums) - 1)
print(nums)
