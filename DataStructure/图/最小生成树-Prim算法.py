# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        最小生成树-Prim算法
Description :   
Author :          wellqin
date:             2019/7/23
Change Activity:  2019/7/23
-------------------------------------------------
"""

"""
普里姆算法（Prim算法）是图论中的一种算法，可在加权连通图里搜索最小生成树。
意即由此算法搜索到的边子集所构成的树中，不但包括了连通图里的所有顶点，且其所有边的权值之和亦为最小

对于任意图，假设包含n个顶点，m条边。Prim算法是从顶点出发的，其算法时间复杂度与顶点数目有关系。
（注意：prim算法适合稠密图，其时间复杂度为O(n^2)，其时间复杂度与边得数目无关，
而Kruskal算法的时间复杂度为O(ElogE)跟边的数目有关，适合稀疏图。）

 

Prim算法是一种构造性算法。假设G=（V,E）是一个具有n个顶点的带权连通无向图，T=（U，TE）是G的最小生成树，
                        其中U是T的顶点集，TE是T的边集，则由G构造从起始顶点v出发的最小生成树T的步骤如下：

（a）初始化U={v},以v到其他顶点的所有边为候选边；
（b）重复以下步骤（n-1）次，使得其他（n-1）个顶点被加入到U中：
   （1）从侯选边中挑选权值最小的边加入TE，设该边在V-U中的顶点是k，将k加入U中；（加入后不能形成环）
   （2）考察当前V-U中所有顶点j，修改侯选边，若边（k，j）的权值小于原来和顶点j关联的侯选边，则用边（k，j）取代后者作为侯选边。
       （加入后不能形成环）
"""

Graph = {'A': {'B': 6, 'E': 10, 'F': 12},
         'B': {'A': 6, 'C': 3, 'D': 5, 'F': 8},
         'C': {'B': 3, 'D': 7},
         'D': {'B': 5, 'C': 7, 'E': 9, 'F': 11},
         'E': {'A': 10, 'D': 9, 'F': 16},
         'F': {'A': 12, 'B': 8, 'D': 11, 'E': 16},
         }

# python3改变了dict.keys,返回的是dict_keys对象,支持iterable 但不支持indexable，我们可以将其明确的转化成list：
# V = set(G.keys())[0]
# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
"""
语法：set.difference(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
 
z = x.difference(y) 
 
print(z)  # {'cherry', 'banana'}返回一个集合，元素包含在集合 x ，但不在集合 y ：
"""
# python3改变了dict.keys,返回的是dict_keys对象,支持iterable 但不支持indexable，我们可以将其明确的转化成list：
# V = set(G.keys())[0]
# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
def Prim(G):
    U = set(G.keys())                        # 图G的顶点集合U，它包含了该图的所有顶点, 创建一个空集合必须用 set() 而不是 { }，
                                             # 因为 { } 是用来创建一个空字典。
    # V = set(list(U)[0])                      # 将起始顶点加入集合V,  集合对 list 和 tuple 具有排序(升序)
    V = set(('C',))
    min_tree = []                            # 存储要返回的最小生成树的所有的边
    cost = []                                # 记录最小生成树各边的权重的值

    while U.difference(V):                   # 当集合U和V不想等时，进入循环while U != V
        min_value = float("inf")             # 初始化一个最小值
        node1 = None                         # 用于记录加入边的第一个节点
        node2 = None                         # 用于记录加入边的第二个节点
        for v in V:                          # 遍历访问过的节点
            for u in U.difference(V):        # 遍历未访问过的节点
                if u in G[v]:                # 如果两个节点之间存在相连的边
                    if G[v][u] < min_value:  # 判断该值是否是所有访问过节点存在的相邻边中的最小值
                        min_value = G[v][u]  # 更新边权重的最小值
                        node1 = v            # 记录边权重最小值的第一个节点
                        node2 = u            # 记录边权重最小值的第二个节点

        V.add(node2)                         # 将第二个节点加入到访问过的节点集合V，因为第二个节点来自于未访问过的节点集合
        min_tree.append([node1, node2])      # 将包括两个节点的边加入到最小生成树边列表
        cost.append(min_value)               # 将边的权重加入到成本列表中

    print("普利姆Prim算法最小生成树：")
    print("各个边的权值: ", cost)
    print("最小生成树的成本: ", sum(cost))
    print("最小生成树的边: ", min_tree)
    return cost, min_tree




def PrimSelf(G):
    U = set(G.keys())
    V = set(list(U)[0])
    tree = []
    cost = []

    while U != V:
        min_value = float("inf")
        node1, node2 = None, None
        for v in V:
            for u in U.difference(V):
                if u in G[v]:
                    if G[v][u] < min_value:
                        min_value = G[v][u]
                        node1 = v
                        node2 = u

        V.add(node2)
        tree.append([node1, node2])
        cost.append(min_value)


if __name__ == '__main__':
    Prim(Graph)


"""
运行结果如下：
普利姆Prim算法最小生成树：
各个边的权值: [6, 3, 5, 8, 9]
最小生成树的成本: 31
最小生成树的边: [['A', 'B'], ['B', 'C'], ['B', 'D'], ['B', 'F'], ['D', 'E']]
"""