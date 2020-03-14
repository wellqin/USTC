# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 
# 
#  示例 1: 
# 
#  输入: 1->1->2
# 输出: 1->2
#  
# 
#  示例 2: 
# 
#  输入: 1->1->2->3->3
# 输出: 1->2->3 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:  # 需要else
                head = head.next
        return cur

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        while head:
            while head.next and head.next.val == head.val:  # 这里用while更好
                head.next = head.next.next  # skip duplicated node
            head = head.next  # not duplicate of current node, move to next node
        return dummy

    def deleteDuplicatesself(self, head: ListNode) -> ListNode:
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head.next


# leetcode submit region end(Prohibit modification and deletion)
head = ListNode(1)  # 测试代码
p1 = ListNode(2)  # 建立链表1->2->3->4->None;
p2 = ListNode(2)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3

print(Solution().deleteDuplicatesself(head))
