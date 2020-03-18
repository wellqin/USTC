# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        sortFunc
Description :   
Author :          wellqin
date:             2020/3/16
Change Activity:  2020/3/16
-------------------------------------------------
"""


def bubbleSort(nums):
    if not nums:
        return []
    for i in range(len(nums) - 1):
        flag = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if flag:
            flag = False
            for j in range(len(nums) - 2, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    flag = True
        if not flag:
            break

    return nums


def insertSort(nums):
    if not nums:
        return []
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


def shellSort(nums):
    if not nums:
        return []
    gap = len(nums) >> 1
    while gap:
        for i in range(gap, len(nums)):
            for j in range(i, 0, -gap):
                if nums[j] < nums[j - gap] and j - gap >= 0:
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]
        gap = gap >> 1
    return nums


def selectSort(nums):
    if not nums:
        return []
    for i in range(len(nums) - 1):
        minI = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minI]:
                minI = j
        if minI != i:
            nums[minI], nums[i] = nums[i], nums[minI]
    return nums


def mergeSort(nums):
    if not nums or len(nums) == 1:
        return nums
    mid = len(nums) >> 1
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    while left and right:
        res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return res + left + right


# list = [19, 2, 13, 8, 34, 25, 7]
# print(mergeSort(list))

class myList(list):
    def __init__(self):
        self.heapsize = 0
        super().__init__()


def maxHeap(nums, i):
    l = i << 1
    r = l + 1

    if l <= nums.heapsize and nums[l] > nums[i]:
        largest = l
    else:
        largest = i
    if r <= nums.heapsize and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        maxHeap(nums, largest)


def buildHeap(nums):
    nums.heapsize = len(nums) - 1
    for i in range(nums.heapsize // 2, 0, -1):
        maxHeap(nums, i)


def HeapSort(nums):
    if not nums:
        return []
    buildHeap(nums)
    for i in range(len(nums) - 1, 0, -1):
        nums[i], nums[1] = nums[1], nums[i]
        nums.heapsize -= 1
        maxHeap(nums, 1)
    return nums


# mylist = myList()
# mylist.extend([-1, 19, 2, 13, 8, 34, 25, 7])
# # list = [19, 2, 13, 8, 34, 25, 7]
# print(HeapSort(mylist))

import random


def quickSort(nums, l, r):
    if l < r:
        lt, gt = partition(nums, l, r)
        quickSort(nums, l, lt - 1)
        quickSort(nums, gt, r)
    return nums


def partition(nums, l, r):
    randomInt = random.randint(l, r)
    nums[l], nums[randomInt] = nums[randomInt], nums[l]
    x = nums[l]
    lt = l
    gt = r + 1
    i = l
    while i < gt:
        if nums[i] < x:
            nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
            i += 1
            lt += 1
        elif nums[i] > x:
            nums[i],nums[gt - 1] = nums[gt - 1], nums[i]
            gt -= 1
        else:
            i += 1
    nums[l], nums[lt] = nums[lt], nums[l]
    return lt, gt



nums = [-1, 19, 2, 13, 8, 34, 25, 7]
print(quickSort(nums, 0, len(nums) - 1))
