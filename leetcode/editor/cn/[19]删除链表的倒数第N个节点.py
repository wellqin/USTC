# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例： 
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
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
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        for i in range(n):
            fast = fast.next  # 此时slow与fast正好相隔n个单位，若相隔n+1个单位，则fast停留在最后一个元素的下一个元素，即None
        while fast.next:  # 此时fast停留在最后一个元素，而slow正好到n-1的位置
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # slow.next = fast.next，会出现fast为空，截断链表
        return dummy.next  # # 此处不返回 head 是因为 head 可能被删除.

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        l = 0
        cur = head
        # 计算链表长度
        while cur:
            l += 1
            cur = cur.next
        # 如果长度为1，直接return None
        if l == 1:
            return None
        # 计算删除需要移动的长度
        l = l - n - 1
        # 如果小于0，说明需要删除第一个元素，那么直接return head.next。
        if l < 0:
            return head.next
        pnt = head
        for i in range(l):
            pnt = pnt.next
        pnt.next = pnt.next.next
        return head

    # def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:  # 二次遍历
    #     cur = head
    #     count = 1  # count = 0
    #     while cur.next:  # while node:
    #         cur = cur.next
    #         count += 1
    #     if count == n:
    #         return head.next
    #     cur = head
    #     for i in range(count - n - 1):
    #         cur = cur.next
    #     cur.next = cur.next.next
    #     return head
    #
    # def removeNthFromEndSelf(self, head, n):  # # 二次遍历自己写的，效率极低
    #     if not head:
    #         return None
    #
    #     def length(head):
    #         cur = head
    #         count = 0
    #         while cur:
    #             count += 1
    #             cur = cur.next
    #         return count
    #
    #     lengthnode = length(head)
    #     if lengthnode == n:
    #         return head.next
    #     cur = head
    #     pre = head
    #     count = 0
    #     while count < (lengthnode - n):
    #         pre = cur
    #         cur = cur.next
    #         count += 1
    #     pre.next = cur.next
    #     return head

    def removeNthFromEnd3(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        count = 0
        cur = head
        while cur:  # 最后停留在None，若写成cur.next，则停在最后一个元素
            count += 1
            cur = cur.next

        k = count - k + 1  # 倒数k个，为正数count - k + 1个
        if count == 1 or k - 2 < 0:
            return head.next

        cur = head
        for i in range(k - 2):  # i从0开始计数，所以只能走k-2步
            cur = cur.next
        cur.next = cur.next.next

        return head

    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = fast = slow = ListNode(-1)
        dummy.next = head

        for i in range(k):
            fast = fast.next

        while slow and fast.next:
            slow = slow.next
            fast = fast.next

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

    print(Solution().removeNthFromEnd(l1_1, 2))
