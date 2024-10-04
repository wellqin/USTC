# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#  
# 
#  示例 2: 
# 
#  输入: 1->1->1->2->3
# 输出: 2->3 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     cur = pre = dummy = head
    #     while cur:
    #         while cur.next and cur.val == cur.next.val:
    #             cur.next = cur.next.next
    #
    #         pre = cur
    #         cur = cur.next
    #     return dummy
    # 时间复杂度: O(N)- 空间复杂度: O(1) 递归
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        nxt, is_head_dup = head.next, False
        while nxt and nxt.val == head.val:
            nxt, is_head_dup = nxt.next, True
        head.next = self.deleteDuplicates(nxt)
        return head.next if is_head_dup else head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(-1)
        dummy.next = head
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.next.val == cur.val:  # 循环找到重复的节点1 1 ， 3 3 ， 5 5
                val = cur.val
                while cur and cur.val == val:  # 循环找到与当前值不同的节点，去除重复值，1 1，去找 3
                    cur = cur.next
                pre.next = cur
        return dummy.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # 停留在最后一个重复元素位置
                cur = cur.next  # 重复元素位置的下一个不重复了
            else:
                pre = cur
                cur = cur.next
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
head = ListNode(1)  # 测试代码
p1 = ListNode(2)  # 建立链表1->2->3->4->None;
p2 = ListNode(2)
p3 = ListNode(3)
head.next = p1
p1.next = p2
p2.next = p3

print(Solution().deleteDuplicates2(head))
