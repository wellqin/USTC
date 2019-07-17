#给定一个链表，判断链表中是否有环。 
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
#
# 
#
# 示例 1： 
#
# 输入：head = [3,2,0,-4], pos = 1
#输出：true
#解释：链表中有一个环，其尾部连接到第二个节点。
# 
#
# 
#
# 示例 2： 
#
# 输入：head = [1,2], pos = 0
#输出：true
#解释：链表中有一个环，其尾部连接到第一个节点。
# 
#
# 
#
# 示例 3： 
#
# 输入：head = [1], pos = -1
#输出：false
#解释：链表中没有环。
# 
#
# 
#
# 
#
# 进阶： 
#
# 你能用 O(1)（即，常量）内存解决此问题吗？ 
#
"""
想法一： 遍历链表，将遍历过的节点加入list，如果出现重复节点，则返回True，否则遍历结束，返回False，但是结果超时。
如果用个字典记录某个点是否被访问过，时间，空间复杂度都是O（n）


想法二： 创建两个节点，第一个慢节点单步走，第二个快节点两步走，如果没有环，则快节点会首先走到链表尾，退出循环，返回False。
如果存在环，则快节点会再第二圈或者第三圈的地方追上慢节点，直到两者相等，则返回True。
"""


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        超时
        """
        if head is None:
            return False

        list = []
        while head:
            if head in list:
                return True
            else:
                list.append(head)
            head = head.next
        return False

    def hasCycle1(self, head):
        # 字典记录某个点是否被访问过，时间，空间复杂度都是O（n）
        if not head or len(head) == 1:
            return False
        lookup = {}
        while head:
            if head in lookup:
                return True
            else:
                lookup[head] = 1
                head = head.next
        return False

    def hasCycle2(self, head):
        # 快慢指针, beats 96.59%
        if not head or len(head) == 1:
            return False

        cur = prev = head

        while cur and cur.next:  # 慢的
            cur = cur.next
            prev = prev.next.next
            if cur == prev:
                return True

        return False
