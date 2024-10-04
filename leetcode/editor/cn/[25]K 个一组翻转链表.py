# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。 
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
#
# 示例 : 
#
# 给定这个链表：1->2->3->4->5 
#
# 当 k = 2 时，应当返回: 2->1->4->3->5 
#
# 当 k = 3 时，应当返回: 3->2->1->4->5 
#
# 说明 : 
#
# 
# 你的算法只能使用常数的额外空间。 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(1)******

可以递归操作, 有两种情况：

    就是压根没有k个node，那么我们直接保持这个k-group不动返回head
    如果有k个node的话，那么我们先找到第k个node之后的递归结果 node = nxt，然后反转前面k个node，让反转结果的结尾 tail.next = nxt

beats 92.70%
"""


class Solution:
    def reverseKGroup(self, head, k):
        cur = head
        cnt = 0
        while cur and cnt != k:  # 往后最多走k步
            cur = cur.next
            cnt += 1
        if cnt == k:  # 如果当前 k-group 有 k 个node的话
            # 先找到第k个node之后的递归结果 node = nxt
            # 让反转结果的结尾 tail.next = nxt
            nxt = self.reverseKGroup(cur, k)
            while cnt > 0:  # 反转前面k个node
                tmp = head.next
                head.next = nxt  # nxt相当于pre
                nxt = head
                head = tmp
                cnt -= 1
            return nxt  # 在有K个node时：递归返回结果(4-->3)
        # 当前 k-group 压根没有k个node，那么我们直接保持这个k-group不动返回head
        return head

    def reverseKGroupIter(self, head, k):

        dummy = ListNode(-1)
        dummy.next = head
        cur = pre = dummy

        n = 0
        while cur.next:
            n += 1
            cur = cur.next

        while n >= k:
            cur = pre.next
            for _ in range(k - 1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt

            pre = cur
            n -= k

        return dummy.next


if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(3)
    l1_4 = ListNode(4)

    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    print(Solution().reverseKGroupIter(l1_1, 2))
