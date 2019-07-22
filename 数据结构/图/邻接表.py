# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        邻接表
Description :   
Author :          wellqin
date:             2019/7/22
Change Activity:  2019/7/22
-------------------------------------------------
"""

class list_node(object):           # 定义一个结点类
    def __init__(self):            # 构造函数
        self.data = 0              # 结点的数据域
        self.next = None           # 结点的指针域

#顶点列表
vertex_list = [1, 2, 3, 4, 5]
head = [list_node] * len(vertex_list)        # 声明一个结点类型的列表
newnode = list_node()
data = [[1, 2], [2, 1], [1, 5], [5, 1], [2, 3], [3, 2], [2, 4], [4, 2], [3, 4], [4, 3], [3, 5], [5, 3], [4, 5], [5, 4]]

print(len(data))
print( "图的邻接表的内容")
print( "-----------------------------------------------------")

for i in range(len(vertex_list)):            # 生成头结点，以五个顶点作为头结点
    head[i].data = vertex_list[i]             # 分别将顶点列表的各个顶点元素存入头结点的数据域中
    head[i].next = None                       # 头结点指针域指向None
    print( "顶点 %d =>" % vertex_list[i])       # 打印头结点信息
    for j in range(len(data)):                # 遍历整个传入的图的数据，通过它创建图的邻接链表结构
        if data[j][0] == vertex_list[i]:       # 输入数据中的起始结点等于顶点，就在终止结点加入到该顶点的邻接链表中去。
            newnode.data = data[j][1]           # 为终止顶点创建一个结点信息，并将其元素值加入到数据域中
            # newnode.next = None         # 采用头部插入的方式，插入该结点
            head[i].next = newnode              # 这是头部插入法
            print( "[%d] " % newnode.data, end='')       # 循环打印属于某一头结点邻接结点的所有数据元素。
    print ("")                                    # 表示换行


"""
运行结果如下：

-----------------------------------------------------
顶点 1 => [2]  [5]  
顶点 2 => [1]  [3]  [4]  
顶点 3 => [2]  [4]  [5]  
顶点 4 => [2]  [3]  [5]  
顶点 5 => [1]  [3]  [4]

"""