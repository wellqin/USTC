# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        小白图
Description :   
Author :          wellqin
date:             2019/7/22
Change Activity:  2019/7/22
-------------------------------------------------
"""
"""
图的python实现
在Python中，图主要是通过列表和词典来构造。比如说下面这张图，
     A --> B
     A --> C
     B --> C
     B --> D
     C --> D
     D --> C
     E --> F
     F --> C

就是通过下面这个字典和列表的结合进行构造
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

实现的功能：
寻找一条路径
查找所有的路径
查找最短路径

完整的代码实现：
# -*- encoding:utf-8 -*-
'''

 A --> B
 A --> C
 B --> C
 B --> D
 C --> D
 D --> C
 E --> F
 F --> C

'''
"""

def find_path(graph, start, end, path=[]):
        '寻找一条路径'
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return path

def find_all_paths(graph, start, end, path=[]):
        '查找所有的路径'
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph.keys():
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        '查找最短路径'
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#test

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    print (find_path(graph,'A','D'))
    print (find_all_paths(graph,'A','D'))
    print (find_shortest_path(graph,'A','D'))