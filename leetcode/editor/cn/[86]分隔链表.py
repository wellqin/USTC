# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。 
# 
#  你应当保留两个分区中每个节点的初始相对位置。 
# 
#  示例: 
# 
#  输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#  
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
"""
思路:
用两个链表,一个链表放小于x的节点,一个链表放大于等于x的节点
最后,拼接这两个链表.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        p2.next = None  # 防止构成死循环
        return dummy1.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_4 = ListNode(2)
    l1_5 = ListNode(5)
    l1_6 = ListNode(2)

    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    l1_4.next = l1_5
    l1_5.next = l1_6

    print(Solution().partition(l1_1, 3))
