# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        选择排序
Description :   
Author :          wellqin
date:             2019/9/23
Change Activity:  2019/9/23
-------------------------------------------------
一、选择排序的介绍
选择排序（Selection sort）是一种简单直观的排序算法。首先在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，
它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。
在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

二、选择排序的原理
在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
再从剩余未排序元素中继续寻找最小（大）元素
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。


1. 有N个数据，需要从未排序区挑选N-1次数据放在已排序区队尾
2. 每次从未排序区中挑选的数据要放在已排序的队尾

七、选择排序的时间复杂度
最优时间复杂度：O(n2)
最坏时间复杂度：O(n2)

八、选择排序的稳定性
选择排序是给每个位置选择当前元素最小的，比如给第一个位置选择最小的，在剩余元素里面给第二个元素选择第二小的，
依次类推，直到第n-1个元素，第n个元素不用选择了，因为只剩下它一个最大的元素了。
那么，在一趟选择，如果一个元素比当前元素小，而该小的元素又出现在一个和当前元素相等的元素后面，
那么交换后稳定性就被破坏了。比较拗口，举个例子，序列5 8 5 2 9，我们知道第一遍选择第1个元素5会和2交换，
那么原序列中两个5的相对前后顺序就被破坏了，所以选择排序是一个不稳定的排序算法。
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
