# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。 
# 
#  示例 1: 
# 
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#  
# 
#  示例 2: 
# 
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5 
#  Related Topics 排序 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
思路 1 - 时间复杂度: O(NlgN)- 空间复杂度: O(1)******
首先看到sort，肯定要想到八大排序，然后看到题目要求是O(NlgN), 那么范围缩小到 quick sort，merge sort 和 heap sort
但是因为我们是链表，链表之间有pointer，heap sort排除
先用merge sort写

1、利用快慢指针找到链表中点，将其分为两半 
2、递归调用上述过程 
3、合并有序链表
"""

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        second = self.findMid(head)  # 找到链表后半段的head
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):  # O(NlgN)
        if not l or not r:
            return l or r
        dummy = head = ListNode(None)
        head.next = l
        while l and r:
            if l.val < r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
        head.next = l or r  # l and r at least one is None
        return dummy.next

    def findMid(self, head):  # 1 2 3 4
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next  # second = 3 4 none
        slow.next = None    # slow = 1 2 none
        return second

    """
    思路 2 - 时间复杂度: O(NlgN)- 空间复杂度: O(1)******
    再用quick sort写一遍, beats 51.92%
    """

    def sortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l, m, r = ListNode(None), ListNode(None), ListNode(None)
        ll, mm, rr = l, m, r

        pivot = head.val
        while head:
            if head.val < pivot:
                ll.next = head
                ll = ll.next
            elif head.val == pivot:
                mm.next = head
                mm = mm.next
            else:
                rr.next = head
                rr = rr.next
            head = head.next

        ll.next, rr.next = None, None
        l.next = self.sortList(l.next)
        r.next = self.sortList(r.next)
        ll = l
        while ll.next:
            ll = ll.next
        ll.next = m.next
        mm.next = r.next
        return l.next
# leetcode submit region end(Prohibit modification and deletion)
