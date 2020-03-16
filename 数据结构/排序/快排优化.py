# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        快排优化
Description :   
Author :          wellqin
date:             2020/3/12
Change Activity:  2020/3/12
-------------------------------------------------
"""
import random

# 算法导论一般解法
"""
类似于归并排序，快速排序也是将整个数组一分为二（小于标定点的部分和大于标定点的部分），
整个过程也会行程一棵二叉树。但区别在于，
归并排序的划分是均匀地一分为二，产生的二叉树高度近乎为logn。
而上面实现的快速排序有在顺序性较强的时候，划分的两个部分是极度偏斜的，就会产生平衡性很差的树。
最差的情况会退化成O（n2）级别的算法。（形成的二叉树退化成了链表）

改进方式：1.在partition操作之前先随机选择一个元素与最右边元素交换。 
        2.也可以再加入对小规模数组进行插入排序的优化。
"""


def partion(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if (array[j] < x):
            i += 1
            array[j], array[i] = array[i], array[j]
    i += 1
    array[i], array[r] = array[r], array[i]
    return i


def quick_sort(array, p, r):
    if p < r:
        q = partion(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


print("=========================================================")


# 算法导论优化一： 随机化版本
def quicksort1(arr, l, r):
    if l < r:
        q = random_partition(arr, l, r)
        quicksort1(arr, l, q - 1)
        quicksort1(arr, q + 1, r)


def partition1(arr, l, r):
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
    return partition1(arr, l, r)


"""
上述的实现方法是默认把等于标定元素的值都放在了右半部分。如果等于标定元素的数值过多，
即数组中存在大量的重复元素时，此时partition的划分仍会十分偏斜，再次退化。
"""


# 优化二： 双路快速排序
# 双路快速排序的partition
# 返回j, 使得arr[l...j-1] < arr[j] ; arr[j+1...r] > arr[j]

def insertion_sort(nums, left, right):
    for i in range(left + 1, right + 1):
        pre = i - 1
        cur_num = nums[i]
        while pre >= left and nums[pre] > cur_num:
            nums[pre + 1] = nums[pre]
            pre -= 1
        nums[pre + 1] = cur_num


def partition2(nums, left, right):
    # 随机在arr[l...r]的范围中, 选择一个数值作为标定点pivot
    rand_index = random.randint(left, right)
    nums[left], nums[rand_index] = nums[rand_index], nums[left]
    x = nums[left]

    i, j = left + 1, right
    """
    注意这里的边界：用小于和大于号，遇到大量相等的partition元素的时候，
    程序可以通过i++,j++使得树的分裂点更居中，因此树也更趋于平衡
    而用小于等于和大于等于方式则会将连续出现的这些值归为其中一方，使得两棵子树不平衡
    """
    while True:
        while i <= right and nums[i] < x:  # 边界：用小于和大于号
            i += 1
        while j >= left + 1 and nums[j] > x:  # AT left + 1
            j -= 1
        if i > j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[left], nums[j] = nums[j], nums[left]
    return j


def __quick_sort(nums, left, right):
    if right - left <= 15:  # 当数据规模很小的时候采用插入排序
        insertion_sort(nums, left, right)
        return
    # if left < right:  # 当快排划分规模小于15时，采用插入排序
    p = partition2(nums, left, right)
    __quick_sort(nums, left, p - 1)
    __quick_sort(nums, p + 1, right)


def quick_sort2(nums):
    __quick_sort(nums, 0, len(nums) - 1)


# arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0, 33, 44, 55, 66]
#
# print("initial array:\n", arr)
# quick_sort2(arr)
# print("result array:\n", arr)


# 优化三：三路快排消除重复元素影响
def __partition_three_ways(nums, left, right):
    # 随机在arr[l...r]的范围中, 选择一个数值作为标定点pivot
    rand_index = random.randint(left, right)
    nums[left], nums[rand_index] = nums[rand_index], nums[left]
    x = nums[left]

    lt, gt = left, right+1
    i = left
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
    nums[left], nums[lt] = nums[lt], nums[left]

    return lt, gt


def __quick_sort3(nums, left, right):
    # if right - left <= 15:  # 当数据规模很小的时候采用插入排序， 具体过程在上面
    #     insertion_sort(nums, left, right)
    #     return
    if left < right:
        lt, gt = __partition_three_ways(nums, left, right)
        __quick_sort3(nums, left, lt - 1)
        __quick_sort3(nums, gt, right)


def quick_sort3(nums):
    __quick_sort3(nums, 0, len(nums) - 1)


arr = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0, 33, 44, 55, 66, 5, 5, 5]

print("initial array:\n", arr)
quick_sort3(arr)
print("result array:\n", arr)
