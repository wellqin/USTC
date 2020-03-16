# coding=utf-8
"""
-------------------------------------------------
File Name:        二个队列实现栈
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""


class Queue(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def enqueue(self, val):
        # 二个队列在入栈时，只入空栈
        if len(self.queue1) == 0:
            self.queue1.append(val)
        elif len(self.queue2) == 0:
            self.queue2.append(val)

        # 都不为空时，将数量大于1的POP加到只有1的栈尾部
        if len(self.queue2) == 1 and len(self.queue1) >= 1:
            while len(self.queue1) > 0:
                self.queue2.append(self.queue1.pop(0))
        elif len(self.queue1) == 1 and len(self.queue2) >= 1:
            while len(self.queue2) > 0:
                self.queue1.append(self.queue2.pop(0))

    def dequeue(self):
        if self.queue1:
            return self.queue1.pop(0)
        elif self.queue2:
            return self.queue2.pop(0)
        else:
            return None


class Stock:
    # 剑指
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def enqueue(self, node):
        self.queueA.append(node)

    def dequeue(self):
        if len(self.queueA) == 0:
            return None
        while len(self.queueA) != 1:
            self.queueB.append(self.queueA.pop(0))
        self.queueA, self.queueB = self.queueB, self.queueA  # 交换是为了下一次的pop
        return self.queueB.pop()


q = Stock()
q.enqueue(3)
# print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

# class StackWithTwoQueues(object):
#     def __init__(self):
#         self._queue1 = []
#         self._queue2 = []
#
#     def push(self, x):
#         if len(self._queue1) == 0:
#             self._queue1.append(x)
#         elif len(self._queue2) == 0:
#             self._queue2.append(x)
#         if len(self._queue2) == 1 and len(self._queue1) >= 1:
#             while self._queue1:
#                 self._queue2.append(self._queue1.pop(0))
#         elif len(self._queue1) == 1 and len(self._queue2) > 1:
#             while self._queue2:
#                 self._queue1.append(self._queue2.pop(0))
#
#     def pop(self):
#         if self._queue1:
#             return self._queue1.pop(0)
#         elif self._queue2:
#             return self._queue2.pop(0)
#         else:
#             return None
#
#     def getStack(self):
#         print("queue1", self._queue1)
#         print("queue2", self._queue2)
#
#
# sta = StackWithTwoQueues()
# sta.push(1)
# sta.getStack()
# sta.push(2)
# sta.getStack()
# sta.push(3)
# sta.getStack()
# sta.push(4)
# sta.getStack()
# print(sta.pop())
# sta.getStack()
# print(sta.pop())
# sta.getStack()
# print(sta.pop())
# sta.getStack()
