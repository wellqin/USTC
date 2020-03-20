# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        最短路径问题-Dijkstra
Description :   
Author :          wellqin
date:             2019/7/24
Change Activity:  2019/7/24
-------------------------------------------------
"""

"""
迪杰斯特拉（Dijkstra）算法是一个按照路径长度递增的次序产生的最短路径算法。

其中，带权值的有向图采用邻接矩阵graph来进行存储，在计算中就是采用n*n的二维数组来进行存储，
v0-v5表示数组的索引编号0-5，二维数组的值表示节点之间的权值，若两个节点不能通行，
比如，v0->v1不能通行，那么graph[0,1]=+∞ （采用计算机中最大正整数来进行表示）。
那如何求解从v0每个v节点的最短路径长度呢?

首先，引进一个辅助数组cost，它的每个值cost[i]表示当前所找到的从起始点v0到终点vi的最短路径的权值（长度花费），
该数组的初态为：若从v0到vi有弧，则cost[i]为弧上的权值，否则置cost[i]为+∞ 。

显然，长度为：cost[j]=Min_i(graph[0,i] | v_i in V) 的路径就是从v0出发的长度最短的一条最短路径。
此路径为(v_0,v_j) ，那么下次长度次短的路径必定是弧(v_0,v_i)上的权值cost[i](v_i in V)，
或者是cost[k](v_k in S)和弧(v_k,v_i)的权值之和。其中V：待求解最短路径的节点j集合；S：已求解最短路径的节点集合。

根据上面的算法原理分析，下面描述算法的实现流程。

1.初始化：初始化辅助数组cost，从v0出发到图上其余节点v的初始权值为：cost[i]=graph[0,i]  |  v_i in V ；
初始化待求节点S集合，它的初始状态为始点，V集合，全部节点-始节点。

2.选择节点v_j ，使得cost[j]=Min ( cost[i] | v_i in V -S ) ，v_j  
就是当前求的一条从v0出发的最短路径的终点，修改S集合，使得 S=S + V_j ，修改集合V = V - V_j。

3.修改从v0出发到节点V-S上任一顶点 v_k 可达的最短路径，
若cost[j]+graph[j,k]<cost[k] ，则修改cost[k]为：cost[k]=cost[j]+graph[j,k] 。

4.重复操作2，3步骤，直到求解集合V中的所有节点为止。

其中最短路径的存储采用一个path整数数组，path[i]的值记录vi的前一个节点的索引，通过path一直追溯到起点，
就可以找到从vi到起始节点的最短路径。比如起始节点索引为0，若path[3]=4, path[4]=0；那么节点v2的最短路径为，v0->v4->v3。
"""


# def dijkstra(graph, startIndex, path, cost, max):
#     """
#     求解各节点最短路径，获取path，和cost数组，
#     path[i] 表示vi节点的前继节点索引，一直追溯到起点。
#     cost[i] 表示vi节点的花费
#     """
#     lenth = len(graph)
#     v = [0] * lenth
#     # 初始化 path，cost，V
#     for i in range(lenth):
#         if i == startIndex:
#             v[startIndex] = 1
#         else:
#             cost[i] = graph[startIndex][i]
#             path[i] = startIndex if (cost[i] < max) else -1
#     print("v = ", v, )
#     print("cost = ", cost)
#     print("path = ", path)
#
#     for i in range(1, lenth):
#         minCost = max
#         curNode = -1
#         for w in range(lenth):
#             if v[w] == 0 and cost[w] < minCost:
#                 minCost = cost[w]
#                 curNode = w
#         # for 获取最小权值的节点
#         if curNode == -1: break
#         # 剩下都是不可通行的节点，跳出循环
#         v[curNode] = 1
#         for w in range(lenth):
#             if v[w] == 0 and (graph[curNode][w] + cost[curNode] < cost[w]):
#                 cost[w] = graph[curNode][w] + cost[curNode]  # 更新权值
#                 path[w] = curNode  # 更新路径
#         # for 更新其他节点的权值（距离）和路径
#     return path, cost
#
#
# if __name__ == '__main__':
#     max = 2147483647
#     graph = [
#         [max, max, 10, max, 30, 100],
#         [max, max, 5, max, max, max],
#         [max, max, max, 50, max, max],
#         [max, max, max, max, max, 10],
#         [max, max, max, 20, max, 60],
#         [max, max, max, max, max, max],
#     ]
#     path = [0] * 6
#     cost = [0] * 6
#     print("dijkstra", dijkstra(graph, 0, path, cost, max))

# 利用最小堆实现, 时间复杂度: O(e * logv), e是边的个数

'''
Dijkstra算法(最短路径算法)

- 适用于有向有权无环图
- 不适用于负权边的情况
'''

import heapq


class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_edge(self, start: str, end: str, distance: float):
        self.graph.setdefault(start, {})  # setdefault() 函数和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
        self.graph[start][end] = distance


def dijkstra(start, end, graph):
    queue = []
    heapq.heappush(queue, (0, start))  # 初始化起点

    # 三个动态存储结构，邻接矩阵中用列表固定
    visited = set()  # 存储已经处理过的节点
    distance = {start: 0}
    parent = {}  # 用于复原路径

    while queue:
        dis, min_node = heapq.heappop(queue)  # 优先队列中取节点
        if min_node == end:  # 对于有向图，这里可以break了
            break
        visited.add(min_node)

        for i, j in graph[min_node].items():  # 检查节点邻居路径值
            new_dis = dis + j
            # 如果是新节点，或者到该点的距离比之前近，则进行更新
            if (i not in distance) or (new_dis < distance[i]):
                distance[i] = new_dis
                heapq.heappush(queue, (new_dis, i))
                parent[i] = min_node

    res = []
    while end != start:
        res.insert(0, end)
        end = parent[end]
    res.insert(0, start)
    return res


g1 = Graph()
G = [['start', 'a', 6], ['start', 'b', 2], ['b', 'a', 3], ['b', 'end', 5], ['a', 'end', 1]]
for i in G:
    g1.add_edge(*i)
print(g1.graph)
# g1.add_edge('start', 'a', 6)
# g1.add_edge('start', 'b', 2)
# g1.add_edge('b', 'a', 3)
# g1.add_edge('b', 'end', 5)
# g1.add_edge('a', 'end', 1)

# G = {'start': {'a': 6, 'b': 2},
#      'a': {'end': 1},
#      'b': {'end': 5, 'a': 3}
#      }

print(dijkstra('start', 'end', g1.graph))

g2 = Graph()
g2.add_edge('start', 'a', 5)
g2.add_edge('start', 'b', 2)
g2.add_edge('b', 'a', 1)
g2.add_edge('b', 'end', 5)
g2.add_edge('a', 'end', 1)
# assert dijkstra('start', 'end', g2.graph) == ['start', 'b', 'a', 'end']
