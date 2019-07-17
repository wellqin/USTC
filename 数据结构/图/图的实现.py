# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        图的实现
Description :   
Author :          wellqin
date:             2019/7/14
Change Activity:  2019/7/14
-------------------------------------------------
"""


"""
 下面展示了 Vertex 类的代码。构造函数只是初始化 id ，通常是一个字符串和 connectedTo 字典。 
 addNeighbor 方法用于从这个顶点添加一个连接到另一个。
 getConnections 方法返回邻接表中的所有顶点，如 connectedTo 实例变量所示。 
 getWeight 方法返回从这个顶点到作为参数传递的顶点的边的权重。
"""


class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


"""
下面展示了 Graph 类的代码，包含将顶点名称映射到顶点对象的字典。Graph 还提供了将顶点添加到图并将一个顶点连接到另一个顶点的方法。
getVertices方法返回图中所有顶点的名称。此外，我们实现了__iter__ 方法，以便轻松地遍历特定图中的所有顶点对象。 
这两种方法允许通过名称或对象本身在图形中的顶点上进行迭代。
"""

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
g.vertList

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))























