# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        二个栈实现队列
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""


class Solution:
    # 初始化两个栈
    def __init__(self):
        self.stackA = []
        self.stackB = []

    # 这里只要求实现队列的push和pop操作，分别使用两个栈表示弹出和压入
    def push(self, val):
        # write code here
        self.stackA.append(val)

    # 弹出需要有一个先验条件：若队列为空，则返回None
    def pop(self):
        # 若压入的栈中有元素则直接弹出
        if self.stackB:
            self.stackB.pop()
        # 若A中没有元素则返回None
        elif not self.stackA:
            return None
        # 若A中有元素，则统一压入B中进行弹出
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
