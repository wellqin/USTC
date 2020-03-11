# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        图的DFS+BFS
Description :   
Author :          wellqin
date:             2019/7/22
Change Activity:  2019/7/22
-------------------------------------------------
"""

"""
深度优先遍历也称为深度优先搜索（Depth First Search），它类似于树的先序遍历，
具体定义如下：
假设初始状态是图中所有顶点均未被访问，则从某个顶点v出发，首先访问该顶点，
然后依次从它的各个未被访问的邻接点出发深度优先搜索遍历图，直至图中所有和v有路径相通的顶点都被访问到。 
若此时尚有其他顶点未被访问到，则另选一个未被访问的顶点作起始点，重复上述过程，直至图中所有顶点都被访问到为止。

深度优先遍历的定义就是一个递归的过程，每次都以当前节点的第一个未曾访问过的邻接点进行深度优先遍历的过程。
因此使用递归函数实现该算法是最直观的实现方式，但由于递归的过程是函数栈累积的过程，如果节点数较多，
容易造成函数栈的溢出而导致程序崩溃，因此正常生产环境一般会使用一个栈结构（Stack）来存放遍历的节点以模拟函数栈的调用情况，
以此避免递归的缺陷。
"""

"""
深度优先算法：

（1）访问初始顶点v并标记顶点v已访问。
（2）查找顶点v的第一个邻接顶点w。
（3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。
（4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。
（5）继续查找顶点w的下一个邻接顶点wi，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。
"""
# 创建一个图, 散列表让你能够将键映射到值。在这里，你要将节点映射到其所有邻居。
# 键—值对的添加顺序重要吗？没影响。散列表是无序的，因此添加键—值对的顺序无关紧要。
Graph = {}
Graph['A'] = ['B', 'C', 'D']
Graph['B'] = ['A', 'E']
Graph['C'] = ['A', 'F']
Graph['D'] = ['A', 'G', 'H']
Graph['E'] = ['B', 'F']
Graph['F'] = ['E', 'C']
Graph['G'] = ['D', 'H', 'I']
Graph['H'] = ['G', 'D']
Graph['I'] = ['G']


# 使用堆栈来实现深度优先遍历
def DFSTraverse(G, start):
    res = []
    stack = [start]  # 初始化一个堆栈并将起始结点入栈
    visited = set()  # 初始化一个访问过的节点集合

    while stack:  # 如果栈不为空，进入循环
        node = stack.pop()  # 栈顶元素出栈
        if node in visited:
            continue  # 判断栈顶元素是否被访问过，元素被访问过，跳出循环,查看栈内的其他元素
        else:  # 栈顶元素未被访问
            res.append(node)  # 保存访问的栈顶元素（遍历结果）
            visited.add(node)  # 将其加入访问过的集合
            # 将该元素的邻居节点加入到栈中去，加整体中的序列用extend，分开写用append
            stack.extend(adj for adj in G[node] if adj not in visited)
    return res


# def DFSTraverse(G, start):
#     res = []
#     stack = [start]
#     visited = set()
#     while stack:
#         node = stack.pop()
#         if node in visited: continue
#         else:
#             res.append(node)
#             visited.add(node)
#             stack.extend(adj for adj in G[node] if adj not in visited)
#     return res

# 自定义遍历初始点
print(DFSTraverse(Graph, 'A'))
# DFS ['A', 'D', 'H', 'G', 'I', 'C', 'F', 'E', 'B']


# 使用队列来实现广度优先遍历,  需要按添加顺序进行检查。有一个可实现这种目的的数据结构，那就是队列（queue）。
# 广度优先搜索的运行时间为O(顶点数 + 边数)，这通常写作O(V + E)，其中V为顶点（vertice）数，E为边数。
"""
你需要按加入顺序检查搜索列表中的人，否则找到的就不是最短路径，因此搜索列表必须是队列。
对于检查过的人，务必不要再去检查，否则可能导致无限循环。
"""


def BFSTraverse(G, start):
    res = []
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop(0)
        if node in visited:
            continue
        else:
            res.append(node)
            visited.add(node)
            stack.extend(adj for adj in G[node] if adj not in visited)
    return res


print(BFSTraverse(Graph, 'A'))
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


from collections import deque


def BFSTraverse1(G, start):
    queue = deque()  # 初始化一个队列， 函数deque来创建一个双端队列。
    visited = set()  # 初始化一个存储访问过元素的集合， 检查之前，要确认之前没检查过他，这很重要。为此，你可使用一个列表来记录检查过的人。
    # 如果不这样做，就可能会导致无限循环
    queue.append(start)  # 将起始结点加入队列
    while queue:  # 当队列不为空时，进入循环
        node = queue.popleft()  # 将队列的队首元素出队
        if node in visited:  # 判断该元素是否被访问过，如果访问过，跳出本次循环
            continue
        else:
            print(node + "-", end='')
            visited.add(node)
            for adj in G[node]:
                if adj not in visited:
                    queue.append(adj)  # 将该节点的所有邻居加入队列
