# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例： 
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
#

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(3)
    l1_3 = ListNode(5)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(2)
    l2_2 = ListNode(4)
    l2_3 = ListNode(6)
    l2_1.next = l2_2
    l2_2.next = l2_3

    # print(ss.addTwoNumbers(ll, tt))
    print(Solution().mergeTwoLists(l1_1, l2_1))
