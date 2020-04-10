# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        基础
Description :   
Author :          wellqin
date:             2019/7/14
Change Activity:  2019/7/14
-------------------------------------------------
"""

"""
栈：
FILO。先进后出。也就是只能从一个方向进出。push()入栈，pop（）出栈。peek。返回栈顶元素而不出栈。栈的入栈和出栈都是O(1)。
 
队列：
FIFO。先进先出。在队列尾部只能插入，而在头部只能删除。插入时候，尾部指针加一，指向后面的空位置。
删除时候，头部指针加一，指向后面存在的数据。
因此可以看出，队列通过移动指针的方式而不是移动移动数据项的方式保证了插入删除的低复杂度。
他们的复杂的都是O（1）。但是这种方式可能会导致。头部尾部指针越来越大造成下面很多空间没有利用。因此引入循环队列的概念
 
循环队列：当你是使用链表去实现队列的化，基本不需要循环队列。因为你的长度可以变化。如果使用的是数组去实现的队列。
那么，要时刻判断队尾是否以及到达数组的边界，
一旦要超出，则将队尾指针复位，也就是-1.。循环队列插入和删除的复杂度也都是O（1）；
 
双端队列：用的较少。也就是两端都可以作为入口或者出口。如果禁用了leftRemove和leftInsert。
则此时双端队列可以看作是普通的栈。因为只能右进右出。
如果禁用了leftRemove 和 rightInsert。此时只能从左进从右出。也就是和普通的队列一样了哈哈哈。
 
优先级队列：如果用数组当底层实现。由于有优先级，插入复杂度O（N），删除的复杂度O（1）。删除永远删除优先级最高的。
普通的队列是一种先进先出的数据结构，元素在队列尾追加，而从队列头删除。在优先队列中，元素被赋予优先级。当访问元素时，
具有最高优先级的元素最先删除。优先队列具有最高级先出 (first in, largest out)的行为特征。通常采用堆数据结构来实现。

"""


# 循环队列
"""
对于队列最好的方法是使用链表实现，因为对于数组来说，队列可能会出现下面这种情况：
不可以继续添加元素，否则会造成数组越界而遭致程序出错。然而此时又不应该扩充数组，因为还有大量实际空间未被占用。
此时我们应该如何解决这个问题呢？我们将其实现为循环队列。
"""
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.cur_size = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cur_size < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre = node
            node.pre.next = node
            self.cur_size += 1
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cur_size > 0:
            node = self.head.next
            self.head.next = node.next
            node.next.pre = self.head
            self.cur_size -= 1
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.head.next.val

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.tail.pre.val

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cur_size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cur_size == self.size