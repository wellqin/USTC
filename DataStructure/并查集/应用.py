# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        应用
Description :   
Author :          wellqin
date:             2019/7/25
Change Activity:  2019/7/25
-------------------------------------------------
"""
"""
背景问题：给定一些好友的关系，求这些好友关系中，存在多少个朋友圈？
例如给定好友关系为：[0,1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]。在这些朋友关系中，存在3个朋友圈，分别是
【0,1,2,3,4】，【5,6,7】，【8,9】
"""

def union_find(edges):
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])

    node_father = {}
    for node in nodes:
        node_father[node] = node

    for edge in edges:
        if node_father[edge[1]] == edge[1]:
            node_father[edge[1]] = edge[0]
        else:
            node_father[edge[0]] = edge[1]

    print(node_father)

    for node in nodes:
        father = node_father[node]
        print(node)
        while father != node_father[father]:
            father = node_father[father]
        node_father[node] = father
    return len([node_father.keys()]), node_father


if __name__ == '__main__':
    nodes = list(range(0, 10))
    test_edges = [[0,1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]
    test_edges2 = [[1, 2], [3, 2], [4, 2]]
    n, pyq = union_find(test_edges)
    print(n, ' ', pyq)