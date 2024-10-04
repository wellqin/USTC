# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。 
# 
#  每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。 
# 
#  这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。 
# 
#  返回一个符合上述规则的链表的列表。 
# 
#  举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ] 
# 
#  示例 1： 
# 
#  
# 输入: 
# root = [1, 2, 3], k = 5
# 输出: [[1],[2],[3],[],[]]
# 解释:
# 输入输出各部分都应该是链表，而不是数组。
# 例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.ne
# xt.next.next = null。
# 第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
# 最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
#  
# 
#  示例 2： 
# 
#  
# 输入: 
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释:
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
#  
# 
#  
# 
#  提示: 
# 
#  
#  root 的长度范围： [0, 1000].
#  输入的每个节点的大小范围：[0, 999]. 
#  k 的取值范围： [1, 50]. 
#  
# 
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # 求链表长度
        length, node = 0, root
        while node:
            node = node.next
            length += 1

        # 初始化结果
        result = [[] for _ in range(k)]

        dom = length % k  # 前dom个需要多存一个node
        length = length // k  # 每个k中存放多少node

        for i in range(k):
            if root != None:
                result[i] = root
                j = length + (1 if dom > 0 else 0)
                dom -= 1
                pre = None
                for _ in range(j, 0, -1):
                    pre = root
                    root = root.next
                pre.next = None
        return result

    def splitListToParts1(self, root, k):
        cur = root
        length = 0
        res = []
        while cur:
            length += 1
            cur = cur.next
        avg = length // k
        ext = length % k
        for i in range(k):
            res.append(root)
            if root:  # 要判断下
                # print(1 + (1 > 2))为 1 + False = 1
                for j in range(1, avg + (i < ext)):
                    root = root.next
                nxt = root.next
                root.next = None
                root = nxt
        return res


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

    print(Solution().splitListToParts1(l1_1, 2))
