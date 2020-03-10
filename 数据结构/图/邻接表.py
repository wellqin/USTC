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
    def __init__(self, data):            # 构造函数
        self.data = data              # 结点的数据域
        self.next = None           # 结点的指针域

#顶点列表
vertex_list = [1, 2, 3, 4, 5]
heads = []
data = [[1, 2], [2, 1], [1, 5], [5, 1], [2, 3], [3, 2], [2, 4], [4, 2],
        [3, 4], [4, 3], [3, 5], [5, 3], [4, 5], [5, 4]]

print(len(data))
print( "图的邻接表的内容")
print( "-----------------------------------------------------")

for i in range(len(vertex_list)):
    head = list_node(None)
    head.data = vertex_list[i]            # 生成头结点，以五个顶点作为头结点
    head.next = None

    for j in range(len(data)):
        if data[j][0] == vertex_list[i]:       # 输入数据中的起始结点等于顶点，就在终止结点加入到该顶点的邻接链表中去。
            newnode = list_node(data[j][1])    # 为终止顶点创建一个结点信息，并将其元素值加入到数据域中
            cur = head
            while cur.next:
                cur= cur.next              # 这是尾部插入法
            cur.next = newnode
    heads.append(head)

for head in heads:
    while head:
        print(head.data, end='')
        head = head.next
    print("")

"""
运行结果如下：

-----------------------------------------------------
顶点 1 => [2]  [5]  
顶点 2 => [1]  [3]  [4]  
顶点 3 => [2]  [4]  [5]  
顶点 4 => [2]  [3]  [5]  
顶点 5 => [1]  [3]  [4]

"""