# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        选择排序
Description :   
Author :          wellqin
date:             2019/9/23
Change Activity:  2019/9/23
-------------------------------------------------
"""
array = [1, 3, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]
array1 = [1, 3, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]

def select_sort(array):
    if not array:
        return
    N = len(array)
    for i in range(N-1):
        minindex = i
        for j in range(i+1, N):
            if array[minindex] > array[j]:  # 交换多次
                array[minindex], array[j] = array[j], array[minindex]
    return array
print(select_sort(array))


def select_sort(array):
    if not array:
        return
    N = len(array)
    for i in range(N-1):
        minindex = i
        for j in range(i+1, N):
            if array[minindex] > array[j]:  # 交换一次
                minindex = j
        if i != minindex:
            array[minindex], array[i] = array[i], array[minindex]
    return array
print(select_sort(array1))
