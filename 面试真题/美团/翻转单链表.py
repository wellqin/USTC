# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        翻转单链表
Description :   
Author :          wellqin
date:             2019/9/17
Change Activity:  2019/9/17
-------------------------------------------------
"""


class linklist:
    def __init__(self, val):
        self.val = val
        self.next = None


class singleList:
    def __init__(self):
        self.head = None

    def add(self, val):
        node = linklist(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def is_empty(self):
        return self.head == None

    def append(self, item):
        node = linklist(item)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def reverse(self, head):
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def travel(self):
        cur = self.head
        while cur:
            print(cur.val, end='')
            cur = cur.next
        print("\n")


lists = singleList()
for i in range(1, 6):
    lists.append(i)
lists.travel()

cur = lists.reverse(lists.head)

while cur:
    print(cur.val, end='')
    cur = cur.next










# class Node(object):
#     def __init__(self, data, next=None):
#         self.val = data
#         self.next = next
#
#
# def fun4(head):
#     if head == None:
#         return None
#     L, M, R = None, None, head
#     while R.next != None:
#         L = M
#         M = R
#         R = R.next
#         M.next = L
#     R.next = M
#     return R
#
#
# # 测试用例
# if __name__ == '__main__':
#     l1 = Node(3)
#     l1.next = Node(2)
#     l1.next.next = Node(1)
#     l1.next.next.next = Node(9)
#     l = fun4(l1)
#
#     print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)







