# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
#
# 
#
# 示例: 
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
#

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 和链表反转类似，关键在于有三个指针，分别指向前后和当前节点。不同点是两两交换后，移动节点步长为２
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # 创建一个不含任何信息的头结点，并添加到原链表的前面
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy  # 指向已完成交换部分的尾结点，初始为头结点dummy
        cur, nxt = head, head.next  # 分别指向要交换的两个结点
        while nxt:  # 后二个都存在
            # 重新调整结点位置
            cur.next = nxt.next
            nxt.next = cur
            pre.next = nxt
            # 更新指针
            pre = cur
            cur = cur.next
            nxt = cur.next if cur else None  # 如果奇数，则最后一个不交换，此处防止出错
        return dummy.next

    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            head, head.next, head.next.next = head.next, head, self.swapPairs(head.next.next)
            return head

    def swapPairs2(self, head):
        # 1. 终止条件：当前节点为null，或者下一个节点为null
        if not (head and head.next):
            return head

        # 2. 函数内：将2指向1，1指向下一层的递归函数，最后返回节点2
        # 假设链表是 1->2->3->4
        # 就先保存节点2
        tmp = head.next
        # 继续递归，处理节点3->4
        # 当递归结束返回后，就变成了4->3
        # 于是head节点就指向了4，变成1->4->3
        head.next = self.swapPairs2(tmp.next)
        # 将2节点指向1
        tmp.next = head

        # 3. 返回给上一层递归的值应该是已经交换完成后的子链表
        return tmp

    def swapPairs3(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:  # 后二个都存在
            cur, nxt = pre.next, pre.next.next  # 标记这二个

            # 三步走
            pre.next = nxt
            cur.next = nxt.next
            nxt.next = cur

            # 更新指针位置，前进二个
            pre = pre.next.next
        return dummy.next


if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(3)
    l1_4 = ListNode(4)

    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = l1_4
    # print(ss.addTwoNumbers(ll, tt))
    print(Solution().swapPairs2(l1_1))
