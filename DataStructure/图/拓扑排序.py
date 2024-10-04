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
    in_degrees = dict((u, 0) for u in G)  # {'a': 0, 'e': 0, 'c': 0, 'd': 0, 'b': 0}
    for u in G:
        for v in  G[u]:
            in_degrees[v] += 1  # 每一个节点的入度  每一个节点的入度 {'a': 0, 'e': 1, 'c': 2, 'd': 3, 'b': 2}
    stack = [u for u in G if in_degrees[u] == 0]   # 入度为 0 的节点
    res = []
    while stack:
        cur = stack.pop()
        res.append(cur)
        for v in G[cur]:
            in_degrees[v] -= 1   # 并移除其指向，删除度数为0节点，其他相邻节点入度减1
            if in_degrees[v] == 0:
                stack.append(v)

    # 如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
    if len(res) == len(in_degrees):
        return res
    else:
        return "there's a circle."

G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
G1 = {
    'a':'bce',
    'b':'d',
    'c':'db',
    'd':'',
    'e':'cd'
}
# print(topsort(G))
print(topsort(G1))