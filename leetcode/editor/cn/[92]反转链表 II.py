# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。 
# 
#  说明: 
# 1 ≤ m ≤ n ≤ 链表长度。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     pre , cur = None, head
    #     count = 1
    #     while cur:
    #         count += 1
    #         pre = cur
    #         cur = cur.next
    #         while m<= count <= n:
    #             cur.next, pre, cur = pre, cur, cur.next
    #     while cur:
    #         cur.next, pre, cur = pre, cur, cur.next
    #     return pre

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n:  # 特殊判断
            return head
        pre = dummy = ListNode(None)
        dummy.next = head

        for i in range(m - 1):  # 此时p位于m - 1位置
            pre = pre.next
        cur = pre.next  # tail位于m位置

        for i in range(n - m):  # 插入式逆序反转（12345）--234倒转--（13245）-- （14325）
            next = pre.next  # 优势：不需要在理会头尾节点的连续性，即重新串起来链表
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = next

            # pre.next, cur.next, pre.next.next = cur.next, cur.next.next, pre.next
        return dummy.next

    def reverseBetween2(self, head, m, n):  # 官方题解
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        # 重新串起来链表
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

# leetcode submit region end(Prohibit modification and deletion)
