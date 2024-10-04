# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        linkList
Description :   
Author :          wellqin
date:             2020/3/16
Change Activity:  2020/3/16
-------------------------------------------------
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class linkList:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        node.next = self.root
        self.root = node

    def travel(self, root):
        cur = root
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def reversed(self, root):
        pre = None
        cur = root
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


li = linkList()
for i in range(5, 0, -1):
    li.add(i)
print(li.travel(li.root))
re = li.reversed(li.root)
print(li.travel(re))
