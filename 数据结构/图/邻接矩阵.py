# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        邻接矩阵
Description :   
Author :          wellqin
date:             2019/7/22
Change Activity:  2019/7/22
-------------------------------------------------
"""

"""
假设一个图A有n个顶点，我们以n*n的二维矩阵列来表示它，这个二维矩阵就是该图的邻接矩阵，
此矩阵的定义如下：对于一个图G=(V,E)，假设有n个顶点，n>=1，则可以将n个顶点的图使用一个n*n的二维矩阵来表示，其中A(i,j)=1，
则表示图中有一条边(Vi,Vj)存在，反之，A(i,j)=0，则不存在(Vi,Vj)。

相关特性说明如下：

（1）对无向图而言，邻接矩阵一定是对称的，而对角线一定为0。有向图则不一定如此。

（2）在无向图中，任意结点 i 的度数就是第 i 行所有元素的和。
     在有向图中，结点 i 的出度就是第 i 行所有元素之和；结点 j 的入度就是第 j 列所有元素之和。
     
（3）用邻接矩阵法表示图共需要 n^2 个单位空间，由于无向图的邻接矩阵具有对称关系的，扣除对角线全部为 0 外，
     仅需要存储上三角形数据即可，因此仅需要n(n-1)/2。
     
"""
# 以邻接矩阵来表示无向图
import numpy as np

# 返回某个顶点在顶点列表中的位置索引
def find_index(node, node_list):
    for i in range(len(node_list)):
        if node == node_list[i]:
            return i
    return -1

# 无向图的输入，采用二维数组, 存储边的二个顶点
data = [[1, 2], [1, 5], [2, 3], [2, 4], [3, 4], [3, 5],[4, 5]]

# 顶点列表
vertex_list = [1, 2, 3, 4, 5]

# 创建一个邻接矩阵
Adj_matrix = np.zeros((5, 5), dtype=int)
#Adj_matrix = [[0 for i in range(5)] for j in range(5)]
print("len(Adj_matrix) = ", len(Adj_matrix))

# 开始遍历图数据，生成邻接矩阵
for i in range(len(data)):
    temp1 = find_index(data[i][0], vertex_list)     # 找到顶点在顶点列表中的索引
    temp2 = find_index(data[i][1], vertex_list)
    Adj_matrix[temp1][temp2] = 1                    # 将有边的点出填入1
    Adj_matrix[temp2][temp1] = 1                    # 将有边的点出填入1

# 输出邻接矩阵
for i in range(len(Adj_matrix)):
    for j in range(len(Adj_matrix)):
        print(Adj_matrix[i][j], end='')                    # python的用法，在后面加“，”表示不换行。
    print ("")