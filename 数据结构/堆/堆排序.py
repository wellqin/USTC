# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        堆排序
Description :   
Author :          wellqin
date:             2019/7/10
Change Activity:  2019/7/10
-------------------------------------------------
"""
"""
关于数组下标

将一个数组构建成二叉树的结构，那么对于其中某一个元素的index假设为n，满足以下条件：

1）它的父节点若存在，父节点的index为n//2(n//2指n除以2取整数)
2）若是左子节点存在，index为2*n
3）若是右子节点存在，index为2*n+1
注意：以上条件是在index是从1开始才满足，所以在后面计算中会在数组第一个位置添加一个[0]作为占位元素。

操作步骤：
以由对数组从小到大进行排序的情况，需要构建大根堆。

1.首先将整个数组进行构建一个大根堆得到[0,R1,....,Rn]（具体实现后面讲）
2.由于R1是最大的数，所以把R1与Rn改变位置，变成[0,Rn,...,Rn-1,R1]，此时[0,Rn...,Rn-1]是无序的，[R1]是有序的
3.对数组[0,Rn...,Rn-1]进行重构大根堆，得到[0,R2,....,Rn-1]
4.由于R2是最大的数，所以把R2与Rn-1改变位置，变成[0,Rn-1,...Rn-2,R2,R1]，此时[0,Rn-1...,Rn-2]是无序的，[R2,R1]是有序的
5.重复以上步骤，直到无序列表只有[0]，最终得到的有序序列则是按照从小到大规律排列的。

为了能更好的理解上面的话，我推荐看b站这个视频演示。。
https://www.bilibili.com/video/av18980178?from=search&seid=3518072115040122033
"""
import math, random


# 网上找的打印树的一个函数，很好用，谁用谁知道
def print_tree(array): # 打印堆排序使用
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
    depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
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

def sort(arr,start,end):
    if end == start * 2:
        if arr[start * 2] > arr[start]:
            arr[start * 2], arr[start] = arr[start], arr[start * 2]
    else:
        if end < start * 2 + 1:
            return
        else:
            left = arr[start*2]
            right = arr[start*2+1]
            if left>right and left > arr[start]:
                arr[start * 2 ], arr[start] = arr[start], arr[start * 2 ]
                sort(arr,start*2,end)
            if left<right and right > arr[start]:
                arr[start * 2+1], arr[start] = arr[start], arr[start * 2+1]
                sort(arr, start * 2+1, end)

def heapfiy(arr):
    x = len(arr) - 1
    n = x // 2
    while n > 0:
        # print(n)
        sort(arr, n, x)
        n -= 1

# 以下是主函数

# 第一个0是占位用
orignal_list=[0, 74, 73, 59, 72, 64, 69, 43, 36, 70, 61, 40, 16, 47, 67, 17, 31, 19, 24, 14, 20, 48, 5, 7, 3, 78, 84, 92, 97, 98, 99]
print(orignal_list)
# 第一次构建最大堆
heapfiy(orignal_list)
# 打印树
print_tree(orignal_list)

x= len(orignal_list) - 1
while x!=1:
    # 交换最大的数和最后一个
    orignal_list[1],orignal_list[x]=orignal_list[x],orignal_list[1]
    x-=1
    # 由于交换了，不再是最大堆，重新构建最大堆
    n = x//2
    while n > 0:
        sort(orignal_list,n,x)
        n -= 1

#打印最后结果
print_tree(orignal_list)
print(orignal_list)
print("================================================================")



import math
# import pygraphviz as pgv
from collections import Iterable



class BinaryHeap(object):
    """一个二叉堆, 小顶堆 利用列表实现"""

    def __init__(self, max_size=math.inf):
        self._heap = [-math.inf]  # 初始值设置一个无限大的哨兵
        self.max_size = max_size

    def __len__(self):
        """求长度"""
        return len(self._heap) - 1

    def insert(self, *data):
        """向堆中插入元素"""
        if isinstance(data[0], Iterable):
            if len(data) > 1:
                print("插入失败...第一个参数可迭代对象时参数只能有一个")
                return
            data = data[0]
        if not len(self) + len(data) < self.max_size:
            print("堆已满, 插入失败")
            return
        for x in data:
            self._heap.append(x)
            self._siftup()
        print("插入成功")

    def _siftup(self):
        """最后插入的元素上浮"""
        pos = len(self)  # 插入的位置
        x = self._heap[-1]  # 获取最后一个位置元素
        while x < self._heap[pos >> 1]:  # 此处可以体现出哨兵的作用了, 当下标为0时, x一定小于inf
            # self._heap[pos], self._heap[pos >> 1] = self._heap[pos >> 1], self._heap[pos]
            self._heap[pos] = self._heap[pos >> 1]
            pos >>= 1
        self._heap[pos] = x

    def _siftdown(self, idx):
        """序号为i的元素下沉"""
        temp = self._heap[idx]
        length = len(self)
        while 1:
            child_idx = idx << 1
            if child_idx > length:
                break
            if child_idx != length and self._heap[child_idx] > self._heap[child_idx + 1]:
                child_idx += 1
            if temp > self._heap[child_idx]:
                self._heap[idx] = self._heap[child_idx]
            else:
                break
            idx = child_idx
        self._heap[idx] = temp

    def show_heap(self):
        """调试用，打印出数组数据"""
        print(self._heap[1:])

    # def draw(self, filename='./heap.png'):
    #     """调试用，生成直观二叉树的图片文件"""
    #     g = pgv.AGraph(strict=False, directed=True)
    #     g.node_attr['shape'] = 'circle'
    #     idx = 1
    #     length = len(self)
    #     idx_length = pow(2, int(math.log(length, 2))) - 1
    #     while idx <= idx_length:
    #         if idx << 1 <= length:
    #             g.add_edge(self._heap[idx], self._heap[idx << 1])
    #             if (idx << 1) + 1 <= length:
    #                 g.add_edge(self._heap[idx], self._heap[(idx << 1) + 1])
    #         else:
    #             g.add_node(self._heap[idx])
    #         idx += 1
    #     g.layout('dot')
    #     g.draw(filename)

    def get_min(self):
        if not len(self):
            print("堆为空")
        return self._heap[1]

    def delete_min(self):
        """删除堆顶元素"""
        if not len(self):
            print("堆为空")
            return
        _min = self._heap[1]
        last = self._heap.pop()
        if len(self):  # 为空了就不需要向下了
            self._heap[1] = last
            self._siftdown(1)
        return _min

    def create_heap(self, data):
        """直接创建一个小顶堆, 接收一个可迭代对象参数,效果同insert, 效率比insert一个个插入高,时间复杂度为n"""
        self._heap.extend(data)
        for idx in range(len(self) // 2, 0, -1):
            self._siftdown(idx)

    def clear(self):
        """清空堆"""
        self._heap = [-math.inf]  # 初始值设置一个无限大的哨兵

    def update_key(self, idx, key):
        """更新指定位置的元素, idx>=1"""
        if idx > len(self) or idx < 1:
            print("索引超出堆的数量或小于1")
            return
        self._heap[idx] = key
        self._siftdown(idx)

    def delete_key(self, idx):
        """删除指定位置的元素, idx>=1"""
        if idx > len(self) or idx < 1:
            print("索引超出堆的数量或小于1")
            return
        x = self._heap.pop()  # 取出最后一个元素代替, 保持完全二叉树, 然后调整到合适位置
        if not len(self):
            self._heap[idx] = x
            self._siftdown(idx)

heap = BinaryHeap()
print(heap.__len__())
heap.insert(9,7,8,3,4,2,1)
heap.show_heap()
heap.delete_min()
heap.show_heap()

heap.clear()
heap.show_heap()
heap.create_heap([9,7,8,3,4,2,1])
heap.show_heap()


def heap_sort(data, reverse=False):
    """接受一个可迭代对象进行排序, 默认从小到大排序, 返回一个列表"""
    heap = BinaryHeap()     # 新建一个堆
    heap.create_heap(data)
    lst = []
    for i in range(len(heap)):
        lst.append(heap.delete_min())
    if reverse:
        return lst[::-1]
    return lst

if __name__ == '__main__':
    print(heap_sort([1, 4, 56, 2, 5, 9, 1, 0, 0, 4], reverse=True))
    print(heap_sort('helloworld'))