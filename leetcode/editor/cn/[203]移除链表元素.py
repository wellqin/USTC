# 删除链表中等于给定值 val 的所有节点。 
# 
#  示例: 
# 
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return None

        pre = head  # pre = None容易出错
        cur = head
        while cur:
            if cur.val == val:
                if cur == head:
                    head = head.next
                # pre.next = cur.next  这么写超时了
                else:
                    cur = cur.next
                    pre.next = cur  # pre = None 时 AttributeError: 'NoneType' object has no attribute 'next'
            else:
                pre = cur
                cur = cur.next
        return head

    # def removeElements1(self, head: ListNode, val: int) -> ListNode:
    #     if not head:
    #         return None
    #
    #     while head and head.val == val:
    #         head = head.next
    #
    #     pre = head
    #     cur = head
    #
    #     while cur:
    #         if cur.val == val:
    #             cur = cur.next
    #             pre.next = cur
    #         else:
    #             pre = cur
    #             cur = cur.next
    #
    #     return head

# leetcode submit region end(Prohibit modification and deletion)
