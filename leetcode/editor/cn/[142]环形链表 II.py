# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。 
#
# 说明：不允许修改给定的链表。 
#
# 
#
# 示例 1： 
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
#
# 
#
# 示例 2： 
#
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
#
# 
#
# 示例 3： 
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
#
# 
#
# 
#
# 进阶： 
# 你是否可以不用额外空间解决此题？
#


def hasCycle2(head):
    # 快慢指针, beats 96.59%
    if not head or len(head) == 1:
        return False

    cur = prev = head

    while prev and prev.next:  # 慢的
        cur = cur.next
        prev = prev.next.next
        if cur == prev:
            return "tail connects to node index", cur

    return "no cycle"


# "直接快慢指针，跟141一样，。这里注意一下while-else clause的用法就行"
class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:  # 利用头指针去找到位置，不能用下标
            slow = slow.next
            head = head.next
        return head
