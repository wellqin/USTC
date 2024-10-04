# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/9/17
Change Activity:  2019/9/17
-------------------------------------------------
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def nonrecurse(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h


head = ListNode(1)  # 测试代码
p1 = ListNode(2)  # 建立链表1->2->3->4->None;
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3


p = nonrecurse(head)  # 输出链表 4->3->2->1->None
while p:
    print(p.val)
    p = p.next
