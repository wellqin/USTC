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
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def add(self, val):
        # 头插入法
        node = Node(val)
        node.next = self.head
        self.head = node

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, val):
        # 在指定位置添加元素
        if pos <= 0:  # 如果pos位置在0或者以前，那么都当做头插法来做
            self.add(val)
        elif pos > self.length() - 1:  # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(val)
        else:
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(val)
            node.next = cur.next
            cur.next = node

    def remove(self, val):
        # 删除节点
        cur = pre = self.head
        while cur:
            if cur.val == val:
                # 先判断该节点是否是头结点
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, val):
        # 查找节点是否存在
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def tarvel(self):
        cur = self.head
        res = []
        # while cur:  # cur停在None
        #     res.append(cur.val)
        #     cur = cur.next

        while cur.next:  # cur停在最后一个元素
            res.append(cur.val)
            cur = cur.next
        res.append(cur.val)  # 加上最后一个元素
        return res

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count


link = linkList()
for i in range(7):
    link.append(i)
print(link.tarvel())
print(link.length())


