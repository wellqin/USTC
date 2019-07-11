# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        算法导论
Description :   
Author :          wellqin
date:             2019/7/10
Change Activity:  2019/7/10
-------------------------------------------------
"""

def PARENT(i):
    return i//2 # 为什么是一半 参考离散数学和数据结构
                # 我的解释是：二叉树的性质+下标从1开始

def LEFT(i):
    return i*2 #同上

def RIGHT(i):
    return i*2 + 1 #同上


class Mylist(list):
    def __init__(self):
        self.heap_size = 0
        super().__init__() # super().__init__()的作用就是执行父类的构造函数，使得我们能够调用父类的属性。

def MAX_HEAPIFY(A, i):
    l = i << 1
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

    if largest != i: #如果A[i]不是最大的 就要调堆了
        A[i],A[largest] = A[largest],A[i] #交换
        MAX_HEAPIFY(A,largest) #递归调largest


def BUILD_MAX_HEAP(A):
    A.heap_size = len(A)-1
    # print(len(A))
    for i in range(A.heap_size//2, 0, -1):  # 从n//2开始到1
        # print(i)
        MAX_HEAPIFY(A, i)


def HEAPSORT(A):
    BUILD_MAX_HEAP(A) # 建堆
    print("建成的堆：",A)
    for i in range(len(A)-1, 1, -1):
        A[1],A[i] = A[i],A[1] # 第一位和最后有位换
        A.heap_size = A.heap_size - 1 # 取出了一个
        MAX_HEAPIFY(A,1) # 调堆

if __name__ == '__main__':
    A = Mylist()
    # print(type(A))
    for i in[-1,4,1,3,2,16,9,10,14,8,7]: # A = [,...] A会变成list
        A.append(i)
    # print(type(A))
    HEAPSORT(A)
    print("堆排序后:",A)