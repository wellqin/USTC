#现在你总共有 n 门课需要选，记为 0 到 n-1。 
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1] 
#
# 给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？ 
#
# 示例 1: 
#
# 输入: 2, [[1,0]] 
#输出: true
#解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。 
#
# 示例 2: 
#
# 输入: 2, [[1,0],[0,1]]
#输出: false
#解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。 
#
# 说明: 
#
# 
# 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。 
# 你可以假定输入的先决条件中没有重复的边。 
# 
#
# 提示: 
#
# 
# 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。 
# 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。 
# 
# 拓扑排序也可以通过 BFS 完成。 
# 
# 
#
# todo
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

def topsort(G):
    in_degrees = dict((u, 0) for u in G)
    for u in G:
        for v in  G[u]:
            in_degrees[v] += 1          # 每一个节点的入度
    Q = [u for u in G if in_degrees[u] == 0]          # 入度为 0 的节点
    S = []
    while Q:
        u = Q.pop()                  # 默认从最后一个移除
        S.append(u)
        for v in G[u]:
            in_degrees[v] -= 1           # 并移除其指向
            if in_degrees[v] == 0:
                Q.append(v)
    if len(S) == len(in_degrees):  # 如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
        return S
    else:
        return -1

G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
G1 = { 'a':'bce', 'b':'d','c':'d','d':'e','e':'cd'}
print(topsort(G))
print(topsort(G1))