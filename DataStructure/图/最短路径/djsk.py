# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        djsk
Description :   
Author :          wellqin
date:             2020/3/11
Change Activity:  2020/3/11
-------------------------------------------------
"""


# graph是表示各顶点距离的矩阵，v0是起始点，P[v]的值为前驱点坐标，D[v]表示v0到v的最短路径长度和
def Dijkstra(G, v0):
    n = len(G)
    visited, distacnce, parent = [False] * n, [0] * n, [0] * n

    for i in range(n):  # 初始化起点与周围距离
        distacnce[i] = G[v0][i]
    distacnce[v0] = 0  # [0, inf, 10, inf, 30, 100]
    visited[v0] = True  # 起点已经访问过

    for v in range(1, n):
        minV = float("Inf")
        curNode = -1
        for w in range(0, n):
            if not visited[w] and distacnce[w] < minV:
                curNode = w
                minV = distacnce[w]

        if curNode == -1: break
        visited[curNode] = True
        # 更新其他节点的权值（距离）和路径
        for w in range(0, n):
            if not visited[w] and minV + G[curNode][w] < distacnce[w]:
                distacnce[w] = minV + G[curNode][w]
                parent[w] = curNode
    return distacnce


# 前面这部分都是在构造equations矩阵
max = float("inf")
graph = [
    [max, max, 10, max, 30, 100],
    [max, max, 5, max, max, max],
    [max, max, max, 50, max, max],
    [max, max, max, max, max, 10],
    [max, max, max, 20, max, 60],
    [max, max, max, max, max, max],
]

res = Dijkstra(graph, 0)
print('最短路径', res)
# 输出结果：[0, 1, 4, 7, 5, 8, 10, 12, 16]
