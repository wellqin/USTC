# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
# 它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。 
# 
#  
# 
#  示例： 
# 
#  给定一个链表: 1->2->3->4->5, 和 k = 2.
# 
# 返回链表 4->5. 
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd0(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        count = 0
        cur = head
        while cur:  # 最后停留在None，若写成cur.next，则停在最后一个元素
            count += 1
            cur = cur.next

        k = count - k + 1
        if count == 1 or k - 2 < 0:
            return head

        cur = head
        for i in range(k-2):
            cur = cur.next
        head = cur.next

        return head


    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = fast = slow = ListNode(-1)
        dummy.next = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        return slow.next




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

    print(Solution().getKthFromEnd(l1_1, 2))
