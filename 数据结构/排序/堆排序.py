# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        算法导论
Description :
Author :          wellqin
date:             2019/7/10
Change Activity:  2019/7/10
-------------------------------------------------

堆排序的时间复杂度分为两个部分一个是建堆的时候所耗费的时间，一个是进行堆调整的时候所耗费的时间。
而堆排序则是调用了建堆和堆调整。

刚刚在上面也提及到了，建堆是一个线性过程，从len/2-0一直调用堆调整的过程，相当于o(h1)+o(h2)+…+o(hlen/2)这里的h表示节点深度，
len/2表示节点深度，对于求和过程，结果为线性的O（n）

堆调整为一个递归的过程，调整堆的过程时间复杂度与堆的深度有关系，相当于lgn的操作。
因为建堆的时间复杂度是O（n）,调整堆的时间复杂度是lgn，所以堆排序的时间复杂度是O（nlgn）。

"""


# def PARENT(i):
#     return i // 2  # 为什么是一半 参考离散数学和数据结构
#     # 我的解释是：二叉树的性质+下标从1开始
#
#
# def LEFT(i):
#     return i * 2  # 同上,下标从1开始
#
#
# def RIGHT(i):
#     return i * 2 + 1  # 同上, 下标从1开始
import math


def print_tree(array):  # 打印堆排序使用
    '''
    深度 前空格 元素间空格
    1     7       0
    2     3       7
    3     1       3
    4     0       1
    '''
    # first=[0]
    # first.extend(array)
    # array=first
    index = 1
    depth = math.ceil(math.log2(len(array)))  # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()


class Mylist(list):
    def __init__(self):
        self.heap_size = 0
        super().__init__()  # super().__init__()的作用就是执行父类的构造函数，使得我们能够调用父类的属性。


def MAX_HEAPIFY(A, i):
    l = i << 1  # 位运算方式省去了LEFT/RIGHT函数调用
    r = (i << 1) + 1

    # 找出最大的结点
    # i的左孩子是否大于i
    # A.heap_size 写一个继承了list类 类中加上这个参数（Mylist）
    # 或者选择A[0] 位放heap_size ??
    # 或者设计全局变量

    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    # 和右孩子比
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r

    # largest = max(A[l], A[r], A[i])  # list index out of range

    if largest != i:  # 如果A[i]不是最大的 就要调堆了
        A[i], A[largest] = A[largest], A[i]  # 交换
        MAX_HEAPIFY(A, largest)  # 递归调largest


def BUILD_MAX_HEAP(A):
    A.heap_size = len(A) - 1
    # 从第一个非叶子节点开始, 从n//2开始到1
    for i in range(A.heap_size // 2, 0, -1):
        MAX_HEAPIFY(A, i)


# 因为建堆的时间复杂度是O（n）,调整堆的时间复杂度是lgn，所以堆排序的时间复杂度是O（nlgn）。
def HEAPSORT(A):
    BUILD_MAX_HEAP(A)  # 建堆O（n）
    for i in range(len(A) - 1, 1, -1):
        A[1], A[i] = A[i], A[1]  # 第一位和最后一位换
        A.heap_size = A.heap_size - 1  # 取出了一个,size递减，保证最大值不会被重新排序
        MAX_HEAPIFY(A, 1)  # 调堆lgn


if __name__ == '__main__':
    A = Mylist()
    # print(type(A))
    # 由于构造了一个前置的-1，所以编号和列表的索引正好重合
    for i in [-1, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 6]:  # A = [,...] A会变成list
        A.append(i)
    # print(type(A))
    HEAPSORT(A)
    print("堆排序后:", A)
