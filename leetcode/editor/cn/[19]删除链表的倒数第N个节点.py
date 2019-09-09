#给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。 
#
# 示例： 
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
#当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
#
# 说明： 
#
# 给定的 n 保证是有效的。 
#
# 进阶： 
#
# 你能尝试使用一趟扫描实现吗？ 
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        count = 0
        while fast.next:
            if count < n:
                count += 1
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(3)
    l1_4 = ListNode(4)
    l1_5 = ListNode(5)

    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    l1_4.next = l1_5

    print(Solution().removeNthFromEnd(l1_1,2))