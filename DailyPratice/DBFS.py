# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        DBFS
Description :   
Author :          wellqin
date:             2020/3/16
Change Activity:  2020/3/16
-------------------------------------------------
"""

Graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E'],
         'C': ['A', 'F'],
         'D': ['A', 'G', 'H'],
         'E': ['B', 'F'],
         'F': ['E', 'C'],
         'G': ['D', 'H', 'I'],
         'H': ['G', 'D'],
         'I': ['G']
         }


# def DFS(G, start):
#     res, stack, visited = [], [start], set()
#     while stack:
#         node = stack.pop()
#         if node in visited:
#             continue
#         else:
#             res.append(node)
#             visited.add(node)
#             # for i in G[node]:
#             #     if i not in visited:
#             #         stack.append(i)
#             stack.extend(i for i in G[node] if i not in visited)
#
#     return res
#
#
# print(DFS(Graph, 'A'))
#
#
# def BFS(G, start):
#     import collections
#     res, queue, visited = [], collections.deque(), set()
#     queue.append(start)  # deque来创建一个双端队列
#     while queue:
#         node = queue.popleft()
#         if node in visited:
#             continue
#         else:
#             res.append(node)
#             visited.add(node)
#             queue.extend(i for i in G[node] if i not in visited)
#
#     return res
#
#
# print(BFS(Graph, 'A'))

def DFS(G, start):
    res, stack = [], [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        else:
            res.append(node)
            visited.add(node)
            stack.extend(i for i in G[node] if i not in visited)
    return res

print(DFS(Graph, 'A'))

