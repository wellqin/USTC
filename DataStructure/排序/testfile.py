# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        testfile
Description :   
Author :          wellqin
date:             2020/3/12
Change Activity:  2020/3/12
-------------------------------------------------
"""
import math
import random


def bubble_sort(nums):
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
            for j in range(len(nums) - 2 - i, 0, -1):
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    flag = True

        if not flag:
            break
    return nums


# list = [19, 2, 13, 8, 34, 25, 7]
# print(bubble_sort(list))


# def insert_sort(nums):
#     if not nums:
#         return []
#     N = len(nums)
#     for i in range(1, N):
#         for j in range(i):
#             if nums[i] < nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#     return nums


def insert_sort1(nums):
    if not nums:
        return []
    N = len(nums)
    # 插入该元素后并未改变原序列的前后顺序: 稳定
    for i in range(1, N):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums


# list = [19, 2, 13, 8, 34, 25, 7]
# print(insert_sort(list))
# print(insert_sort1(list))

def shell_sort(nums):
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


# list = [19, 2, 13, 8, 34, 25, 7]
# print(shell_sort(list))


# def select_sort(nums):
#     N = len(nums)
#     for i in range(N - 1):
#         minI = i
#         for j in range(i + 1, N):
#             if nums[j] < nums[minI]:
#                 nums[j], nums[minI] = nums[minI], nums[j]
#     return nums


def select_sort1(nums):
    N = len(nums)
    for i in range(N - 1):
        minI = i
        for j in range(i + 1, N):
            if nums[j] < nums[minI]:
                minI = j
        if minI != i:
            nums[i], nums[minI] = nums[minI], nums[i]
    return nums


# list = [19, 2, 13, 8, 34, 25, 7]
# print(select_sort(list))
# print(select_sort1(list))


def merge_sort(nums):
    if not nums or len(nums) == 1:  # AT
        return nums

    mid = len(nums) >> 1
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    while left and right:
        # AT: append + <=
        res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return res + left + right


def merge_sorts(nums):
    def merge(left, right):
        res = []
        while left and right:
            res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return res + left + right

    length = len(nums)
    if length == 1:
        return nums
    while True:
        mid = length // 2
        return merge(merge_sorts(nums[:mid]), merge_sorts(nums[mid:]))


# list = [19, 2, 13, 8, 34, 25, 7]
# print(merge_sort(list))
# print(merge_sorts(list))

# def print_tree(array):  # 打印堆排序使用
#     """
#     深度 前空格 元素间空格
#     1     7       0
#     2     3       7
#     3     1       3
#     4     0       1
#     """
#     # first=[0]
#     # first.extend(array)
#     # array=first
#     index = 1
#     depth = math.ceil(math.log2(len(array)))  # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
#     sep = '  '
#     for i in range(depth):
#         offset = 2 ** i
#         print(sep * (2 ** (depth - i - 1) - 1), end='')
#         line = array[index:index + offset]
#         for j, x in enumerate(line):
#             print("{:>{}}".format(x, len(sep)), end='')
#             interval = 0 if i == 0 else 2 ** (depth - i) - 1
#             if j < len(line) - 1:
#                 print(sep * interval, end='')
#         index += offset
#         print()


class mylist(list):
    def __init__(self):
        self.heapsize = 0
        super().__init__()


def heapsort(A):
    heapmax(A)
    print_tree(A)
    for i in range(len(A) - 1, 1, -1):
        A[1], A[i] = A[i], A[1]
        A.heapsize = A.heapsize - 1
        maxheap(A, 1)


def heapmax(A):
    A.heapsize = len(A) - 1
    for i in range(A.heapsize // 2, 0, -1):
        maxheap(A, i)


def maxheap(A, i):
    l = i << 1
    r = (i << 1) + 1
    if l <= A.heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= A.heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxheap(A, largest)


# A = mylist()
# A.extend(i for i in [-1, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 6])
# print(A)
# heapsort(A)
# print(A)

# 算法导论解法
# def partion(nums, l, r):
#     x = nums[r]
#     i = l - 1
#     for j in range(l, r):
#         if nums[j] < x:
#             i += 1
#             nums[j], nums[i] = nums[i], nums[j]
#     # 把基准值移过来
#     i += 1
#     nums[i], nums[r] = nums[r], nums[i]
#     return i
#
#
# def quick_sort(nums, l, r):
#     if l < r:
#         print(nums)
#         q = partion(nums, l, r)
#         quick_sort(nums, l, q - 1)
#         quick_sort(nums, q + 1, r)


def partion1(nums, l, r):
    x = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < x:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    # 把基准值移过来
    i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i


def quick_sort1(nums, l, r):
    if l < r:
        q = random_int(nums, l, r)
        quick_sort1(nums, l, q - 1)
        quick_sort1(nums, q + 1, r)


def random_int(nums, l, r):
    randomI = random.randint(l, r)
    nums[r], nums[randomI] = nums[randomI], nums[r]
    return partion1(nums, l, r)


nums = [1, 3, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]
quick_sort1(nums, 0, len(nums) - 1)
print(nums)
