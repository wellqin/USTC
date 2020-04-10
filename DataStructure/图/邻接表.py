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

for i in range(len(vertex_list)):
    # head = [list_node] * len(vertex_list) 这样在外面声明弊端很大
                                               # 1. 生成头结点，以五个顶点作为头结点
    head = list_node(vertex_list[i])           # 在内单个申明，防止节点在同一个位置，同时粘连变更

    for j in range(len(data)):
        if data[j][0] == vertex_list[i]:       # 2. 找到以当前头结点开始的边了
            newnode = list_node(data[j][1])    # 3. 生成边所对应的顶点（链表节点）

            cur = head                         # 4. 尾部插入
            while cur.next:
                cur= cur.next
            cur.next = newnode
    heads.append(head)                         # 加入到整体列表中进行保存

# 遍历保存的链表节点
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