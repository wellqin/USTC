# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        翻转
Description :   
Author :          wellqin
date:             2019/9/17
Change Activity:  2019/9/17
-------------------------------------------------
"""

# -*- coding: utf-8 -*-
'''
链表逆序
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


'''
第一种方法：
对于一个长度为n的单链表head,用一个大小为n的数组arr储存从单链表从头
到尾遍历的所有元素，在从arr尾到头读取元素简历一个新的单链表
时间消耗O(n),空间消耗O(n)
'''


# 第一种方法：
def reverse_linkedlist1(head):
    if not head or not head.next:  # 边界条件
        return head
    arr = []  # 空间消耗为n,n为单链表的长度
    while head:
        arr.append(head.val)
        head = head.next
    newhead = ListNode(0)
    tmp = newhead
    for i in arr[::-1]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return newhead.next


'''
开始以单链表的第一个元素为循环变量cur,并设置2个辅助变量tmp,保存数据;
newhead,新的翻转链表的表头。
时间消耗O(n),空间消耗O(1)
'''


# 第二种方法：
def reverse_linkedlist2(head):
    if head is None or head.next is None:  # 边界条件
        return head
    cur = head  # 循环变量
    tmp = None  # 保存数据的临时变量
    newhead = None  # 新的翻转单链表的表头
    while cur:
        tmp = cur.next
        cur.next = newhead
        newhead = cur  # 更新 新链表的表头
        cur = tmp
    return newhead


'''
开始以单链表的第二个元素为循环变量，用2个变量循环向后操作,并设置1个辅助变量tmp,保存数据;
时间消耗O(n),空间消耗O(1)
'''


# 第三种方法：
def reverse_linkedlist3(head):
    if head == None or head.next is None:  # 边界条件
        return head
    p1 = head  # 循环变量1
    p2 = head.next  # 循环变量2
    tmp = None  # 保存数据的临时变量
    while p2:
        tmp = p2.next
        p2.next = p1
        p1 = p2
        p2 = tmp
    head.next = None
    return p1


'''
递归操作，先将从第一个点开始翻转转换从下一个节点开始翻转
直至只剩一个节点
时间消耗O(n),空间消耗O(1)
'''


# 第四种方法：
def reverse_linkedlist4(head):
    if head is None or head.next is None:
        return head
    else:
        newhead = reverse_linkedlist4(head.next)
        head.next.next = head
        head.next = None
    return newhead


def create_ll(arr):
    pre = ListNode(0)
    tmp = pre
    for i in arr:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return pre.next


def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.val, end='')
        tmp = tmp.next


a = create_ll(range(5))
print_ll(a)  # 0 1 2 3 4
a = reverse_linkedlist1(a)
print_ll(a)  # 4 3 2 1 0
a = reverse_linkedlist2(a)
print_ll(a)  # 0 1 2 3 4
a = reverse_linkedlist3(a)
print_ll(a)  # 4 3 2 1 0
a = reverse_linkedlist4(a)
print_ll(a)  # 0 1 2 3 4
