# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        BDS
Description :   
Author :          wellqin
date:             2019/7/26
Change Activity:  2019/7/26
-------------------------------------------------
"""
from collections import deque
# graph is in adjacent list representation
graph = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

# graph is in adjacent list representation
graph1 = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [4, 11],
    5: [9, 10],
    4: [7, 8],
    7: [11, 12]
}


def bfs(graph, start, end):
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        for adj in graph.get(node, []):
            new_path = list(path)
            new_path.append(adj)
            queue.append(new_path)

print(bfs(graph, '1', '11'))




def bfs(graph, start, end):
    queue = []
    allpath = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            allpath.append(path)
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return allpath


print(bfs(graph1, 1, 11))

