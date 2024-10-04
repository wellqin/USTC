# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        链表实现队列
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""


class QueueError(ValueError):
    def __init__(self, text='队列为空，不可进行操作！'):
        print(text)
        # pass


# 链表节点
class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


# 链表实现队列,头部删除和查看O(1),尾部加入O(1)
class LQueue(object):
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    # 查看队列中最早进入的元素，不删除
    def peek(self):
        if self.is_empty():
            raise QueueError('队列为空不可进行查看元素操作！')
        return self._head.val

    # 将元素elem加入队列，入队
    def enqueue(self, val):
        '''
        尾插法
        '''
        p = Node(val)
        if self.is_empty():
            self._head = p
            self._rear = p
        else:
            self._rear.next = p
            self._rear = self._rear.next

    # 删除队列中最早进入的元素并将其返回，出队
    def del_queue(self):
        if self.is_empty():
            raise QueueError('队列为空不可进行元素删除操作！')
        cur = self._head.val
        self._head = self._head.next
        return cur


if __name__ == "__main__":
    # pass
    queue = LQueue()
    print(queue.is_empty())
    data_list = [1, 2, 3, 4]
    for data in data_list:
        queue.enqueue(data)
    print(queue.is_empty())
    print(queue.peek())
    print(queue.del_queue())
    print(queue.peek())