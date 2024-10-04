# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        链表实现栈
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""

'''
链表（Linked List）
堆栈的链表实现插到元素前面，因此都是对第一个节点进行操作
下面模块导入自我的链表学习笔记代码
'''


class Node(object):
    """节点"""

    def __init__(self, val=None):
        self.val = val
        self.next = None  # 初始设置下一节点为空


class LinkedStack(object):
    def __init__(self, size):
        self.head = Node()
        self.top = -1
        self.size = size

    def size(self):
        if self.is_empty:
            return 0
        else:
            count = 0
            cur = self.head
            while cur:
                count += 1
                cur = cur.next
        return count

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top + 1 == self.size

    # O(1)
    def push(self, val):
        if not self.is_full():
            node = Node(val)
            node.next = self.head
            self.head = node
            self.top += 1
        else:
            return "is full"

    # O(1)
    def peek(self):
        if not self.is_empty():
            return self.head.val

    # O(1)
    def pop(self):
        if not self.is_empty():
            self.head = self.head.next

    def showstack(self):
        cur = self.head
        res = []
        while cur.next:
            res.append(cur.val)
            cur = cur.next
        return res


link = LinkedStack(3)
print(link.is_empty())  # True
link.push(1)
link.push(2)
link.push(3)
print(link.is_full())  # True
print(link.push(4))  # is full
print(link.showstack())  # [3, 2, 1]
print(link.peek())  # 3
print(link.showstack())  # [3, 2, 1]
link.pop()
print(link.showstack())  # [2, 1]
