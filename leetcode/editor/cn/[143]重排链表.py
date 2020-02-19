# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ， 
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→… 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  示例 1: 
# 
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3. 
# 
#  示例 2: 
# 
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3. 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        fast, slow = head, head
        # 找到中点
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 反转后半链表cur
        cur, pre = slow.next, None
        slow.next = None  # 此时head从此处断开，变成一半（left）
        while cur:
            pre, pre.next, cur = cur, pre, cur.next
        # 重排练表
        left = head
        while left and pre:
            left.next, pre.next, left, pre = pre, left.next, left.next, pre.next


# leetcode submit region end(Prohibit modification and deletion)
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

    print(Solution().reorderList(l1_1))
