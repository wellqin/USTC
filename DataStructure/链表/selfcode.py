# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        selfcode
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


class LinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def add(self, val):
        node = Node(val)
        node.next = self.__head
        self.__head = node

    def append(self, val):
        node = Node(val)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def insert(self, pos, val):
        if pos < 0:
            self.add(val)
        elif pos > self.length() - 1:
            self.append(val)
        else:
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node = Node(val)
            node.next = cur.next
            cur.next = node

    def remove(self, val):
        pre = None
        cur = self.__head
        while cur:
            if cur.val == val:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def exists(self, val):
        cur = self.__head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False






    def travel(self):
        cur = self.__head
        li = []
        while cur is not None:
            # print(cur.val, end='')
            li.append(cur.val)
            cur = cur.next
        return li


if __name__ == "__main__":
    obj = LinkList()
    for i in range(6):
        obj.append(i)
    obj.insert(1, 999)
    print(obj.travel())
