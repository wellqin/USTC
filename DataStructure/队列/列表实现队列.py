# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        列表实现队列
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""


# 先进先出
class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = []

    def enqueue(self, ele):  # 入队操作
        if self.isfull():
            print("queue is full")
        else:
            self.queue.append(ele)
            self.rear = self.rear + 1

    def dequeue(self):  # 出队操作
        if self.isempty():
            print("queue is empty")
        else:
            self.queue.pop(0)
            self.front = self.front + 1

    def isfull(self):
        return self.rear - self.front + 1 == self.size

    def isempty(self):
        return self.front == self.rear

    def showQueue(self):
        print(self.queue)


q = Queue(10)
for i in range(6):
    q.enqueue(i)
q.showQueue()
for i in range(3):
    q.dequeue()
q.showQueue()
print(q.isempty())
