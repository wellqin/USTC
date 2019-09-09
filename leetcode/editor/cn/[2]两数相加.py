# #给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# #
# # 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# #
# # 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# #
# # 示例：
# #
# # 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# #输出：7 -> 0 -> 8
# #原因：342 + 465 = 807
# #
#
class ListNode(object):
    """节点"""

    def __init__(self, val):
        self.val = val
        self.next = None  # 初始设置下一节点为空

'''
上面定义了一个节点的类，当然也可以直接使用python的一些结构。比如通过元组（elem, None）
'''


# 下面创建单链表，并实现其应有的功能


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个列表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("\n")

    def add(self, val):
        '''链表头部添加元素'''
        node = Node(val)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
                # 如果pos位置在0或者以前，那么都当做头插法来做
            self.add(item)
        elif pos > self.length() - 1:
            # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断该节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while not cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1



        val1, val2 = [l1.val], [l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        num1 = ''.join([str(i) for i in val1[::-1]])
        num2 = ''.join([str(i) for i in val2[::-1]])

        tmp = str(int(num1) + int(num2))[::-1]
        res = ListNode(int(tmp[0]))
        run_res = res
        for i in range(1, len(tmp)):
            run_res.next = ListNode(int(tmp[i]))
            run_res = run_res.next
        return res

    def addTwoNumbersDG(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        elif not (l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
        return l3


    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ans = ListNode(0)  # 新建一个节点，初始值为0
        temp = ans
        tempsum = 0

        while True:
            if (l1 != None):
                tempsum = l1.val + tempsum  # l1链表节点值添加到总和里
                l1 = l1.next  # 指针指向下一个节点
            if (l2 != None):
                tempsum = tempsum + l2.val  # l2链表节点值添加到总和里
                l2 = l2.next  # 指针指向下一个节点

            temp.val = tempsum % 10  # 取余数（满十进位），赋值当前节点值
            print(tempsum)
            tempsum = int(tempsum / 10)  # 获取进位数赋值给总和（比如tempsum为10则进1位，否则进位为0），下一次节点相加，从新的总和开始。
            if l1 == None and l2 == None and tempsum == 0:  # 直到没有进位了，同时节点位空了，跳出循环。（这里加上tempsum==0条件是因为，最后两个节
                break  # 点和值可能大于10）

            temp.next = ListNode(0)  # 新建下一个节点，存放和
            temp = temp.next  # 指针指向下一个节点

        return ans


    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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
            tmpres = ((tmpsum + flag) % 10)
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        return res





if __name__ == "__main__":

    l1_1 = ListNode(3)
    l1_2 = ListNode(4)
    l1_3 = ListNode(2)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(4)
    l2_2 = ListNode(6)
    l2_3 = ListNode(5)
    l2_1.next = l2_2
    l2_2.next = l2_3


    # print(ss.addTwoNumbers(ll, tt))
    print(SingleLinkList().addTwoNumbers2(l1_1, l2_1))





# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     # @return a ListNode
#     def addTwoNumbers(self, l1, l2):
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         else:
#             carry = 0
#             ret = ListNode(0)
#             ret_Last = ret
#             while (l1 or l2):
#                 sum = 0
#                 if l1:
#                     sum += l1.val
#                     l1 = l1.next
#                 if l2:
#                     sum += l2.val
#                     l2 = l2.next
#                 sum += carry
#                 ret_Last.next = ListNode(sum % 10)
#                 ret_Last = ret_Last.next
#                 carry = (sum >= 10)
#             ret = ret.next
#             if carry:
#                 ret_Last.next = ListNode(1)
#             del ret_Last
#             return ret
#
#
# def myPrintList(l):
#     while (True):
#         print(l.val)
#         if l.next is not None:
#             l = l.next
#         else:
#             print()
#             break
#
#
# if __name__ == '__main__':
#     # 342 + 465 = 807
#     l1_1 = ListNode(3)
#     l1_2 = ListNode(4)
#     l1_3 = ListNode(2)
#     l1_1.next = l1_2
#     l1_2.next = l1_3
#
#     l2_1 = ListNode(4)
#     l2_2 = ListNode(6)
#     l2_3 = ListNode(5)
#     l2_1.next = l2_2
#     l2_2.next = l2_3
#
#     l3 = Solution().addTwoNumbers(l1_1, l2_1)
#     myPrintList(l3)
