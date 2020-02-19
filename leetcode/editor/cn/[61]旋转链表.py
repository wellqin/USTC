# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#  
# 
#  示例 2: 
# 
#  输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL 
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 特判
        if head is None or head.next is None or k <= 0:
            return head

        # 先看链表有多少元素，数这个链表的长度
        cur = head
        counter = 1
        while cur.next:
            cur = cur.next
            counter += 1

        k = k % counter  # 判断是否为整倍数，是的话不用移动 先对k取模，取模后的k范围应该是 1<=k<=链表总长-1
        if k == 0:
            return head

        cur.next = head  # 此时cur在链表尾部，将链表串成环
        cur = head  # cur重新定位为原表头
        # 可以取一些极端的例子找到规律
        # counter - k - 1
        for _ in range(counter - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None  # 处理尾部
        return new_head


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

    print(Solution().rotateRight(l1_1, 2))
