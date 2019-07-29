# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        bellman-Ford
Description :   
Author :          wellqin
date:             2019/7/25
Change Activity:  2019/7/25
-------------------------------------------------
"""

"""
Bellman-Ford是一种容易理解的单源最短路径算法, Bellman-Ford算法需要两个数组进行辅助:

    dis[i]: 存储顶点i到源点已知最短路径
    path[i]: 存储顶点i到源点已知最短路径上, i的前一个顶点.
    
若图有n个顶点, 则图中最长简单路径长度不超过n-1, 因此Ford算法进行n-1次迭代确保获得最短路径.

Ford算法的每次迭代遍历所有边, 并对边进行松弛(relax)操作. 对边e进行松弛是指: 
    若从源点通过e.start到达e.stop的路径长小于已知最短路径, 则更新已知最短路径.

为了便于描述, 本文采用python实现算法. 首先实现两个工具函数:make_mat//get_edges
make_mat用于初始化二维数组, get_edges用于将图由邻接矩阵表示变换为边的列表.
"""

def make_mat(m, n, fill=None):
    mat = []
    for i in range(m):
        mat.append([fill] * n)
    return mat


INF = 1e6


def get_edges(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    return edges


def show(path, start, stop):
    i = stop
    tmp = [stop]
    while i != start:
        i = path[i]
        tmp.append(i)
    return list(reversed(tmp))

"""
初始化后执行迭代和松弛操作, 非常简单.

由path[i]获得最短路径的前驱顶点, 逐次迭代得到从顶点i到源点的最短路径. 倒序即可得源点到i的最短路径.


Ford算法允许路径的权值为负, 但是若路径中存在总权值为负的环的话, 每次经过该环最短路径长就会减少. 
因此, 图中的部分点不存在最短路径(最短路径长为负无穷).

若路径中不存在负环, 则进行n-1次迭代后不存在可以进行松弛的边. 因此再遍历一次边, 若存在可松弛的边说明图中存在负环.
"""
def ford(graph, v0):
    n = len(graph)
    edges = get_edges(graph)
    dis = [INF] * n
    dis[v0] = 0
    path = [0] * n

    for k in range(n-1):
        for edge in edges:
            # relax
            if dis[edge[0]] + edge[2] < dis[edge[1]]:
                dis[edge[1]] = dis[edge[0]] + edge[2]
                path[edge[1]] = edge[0]

    # check negative loop
    flag = False
    for edge in edges:
        # try to relax
        if dis[edge[0]] + edge[2] < dis[edge[1]]:
            flag = True
            break
    if flag:
        return False
    return dis, path


if __name__ == '__main__':
    graph = make_mat(5, 5, fill=INF)
    graph[0][1] = -1
    graph[0][2] = 3
    graph[1][2] = 3
    graph[1][3] = 2
    graph[1][4] = 2
    graph[3][1] = 1
    graph[3][2] = 5
    graph[4][3] = -3

    dis, path = ford(graph, 0)

    v0 = 0
    for i in range(len(graph)):
        if i == v0:
            continue
        print("%d->%d: " % (v0, i), end="")
        print(show(path, v0, i))
        print(dis[i])