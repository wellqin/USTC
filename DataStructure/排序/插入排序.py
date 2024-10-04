# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        插入排序
Description :   
Author :          wellqin
date:             2019/8/23
Change Activity:  2019/8/23
-------------------------------------------------

插入排序算法是基于某序列已经有序排列的情况下，通过一次插入一个元素的方式按照原有排序方式增加元素。
这种比较是从该有序序列的最末端开始执行，即要插入序列中的元素最先和有序序列中最大的元素比较，
若其大于该最大元素，则可直接插入最大元素的后面即可，否则再向前一位比较查找直至找到应该插入的位置为止。

插入排序的基本思想是，每次将1个待排序的记录按其关键字大小插入到前面已经排好序的子序列中，
寻找最适当的位置，直至全部记录插入完毕。执行过程中，若遇到和插入元素相等的位置，
则将要插人的元素放在该相等元素的后面，因此插入该元素后并未改变原序列的前后顺序。
我们认为插入排序也是一种稳定的排序方法。插入排序分直接插入排序、折半插入排序和希尔排序3类。


六、插入排序的时间复杂度
最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n^2)

七、插入排序的稳定性
插入排序的基本思想是，每次将1个待排序的数据按其大小插入到前面已经排好序的子序列中，
寻找最适当的位置，直至全部记录插入完毕。执行过程中，若遇到和插入元素相等的位置，
则将要插人的元素放在该相等元素的后面，因此插入该元素后并未改变原序列的前后顺序。
我们认为插入排序也是一种稳定的排序方法。

文章中介绍的直接插入排序，它对于已经基本有序的数据进行排序，效率会很高，
而如果对于最初的数据是倒序排列的，则每次比较都需要移动数据，导致算法效率降低。
"""


# 定义插入排序函数
def insertion_sort(nums):
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

numnums = [19, 2, 13, 8, 34, 25, 7]
print("排序前：%s" % numnums)
insertion_sort(numnums)
print("排序后：%s" % numnums)
