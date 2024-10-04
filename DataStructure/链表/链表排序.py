# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        链表排序
Description :   
Author :          wellqin
date:             2020/3/15
Change Activity:  2020/3/15
-------------------------------------------------
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def travel(self, linklist):
        cur = linklist
        while cur.next:
            print(cur.val, end=" ")
            cur = cur.next
        print(cur.val)


class SolutionMerge:
    def sortList(self, head):
        if not (head and head.next):
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:  # 使用快慢指针寻找链表中点，并分解链表
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.mergeTwoLists(*map(self.sortList, (head, slow)))

    def mergeTwoLists(self, left, right):  # 递归融合俩个有序链表
        if left and right:
            if left.val > right.val:
                left, right = right, left
            left.next = self.mergeTwoLists(left.next, right)
        return left or right


class Solution:
    # 归并排序
    def sortList(self, head):
        if not head or not head.next:
            return head
        second = self.findMid(head)
        # left = self.sortList(head)
        # right = self.sortList(second)
        # return self.merge(left, right)

        # 不加*：<map object at 0x000001F938336FD0>
        # 在数组中list()函数可以使得map object变成具体数字
        return self.merge(*map(self.sortList, (head, second)))

    def merge(self, left, right):
        if not left or not right:
            return left or right
        head = dummy = ListNode(-1)
        head.next = left
        while left and right:
            if left.val <= right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        head.next = left or right
        return dummy.next

    def findMid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:  # fast.next不能少
            slow = slow.next  # 不是head.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        return second

    # 快速排序：速度比归并排序快50%左右
    def sortList_quick(self, head):
        # 三路快排
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev

            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]

        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = ListNode(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next

    def sortList_normal(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        self.sort(head, None)
        return head

    def sort(self, left, right):
        if left == right or left.next == right:
            return left
        p = self.partition(left, right)
        self.sort(left, p)
        self.sort(p.next, right)

    def partition(self, left, right):
        # 前后指针法
        value = left.val
        pre = left
        cur = left
        while cur != right:
            if cur.val < value:
                pre = pre.next
                pre.val, cur.val = cur.val, pre.val
            cur = cur.next
        pre.val, left.val = left.val, pre.val
        return pre


obj = SingleLinkList()
for i in reversed([5, 4, 8, 9, 10]):
    obj.add(i)

# obj.travel(obj.head)
#
# link = Solution().sortList(obj.head)
# obj.travel(link)

link1 = Solution().sortList_normal(obj.head)
obj.travel(link1)
