# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        归并
Description :   
Author :          wellqin
date:             2019/9/12
Change Activity:  2019/9/12
-------------------------------------------------
"""

"""
归并排序：
    先分开再合并，分开成单个元素，合并的时候按照正确顺序合并
    
    假如我们有一个n个数的数列，下标从0到n-1
    首先是分开的过程
    1 我们按照 n//2 把这个数列分成两个小的数列
    2 把两个小数列 再按照新长度的一半 把每个小数列都分成两个更小的。。。一直这样重复，一直到每一个数分开了
    
    比如：    6 5 4 3 2 1
        第一次 n=6 n//2=3 分成      6 5 4      3 2 1
        第二次 n=3 n//2=1 分成    6   5 4    3   2 1
        第三次 n=1的部分不分了
               n=2 n//2=1 分成     5   4      2  1
                
    之后是合并排序的过程：
    
    3 分开之后我们按照最后分开的两个数比较大小形成正确顺序后组合绑定
        刚刚举得例子 最后一行最后分开的数排序后绑定   变成     4 5     1 2
        排序后倒数第二行相当于把最新分开的数排序之后变成    6   4 5       3    12
    
    4 对每组数据按照上次分开的结果，进行排序后绑定
        6 和 4 5(两个数绑定了)  进行排序
        3 和 1 2(两个数绑定了)  进行排序
        排完后 上述例子第一行待排序的  4 5 6      1 2 3  两组数据
    
    5 对上次分开的两组进行排序
        拿着 4 5 6     1 2 3两个数组，进行排序，每次拿出每个数列中第一个(最小的数)比较，把较小的数放入结果数组。再进行下一次排序。
        每个数组拿出第一个数，小的那个拿出来放在第一位 1 拿出来了，   变成4 5 6    2 3
        每个数组拿出第一个书比较小的那个放在下一个位置  1 2被拿出来，  待排序 4 5 6      2
        每个数组拿出第一个书比较小的那个放在下一个位置  1 2 3 被拿出来，  待排序 4 5 6
        如果一个数组空了，说明另一个数组一定比排好序的数组最后一个大 追加就可以结果 1 2 3 4 5 6
    相当于我们每次拿到两个有序的列表进行合并，分别从两个列表第一个元素比较，把小的拿出来，在拿新的第一个元素比较，把小的拿出来
        这样一直到两个列表空了 就按顺序合并了两个列表
        

时间复杂度： 最好最坏都是 O(nlogn)
空间复杂度:  O(n)
稳定性：稳定
缺点：每次拆分数组都要开新的数组， 每次合并数组都要开新数组，空间复杂度很大

二叉树的形式，所以若集合有n个元素，那高度就为log(n)
但其实在每一层做比较的时候，都是一个一个的向序列中放小的元素，每一层都是要放n次
所以时间复杂度为nlog(n)


排序思路：
首先归并排序使用了二分法，归根到底的思想还是分而治之。归并排序是指把无序的待排序序列分解成若干个有序子序列，
并把有序子序列合并为整体有序序列的过程。长度为1的序列是有序的。因此当分解得到的子序列长度大于1时，应继续分解，直到长度为1.
    
"""


def merge_sort(array):  # 递归分解
    mid = len(array) >> 1
    print("mid = ", mid)
    if len(array) == 1:  # 递归结束的条件，分解到列表只有一个数据时结束
        return array
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)  # 进行归并


def merge(left, right):  # 进行归并
    res = []
    while left and right:
        res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        # if list_left[0] <= list_right[0]:  # 如果将"<="改为"<",则归并排序不稳定
        #     final.append(list_left.pop(0))
        # else:
        #     final.append(list_right.pop(0))

    return res+left+right  # 返回排序好的列表


def merge_sort6(array):
    ''' 自己写的（递归法）'''
    # 巧妙之处在于要想到能把merge和merge_sort6结合起来递归，思考的线索是根据参数的格式
    def merge(left,right):
        result=[]
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return result+left+right
    # 递归
    length = len(array)
    if length == 1:
        return array
    while True:
        mid = length//2
        return(merge(merge_sort6(array[:mid]),merge_sort6(array[mid:])))


if __name__ == "__main__":
    array = [6, 5, 4, 3, 2, 1]
    array1 = [6, 5, 4, 3, 2, 1]
    print(merge_sort(array))
    print(merge_sort6(array1))
