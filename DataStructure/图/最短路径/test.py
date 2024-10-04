# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/27
Change Activity:  2019/7/27
-------------------------------------------------
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

"""
我将讨论的第一个算法是深度优先搜索，正如名称提示的，在回溯之前探索每个分支的可能顶点（通过提供的根节点）。
此属性允许以迭代和递归形式简洁地实现算法。下面列出了每次访问节点时执行的操作。
"""

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for it in graph[vertex] - set(path):
            if it == goal:
                yield path + [it]
            else:
                stack.append((it, path + [it]))

print(list(dfs_paths(graph, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]


"""
另一种称为广度优先搜索的算法使我们能够返回与深度优先搜索相同的结果，但增加了保证首先返回最短路径的能力。 
使用队列数据结构以递归方式实现此算法有点棘手，因此我将仅记录迭代方法。 每个探索顶点执行的操作与深度优先实现相同，
但是，使用队列替换堆栈将改为在移动之前探索顶点深度的宽度。
 此行为可确保位于的第一条路径是存在的最短路径之一，基于作为成本因子的边数。


"""

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

shortest_path(graph, 'A', 'F') # ['A', 'C', 'F']

