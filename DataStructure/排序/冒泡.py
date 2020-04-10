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


def bubble_sort(nums):
    # 需要排列的数据个数
    N = len(nums)
    # i 控制一共需要多少趟 N-1
    for i in range(N - 1):
        # j 控制每趟需要比较多少次(因为i是从0开始，所以N-i-1)
        for j in range(N - 1 - i):
            # 判断j和j+1两个位置的数据大小
            if nums[j] > nums[j + 1]:
                # 交换（交换的代码有很多种写法）
                nums[j], nums[j + 1] = nums[j + 1], nums[j]



list = [19, 2, 13, 8, 34, 25, 7]
print("排序前list = %s" % list)
bubble_sort(list)
print("排序后list = %s" % list)

# 冒泡排序优化一：设定一个变量为False，如果元素之间交换了位置，将变量重新赋值为True
def bubble_sort(nums):
    # 需要排列的数据个数
    N = len(nums)
    # i 控制一共需要多少趟 N-1
    for i in range(N - 1):

        # 定义一个变量，用于记录是否在本趟中发生了交换
        isChange = 0

        # j 控制每趟需要比较多少次(因为i是从0开始，所以N-i-1)
        for j in range(N - i - 1):
            # 判断j和j+1两个位置的数据大小
            if nums[j] > nums[j + 1]:
                # 交换（交换的代码有很多种写法）
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # 只要发生了交换，我们就改变isChange的值为1
                isChange = 1

        # 只要isChange =0说明已经是正确顺序了，直接break即可
        if isChange == 0:
            break


list1 = [1,2,3,4,5,6,7,8]
print("排序前list1 = %s" % list1)
bubble_sort(list1)
print("排序后list1 = %s" % list1)

# 冒泡排序优化二：搅拌排序 / 鸡尾酒排序
def bubble_sort_1(nums):
    N = len(nums)
    for i in range(N - 1):
        flag = False
        for j in range(N - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if flag:
            flag = False
            for j in range(N - 2 - i, 0, -1):
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    flag = True
        if not flag:
            break
    return nums

list2 = [19, 2, 13, 8, 34, 25, 7]
print("排序前list = %s" % list2)
bubble_sort(list2)
print("排序后list = %s" % list2)

# 冒泡排序优化三：对象排序，或者列表里面都是字符串，那么上述的代码也就没有用了
def bubble_sort_2(nums, comp=lambda x, y: x > y):
    for i in range(len(nums) - 1):
        flag = False
        for j in range(len(nums) - 1 - i):
            if comp(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if flag:
            flag = False
            for j in range(len(nums) - 2 - i, 0, -1):
                if comp(nums[j - 1], nums[j]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    flag = True
        if not flag:
            break
    return nums


list3 = ['apple', 'watermelon', 'pitaya', 'waxberry', 'pear']
print(bubble_sort(list3, lambda s1, s2: len(s1) > len(s2)))  # 按照字符串长度从小到大来排序

# 类似的，当有人叫你给一个类对象排序时，也可以传入lambda 自定义函数
# class Student():
#     """学生"""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return '{self.name}: {self.age}'
#
#
# items1 = [
#     Student('Wang Dachui', 25),
#     Student('Di ren jie', 38),
#     Student('Zhang Sanfeng', 120),
#     Student('Bai yuanfang', 18)
# ]
#
# print(bubble_sort(items1, lambda s1, s2: s1.age > s2.age))



