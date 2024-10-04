# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        模板
Description :   
Author :          wellqin
date:             2019/7/25
Change Activity:  2019/7/25
并查集是一种算法可以用来判断相互关联（同属一个集合）的元素属于几个集合，也可以用来判断图结构中的两点是否是联通的。
并查集的问题主要分成两大类：带权并查集，种类并查集。
-------------------------------------------------
"""


# 这里记录一下一种新的数据结构：并查集
def find(x, pres):
    """
    查找x的最上级（首级）
    :param x: 要查找的数
    :param pre: 每个元素的首级
    :return: 元素的上一级
    """
    root, p = x, x  # root:根节点， p:指针

    # 找根节点
    while root != pres[root]:
        root = pres[root]

    # 路径压缩，把每个经过的结点的上一级设为root（直接设为首级）
    while p != pres[p]:
        p, pres[p] = pres[p], root
    return root


def join(x, y, pre, ranks):
    """
    合并两个元素（合并两个集合）
    :param x: 第一个元素
    :param y: 第二个元素
    :param pre: 每个元素的上一级
    :param ranks: 每个元素作为根节点时的秩（树的深度）
    :return: None
    """
    h1, h2 = find(x, pre), find(y, pre)
    # 当两个元素不是同一组的时候才合并
    # 按秩合并
    if h1 != h2:
        if ranks[h1] < ranks[h2]:
            pre[h1] = h2
        else:
            pre[h2] = h1
            if ranks[h1] == ranks[h2]:
                ranks[h1] += 1


# 结点数
n = 10

# 边数据
data = [[0, 9], [9, 3], [1, 2], [2, 8], [4, 5], [6, 7], [0, 5], [6, 8]]

# pre是每个元素的首级，一开始设置每个元素的上一级是自己，ranks一开始设置每个元素的秩为0
pre, ranks = [i for i in range(n)], [0] * n

for edge in data:
    join(edge[0], edge[1], pre, ranks)

print('pre:\t', pre)
print('ranks:\t', ranks)
print('idx:\t', list(range(n)))




# 另外一种方式
class UnionFind():
    is_root = []  # 是否为根
    father = []  # father[k] = value   保存k的父亲节点

    def __init__(self, n):    # 为方便编写，数组下标从1开始，占用列表的零下标
        self.isRoot.append(0)
        self.father.append(True)
        for i in range(1, n + 1):
            self.is_root.append(False)  # 初始化不为其他节点的根节点
            self.father.append(i)       # 初始自己为自己的父亲


    # 递归查找n的父亲节点
    def find(self, n):
        if self.father[n] == n:
            return n
        else:
            return self.find(self.father[n])


    # 合并操作   优化可以使用：路径压缩
    def union(self, a, b):
        Fa = self.find(a)
        Fb = self.find(b)
        if Fa != Fb:
            self.father[Fa] = Fb