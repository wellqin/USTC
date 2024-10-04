# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 123 + 123 = 246
#


class ListNode(object):
    """节点"""
    def __init__(self, val):
        self.val = val
        self.next = None  # 初始设置下一节点为空


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)  # 取余数
            flag = ((tmpsum + flag) // 10)  # 取整
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        return res

    def addTwoNumbers1(self, l1, l2):
        if not l1 and not l2:
            return
        elif not (l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                res = ListNode(l1.val + l2.val)
                res.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                res = ListNode(l1.val + l2.val - 10)
                res.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
        return res


if __name__ == "__main__":
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    # print(ss.addTwoNumbers(ll, tt))
    print(Solution().addTwoNumbers(l1_1, l2_1))
