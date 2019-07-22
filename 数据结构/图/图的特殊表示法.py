# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        图的特殊表示法
Description :   
Author :          wellqin
date:             2019/7/22
Change Activity:  2019/7/22
-------------------------------------------------
"""

# 利用python的基本数据结构类型
"""
1）邻接集合：第一种实现邻接表的方式是：针对每个结点设置一个邻居集合，在python中就是set。
"""
a, b, c, d, e, f, g, h = range(8)
Adj_set = [
            {b, c, d, e, f},
            {c, e},
            {d},
            {e},
            {f},
            {c, g, h},
            {f, h},
            {f, g}
]
# 列表中的每个集合是每个结点的邻接点集
print("邻接集合")
print(b in Adj_set[a])         # 结点b是否是结点a的邻居结点
print(len(Adj_set[a]))         # 结点a的出度


"""
2）邻接列表: 第二种实现邻接表的方式是：针对每个结点设置一个邻居列表，在python中就是list。
"""
Adj_list = [
            [b, c, d, e, f],
            [c, e],
            [d],
            [e],
            [f],
            [c, g, h],
            [f, h],
            [f, g]
]

print("邻接列表")
print(b in Adj_set[a])         # 结点b是否是结点a的邻居结点
print(len(Adj_set[a]))         # 结点a的出度


"""
3）加权的邻接字典:使用字典类型来代替集合或列表来表示邻接表。
   在字典类型中，每个邻居节点都会有一个键和一个额外的值，用于表示与其邻居节点（或出边）之间的关联性，如边的权重。
"""

Adj_dict_weight = [
                      {b: 2, c: 1, d: 3, e: 9, f: 4},
                      {c: 4, e: 3},
                      {d: 8},
                      {e: 7},
                      {f: 5},
                      {c: 2, g: 2, h: 2},
                      {f: 1, h: 6},
                      {f: 9, g: 8}
]

print("加权的邻接字典")
print (b in Adj_dict_weight[a])         # 结点b是否是结点a的邻居结点
print (len(Adj_dict_weight[a]))         # 结点a的出度
print (Adj_dict_weight[a][b])           # 边（a,b）的权重 ==> b: 2


"""
4）邻接集字典: 以上图的表示方法都使用了list类型，其实，也可以使用字典结构dict和集合结构set的嵌套来实现。
"""
Adj_set_dict = {'a':set('bcdef'),
     'b':set('ce'),
     'c':set('d'),
     'd':set('e'),
     'e':set('f'),
     'f':set('cgh'),
     'g':set('fh'),
     'h':set('fg')
}

print("邻接集字典")
print (Adj_set_dict["a"])            # 节点a的邻居节点
print ("b" in Adj_set_dict["a"])     # 节点b是否是节点a的邻居节点


"""
5）嵌套字典（最重要*****）: 也可以使用嵌套字典的方式来实现加权图。
"""
Nest_dict = {'a':{'b':2, 'c':1, 'd':3, 'e':9, 'f':4},
     'b':{'c':4, 'e':3},
     'c':{'d':8},
     'd':{'e':7},
     'e':{'f':5},
     'f':{'c':2, 'g':2, 'h':2},
     'g':{'f':1, 'h':6},
     'h':{'f':9, 'g':8}
}
print("嵌套字典")
print (Nest_dict["a"])            # 节点a的邻居节点
print ("b" in Nest_dict["a"])     # 节点b是否是节点a的邻居节点

