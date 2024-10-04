# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        最小生成树-贪心Kruskal-是基于并查集的贪心算法。
Description :   
Author :          wellqin
date:             2019/7/23
Change Activity:  2019/7/23
-------------------------------------------------
"""

"""
Kruskal算法是一种用来查找最小生成树的算法，它是基于贪心的思想得到的。

首先我们把所有的边按照权值先从小到大排列，接着按照顺序选取每条边，
如果这条边的两个端点不属于同一集合，那么就将它们合并，直到所有的点都属于同一个集合为止。
至于怎么合并到一个集合，那么这里我们就可以用到一个工具——-并查集。换而言之，Kruskal算法就是基于并查集的贪心算法。

Kruskal算法每次要从都要从剩余的边中选取一个最小的边。通常我们要先对边按权值从小到大排序，
这一步的时间复杂度为为O(|Elog|E|)。Kruskal算法的实现通常使用并查集，来快速判断两个顶点是否属于同一个集合。
最坏的情况可能要枚举完所有的边，此时要循环|E|次，所以这一步的时间复杂度为O(|E|α(V))，其中α为Ackermann函数，
其增长非常慢，我们可以视为常数。所以Kruskal算法的时间复杂度为O(|Elog|E|)，其中E和V分别是图的边集和点集。

因此，使用Kruskal算法查找最小生成树的代码如下
"""

Graph = {'A': {'B': 6, 'E': 10, 'F': 12},
         'B': {'A': 6, 'C': 3, 'D': 5, 'F': 8},
         'C': {'B': 3, 'D': 7},
         'D': {'B': 5, 'C': 7, 'E': 9, 'F': 11},
         'E': {'A': 10, 'D': 9, 'F': 16},
         'F': {'A': 12, 'B': 8, 'D': 11, 'E': 16},
}

def Kruskal(G):
    record_node = set()    # 记录添加的边节点,重复的会忽略
    mintree = []           # 最小生成树的所有的边
    cost = []
    edges = []             # 获得图的所有的边，并对它排序

    for key1 in G.keys():
        for key2 in G[key1].keys():
            edges.append([key1, key2, G[key1][key2]])
    edges = sorted(edges, key=lambda x:x[2], reverse=True)     # 边的权值降序排列

    while edges:
        edge = edges.pop()  # edge = ["B", "C", 3] 形式         # 选取最短的边
        if (edge[0] in record_node) and (edge[1] in record_node):
            # 如果这两个顶点同时在集合中，表示会形成环路，不能加入这条边
            continue
        else:
            record_node.add(edge[0])  # "B"
            record_node.add(edge[1])  # "C"
            cost.append(edge.pop())   #  3
            mintree.append(edge)      # ["B", "C"]

    print ("各个边的权值: ", cost)  # [3, 5, 6, 8, 9]
    print ("最小生成树的成本: ", sum(cost))
    print ("最小生成树的边: ", mintree)
    # [['B', 'C'], ['B', 'D'], ['B', 'A'], ['B', 'F'], ['E', 'D']]
    return cost, mintree

if __name__ == '__main__':
    cost,mintree = Kruskal(Graph)
    print ("\n")


"""
运行结果如下：

克鲁斯卡尔Kruskal算法最小生成树：
各个边的权值:  [3, 5, 6, 8, 9]
最小生成树的成本:  31
最小生成树的边:  [['B', 'C'], ['D', 'B'], ['B', 'A'], ['F', 'B'], ['D', 'E']]
"""