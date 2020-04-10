# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        creatLinkList
Description :   
Author :          wellqin
date:             2020/2/16
Change Activity:  2020/2/16
-------------------------------------------------
"""


class Node(object):
    """节点"""

    def __init__(self, val):
        self.val = val
        self.next = None  # 初始设置下一节点为空


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def travel(self):
        """遍历整个列表"""
        cur = self.__head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print("\n")


obj = SingleLinkList()
# 头插法
for i in range(6):
    obj.add(i)
obj.travel()  # 5 4 3 2 1 0
# 尾插法
for j in range(6, 11):
    obj.append(j)
obj.travel()  # 5 4 3 2 1 0 6 7 8 9 10
