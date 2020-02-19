# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例: 
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop
        node_pools = []
        lookup = collections.defaultdict(list)
        for head in lists:
            if head:
                heappush(node_pools, head.val)
                lookup[head.val].append(head)
        dummy = cur = ListNode(None)
        while node_pools:
            smallest_val = heappop(node_pools)
            smallest_node = lookup[smallest_val].pop(0)
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heappush(node_pools, smallest_node.next.val)
                lookup[smallest_node.next.val].append(smallest_node.next)
        return dummy.next
