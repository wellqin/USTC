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
        self.stack1=[]
        self.stack2=[]

    def enqueue(self, item):
        if len(self.stack1) == 0:
            self.stack1.append(item)
        elif len(self.stack2) == 0:
            self.stack2.append(item)
        if len(self.stack2)==1 and len(self.stack1) >= 1:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop(0))
        elif len(self.stack1)==1 and len(self.stack2) >= 1:
            while len(self.stack2)>0:
                self.stack1.append(self.stack2.pop(0))

    def dequeue(self):
        if self.stack1:
            return self.stack1.pop(0)
        elif self.stack2:
            return self.stack2.pop(0)
        else:
            return None

q = Queue()
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