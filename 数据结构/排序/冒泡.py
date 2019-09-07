# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        冒泡
Description :   
Author :          wellqin
date:             2019/8/23
Change Activity:  2019/8/23
-------------------------------------------------

通过上面的案例我们已经知道冒泡排序的原理和实现过程，但是在处理一些特殊数据上的时候，
我们还可以对冒泡排序优化，例如：一个数组本来就是有序，1，2，3，4，5，6，7，这样的一个数组
已经是正确的顺序的，我们只需要比较一趟后，发现这一趟所有的数据都没有发生改变，
就说明这已经是一个正确的顺序的，后面的循环就没必要循环下去了，这样便能提高程序的效率，
而我们只需要在冒泡排序的代码中，判断是否这一样都没发生交换即可。


最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
最坏时间复杂度：O(n2)

冒泡排序就是把小的元素往前调或者把大的元素往后调。
比较是相邻的两个元素比较，交换也发生在这两个元素之间。
所以，如果两个元素相等，是不会再交换的；如果两个相等的元素没有相邻，
那么即使通过前面的两两交换把两个相邻起来，这时候也不会交换，
所以相同元素的前后顺序并没有改变，所以冒泡排序是一种稳定排序算法。
"""


def bubble_sort(numlist):
    # 需要排列的数据个数
    N = len(numlist)
    # i 控制一共需要多少趟 N-1
    for i in range(N - 1):
        # j 控制每趟需要比较多少次(因为i是从0开始，所以N-i-1)
        for j in range(N - i - 1):
            # 判断j和j+1两个位置的数据大小
            if numlist[j] > numlist[j + 1]:
                # 交换（交换的代码有很多种写法）
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]



list = [19, 2, 13, 8, 34, 25, 7]
print("排序前list = %s" % list)
bubble_sort(list)
print("排序后list = %s" % list)


def bubble_sort(numlist):
    # 需要排列的数据个数
    N = len(numlist)
    # i 控制一共需要多少趟 N-1
    for i in range(N - 1):

        # 定义一个变量，用于记录是否在本趟中发生了交换
        isChange = 0

        # j 控制每趟需要比较多少次(因为i是从0开始，所以N-i-1)
        for j in range(N - i - 1):
            # 判断j和j+1两个位置的数据大小
            if numlist[j] > numlist[j + 1]:
                # 交换（交换的代码有很多种写法）
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
                # 只要发生了交换，我们就改变isChange的值为1
                isChange = 1

        # 只要isChange =0说明已经是正确顺序了，直接break即可
        if isChange == 0:
            break


list1 = [19, 2, 13, 8, 34, 25, 7]
print("排序前list1 = %s" % list1)
bubble_sort(list1)
print("排序后list1 = %s" % list1)

