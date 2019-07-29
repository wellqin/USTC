# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        并查集实现
Description :   
Author :          wellqin
date:             2019/7/25
Change Activity:  2019/7/25
-------------------------------------------------
"""

"""
并查集是一种数据结构，形象地来说，有点像“朋友圈”：
A和B是朋友，A和B就构成了一个朋友圈，C和D是朋友，C和D也构成了一个朋友圈，那么这时，如果B和C在成为了朋友，A、B、C、D就构成了一个大的朋友圈。

现实生活中和稀松平常的现象，到了用计算机描述的时候，往往显得不是那么容易，二者常存在着一条鸿沟，而正是考验我们智慧的时候。

回到“朋友圈”，的问题上，在现实生活中，我们是怎样判断酒桌上认识的新朋友是不是同一个圈子里的人的呢？
常用的一个办法是提一些自己圈子里比较有知名度的人，如果彼此圈子里都有这样同一个人，就可以判定彼此是同一个圈子里的人了。
"""

class UnionFind(object):
    """并查集类,将列表每一个结点初始化为-1，列表的结点值为负数表示它自己就是根结点，这样做还有一个好处可以用-n表示自己的子结点的数量"""
    def __init__(self, n):
        """长度为n的并查集"""
        self.uf = [-1 for i in range(n)]    # 列表0位置空出，并查集里的元素，代表朋友圈里每一个人，保存的数字代表其最知名朋友的id，初始状态，每个人的圈子只有自己一个人，等于自己
        self.sets_count = n                     # 判断并查集里共有几个集合, 初始化默认互相独立，并查集的大小，即朋友圈的的数量

    # def find(self, p):
    #     """查找p的根结点(祖先)"""                 # 查找我（p）的掌门
    #     r = p                                   # 初始p， 委托r去找掌门
    #     while self.uf[p] > 0:
    #         p = self.uf[p]
    #     while r != p:                           # 路径压缩, 把搜索下来的结点祖先全指向根结点，如果r的上级不是r自己（也就是说找到的大侠他不是掌门 = =）
    #         self.uf[r], r = p, self.uf[r]       # r 就接着找他的上级，直到找到掌门为止。
    #     return p

    # def find(self, p):
    #     while self.uf[p] >= 0:
    #         p = self.uf[p]
    #     return p

    def find(self, p):
        """尾递归,查找p所在的圈子，以圈子里最有名的朋友为标志"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p，并保证并查集不会退化成了一个链表的结构""" # 我想让虚竹和周芷若做朋友,a、b成为了新朋友，为此需要改变朋友圈的状态。
        """合并操作   优化可以使用：路径压缩"""
        proot = self.find(p)
        qroot = self.find(q)                    # 虚竹的老大是玄慈，芷若MM的老大是灭绝
        if proot == qroot:                      # 如果两人其实早就是同一个圈子里的人，就无需进行操作了
            return
        elif self.uf[proot] > self.uf[qroot]:   # 负数比较, 左边规模更小， 玄慈和灭绝显然不是同一个人,如果不是，那么所有和a在同一个圈子里的人，全部并入b的圈子
            self.uf[qroot] += self.uf[proot]    # 根据圈子大小选择合并操作，总是将小圈子融入大圈子。
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1                    # 连通后集合总数减一,二个集合，合并之后，就是一个圈子集合了
        return self.uf , self.sets_count

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find(p) == self.find(q)     # 即判断两个结点是否是属于同一个祖先  = 用于检查a，b二人是否是同一个圈子里的人

# 结点数
n = 10

# 边数据
data = [[0, 9], [9, 3], [1, 2], [2, 8], [4, 5], [6, 7], [0, 5], [6, 8]]
# data = [[0,1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]

ss = UnionFind(n)

for edge in data:
    print(ss.union(edge[0], edge[1]))
    list_1 = ss.union(edge[0], edge[1])
print(ss.is_connected(1,7))

ex = [-5, 0, 0, 0, 0, -3, 5, 5, -2, 8]   # self.uf = [-1 for i in range(n+1)] 改为range(n)
print(len(list(filter(lambda x:x<0, ex))))

"""
Pyhton2.7 返回列表，Python3.x 返回迭代器对象
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
a = filter(lambda x: x % 2 == 0, range(10))
print(a)  # <filter object at 0x0000022EC66BB128>
"""