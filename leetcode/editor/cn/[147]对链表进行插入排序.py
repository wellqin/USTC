# 对链表进行插入排序。 
# 
#  
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。 
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。 
# 
#  
# 
#  插入排序算法： 
# 
#  
#  插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 
#  每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。 
#  重复直到所有输入数据插入完为止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 4->2->1->3
#  输出: 1->2->3->4
#  
# 
#  示例 2： 
# 
#  输入: -1->5->3->4->0
#  输出: -1->0->3->4->5
#  
#  Related Topics 排序 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        相当于分为二部分链表，pre和dummy的已排序区域  +  cur及其之后的未排序区域
            二个指针：dummy记录已排序区域链表头部  pre找到当前cur节点应该插入的位置（即插在pre和pre.next之间）
        插入完成后pre回到dummy链表头部，以便下一次的从头遍历，如果cur最小，则头插
        """
        if not head:
            return head
        dummy = ListNode(None)  # new starter of the sorted list
        cur, pre, nxt = head, dummy, None
        while cur:
            nxt = cur.next
            # find the right place to insert  找到待插入元素
            while pre.next and pre.next.val < cur.val:  # 当前元素小了需要pre从头向后移动到指定位置
                pre = pre.next
            # insert between pre and pre.next  从头插入或中间pre插入
            cur.next = pre.next
            pre.next = cur
            pre = dummy  # dummy记录表头。每次pre移动后回位
            cur = nxt
        return dummy.next

    def insertionSortList1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
                continue
            pre = dummy
            while pre.next.val < head.next.val:
                pre = pre.next
            cur = head.next
            head.next = cur.next
            cur.next = pre.next
            pre.next = cur

        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    l1_1 = ListNode(5)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_4 = ListNode(2)
    l1_5 = ListNode(1)

    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    l1_4.next = l1_5

    print(Solution().insertionSortList(l1_1))
