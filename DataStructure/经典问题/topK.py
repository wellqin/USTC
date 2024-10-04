# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        topK
Description :   
Author :          wellqin
date:             2020/3/14
Change Activity:  2020/3/14
-------------------------------------------------
"""


def quick_select_without_optimizer(arr, k):
    n = len(arr)
    # 如果k大于n，没啥好说的，直接返回
    if k >= n:
        return arr

    # 缓存
    buffer = []
    while arr:
        # 选择最后一个元素作为标杆
        mark = arr.pop()
        lt, gt = [], []
        # 遍历数组，将元素分为less和greater
        for x in arr:
            if x <= mark:
                lt.append(x)
            else:
                gt.append(x)
        # 判断三种情况，如果相等直接返回
        if len(lt) == k:
            return buffer + arr
        # 如果小于，将less存入buffer，因为它一定是答案的一部分，可以简化计算
        elif len(lt) < k:
            buffer += lt
            # k要减去less的长度
            k -= len(lt)
            arr = [mark] + gt
        else:
            # 如果大于，直接舍弃右边
            arr = lt



arr = [10, 1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 10]
print(quick_select_without_optimizer(arr, 5))


def insert_sort(nums):
    # 获取需要排序数据的个数
    N = len(nums)
    # 插入排序的第一次插入从第二个数字开始选择，所以下标从1开始
    for i in range(1, N):
        # 从选择插入的数据，一次和它前一个比较，主要比前面的小就交换
        for j in range(i, 0, -1):
            # 判断大小
            if nums[j] < nums[j - 1]:
                # 交换
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums

# 算法导论BFPRT算法
def bfprt(arr, l=None, r=None):
    if l is None or r is None:
        l, r = 0, len(arr)
    length = r - l
    # 如果长度小于5，直接返回中位数
    if length <= 5:
        arr[l: r] = insert_sort(arr[l: r])
        return l + length // 2
    medium_num = l
    start = l
    # 否则每5个数分组
    while start + 5 < r:
        # 对每5个数进行插入排序
        arr[start: start + 5] = insert_sort(arr[start: start + 5])
        arr[medium_num], arr[start + 2] = arr[start + 2], arr[medium_num]
        medium_num += 1
        start += 5
    # 特殊处理最后不足5个的情况
    if start < r:
        arr[start:r] = insert_sort(arr[start:r])
        _l = r - start
        arr[medium_num], arr[start + _l // 2] = arr[start + _l // 2], arr[medium_num]
        medium_num += 1
    # 递归调用，对中位数继续求中位数
    return bfprt(arr, l, medium_num)


def quick_select(arr, k):
    n = len(arr)
    if k >= n:
        return arr

    # 获取标杆的下标
    mark = bfprt(arr)
    arr[mark], arr[-1] = arr[-1], arr[mark]
    buffer = []

    while arr:
        mark = arr.pop()
        less, greater = [], []
        for x in arr:
            if x <= mark:
                less.append(x)
            else:
                greater.append(x)
        if len(less) == k:
            return buffer + less
        elif len(less) < k:
            k -= len(less)
            buffer += less
            arr = [mark] + greater
        else:
            arr = less


arr = [10, 1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 10]
print(quick_select(arr, 5))