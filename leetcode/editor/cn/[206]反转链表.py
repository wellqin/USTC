# 反转一个单链表。
#
# 示例: 
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 思路 1 - 时间复杂度: O(N)- 空间复杂度: O(1)
    # 用三个指针，分别指向prev，cur 和 next，然后loop一圈还算比较简单.
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:  # 终止时，prev在最后元素位置，cur指向空
            next = cur.next  # next一直往前走
            cur.next = prev  # 当前的下一个往回指(反转)
            prev = cur  # prev占据cur位置
            cur = next  # cur指向下一个位置, 不能写成cur = cur.next。此时链表已经反转，当前的下一个节点保存在next
        # while cur:
        #     cur.next, pre, cur = pre, cur, cur.next
        return prev

    # 思路 2 -（递归版本） - 时间复杂度: O(N)- 空间复杂度: O(1)
    def reverseList2(self, head):
        def helper(head, new_head):
            if head:
                nxt = head.next
                head.next = new_head
                return helper(nxt, head)
            else:
                return new_head

        return helper(head, None)  # (cur, pre)

    def func(self, head):
        pre = None
        cur = head
        # while cur:
        #     next = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = next

        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
