# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        TopK
Description :   
Author :          wellqin
date:             2019/9/15
Change Activity:  2019/9/15
-------------------------------------------------
问题描述：

从arr[1, n]这n个数中，找出最大的k个数，这就是经典的TopK问题。
"""

# 1. 排序是最容易想到的方法，将n个数排序之后，取出最大的k个，即为所得。
"""
思路1：最基本的思路，将N个数进行完全排序，从中选出排在前K的元素即为所求。
有了这个思路，我们可以选择相应的排序算法进行处理，目前来看快速排序，堆排序和归并排序都能达到O(NlogN)的时间复杂度。
当然，这样的答案也是无缘offer的。
"""


# def partition(alist, l, r):
#     x = alist[r]
#     i = l - 1
#     for j in range(l, r):
#         if (alist[j] < x):
#             i += 1
#             alist[j], alist[i] = alist[i], alist[j]
#     alist[i+1], alist[r] = alist[r], alist[i+1]
#     return i + 1
#
#
# def quick_sort(alist, l, r):
#     if l < r:
#         q = partition(alist, l, r)
#         quick_sort(alist, l, q-1)
#         quick_sort(alist, q+1, r)
#
#
# def find_least_k_nums(alist, k):
#     length = len(alist)
#     if not alist or k <= 0 or k > length:
#         return None
#     start = 0
#     end = length - 1
#     quick_sort(alist, start, end)
#     return alist[:k]


# if __name__ == "__main__":
#     alist = [1, 9, 2, 4, 7, 6, 3]
#     min_k = find_least_k_nums(alist, 5)
#     print(min_k)

"""
时间复杂度：O(n*lg(n))
分析：明明只需要TopK，却将全局都排序了，这也是这个方法复杂度非常高的原因。
那能不能不全局排序，而只局部排序呢？这就引出了第二个优化方法。
"""

# 二、局部排序  不再全局排序，只对最大的k个排序。
# 冒泡是一个很常见的排序方法，每冒一个泡，找出最大值，冒k个泡，就得到TopK。

# def bubble_sort(numlist):
#     # 需要排列的数据个数
#     N = len(numlist)
#     # i 控制一共需要多少趟 N-1
#     for i in range(N - 1):
#         # j 控制每趟需要比较多少次(因为i是从0开始，所以N-i-1)
#         for j in range(N - i - 1):
#             # 判断j和j+1两个位置的数据大小
#             if numlist[j] > numlist[j + 1]:
#                 # 交换（交换的代码有很多种写法）
#                 numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]

def bubble_sort_max(numlist, k):
    # 需要排列的数据个数
    N = len(numlist)
    # i 控制一共需要多少趟 N-1
    for j in range(N - 1):
        # 判断j和j+1两个位置的数据大小
        if numlist[j] > numlist[j + 1]:
            # 交换（交换的代码有很多种写法）
            numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]


def find_least_k_nums2(alist, k):
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return None
    for i in range(k):
        bubble_sort_max(alist, k)
    print(alist[-k:])   # [3, 4, 6, 7, 9]
    return alist[:k]    # [1, 2, 3, 4, 6]


alist = [1, 9, 2, 4, 7, 6, 3]  # [1, 2, 3, 4, 6, 7, 9]
min_k = find_least_k_nums2(alist, 5)
print(min_k)


def bubbleSort(nums, k):
    if not nums:
        return []
    for i in range(k):
        flag = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        # if flag:
        #     flag = False
        #     for j in range(len(nums) - 2 - i, 0, -1):
        #         if nums[j] < nums[j - 1]:
        #             nums[j], nums[j - 1] = nums[j - 1], nums[j]
        #             flag = True
        if not flag:
            break
    return nums[-4:]


list = [19, 2, 13, 8, 34, 25, 7]
print(bubbleSort(list, 4))
"""
时间复杂度：O(n*k)
分析：冒泡，将全局排序优化为了局部排序，非TopK的元素是不需要排序的，节省了计算资源。
不少朋友会想到，需求是TopK，是不是这最大的k个元素也不需要排序呢？这就引出了第三个优化方法。
"""


# 三、堆
# 思路：只找到TopK，不排序TopK。
"""
先用前k个元素生成一个小顶堆，这个小顶堆用于存储，当前最大的k个元素。
接着，从第k+1个元素开始扫描，和堆顶（堆中最小的元素）比较，如果被扫描的元素大于堆顶，则替换堆顶的元素，并调整堆，以保证堆内的k个元素，总是当前最大的k个元素。
直到，扫描完所有n-k个元素，最终堆中的k个元素，就是猥琐求的TopK。

"""
