# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        拓扑排序
Description :   
Author :          wellqin
date:             2019/7/26
Change Activity:  2019/7/26
-------------------------------------------------
"""

def topsort(G):
    in_degrees = dict((u, 0) for u in G)
    for u in G:
        for v in  G[u]:
            in_degrees[v] += 1          # 每一个节点的入度
    Q = [u for u in G if in_degrees[u] == 0]          # 入度为 0 的节点
    S = []
    while Q:
        u = Q.pop()                  # 默认从最后一个移除
        S.append(u)
        for v in G[u]:
            in_degrees[v] -= 1           # 并移除其指向
            if in_degrees[v] == 0:
                Q.append(v)
    if len(S) == len(in_degrees):  # 如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
        return S
    else:
        return -1

G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
G1 = { 'a':'bce', 'b':'d','c':'d','d':'e','e':'cd'}
print(topsort(G))
print(topsort(G1))