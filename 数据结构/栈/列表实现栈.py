# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        列表实现栈
Description :   
Author :          wellqin
date:             2019/7/11
Change Activity:  2019/7/11
-------------------------------------------------
"""

"""
stack通常的操作：静态数组
Stack()    建立一个空的栈对象
push()     把一个元素添加到栈的最顶层
pop()      删除栈最顶层的元素，并返回这个元素
peek()     返回最顶层的元素，并不删除它
isEmpty()  判断栈是否为空
size()     返回栈中元素的个数


stack通常的操作：动态数组，插入前面O(n)，插入后面0(1)
Stack() 创建堆栈
push(item) 向栈顶插入项(平时的insert) / append()(内置)        # 入栈之前不需要检查栈是否已满
pop() 返回栈顶的项(内置)，并从堆栈中删除该项(平时的remove)     
clear() 清空堆栈
empty() 判断堆栈是否为空
size() 返回堆栈中项的个数
top() 返回栈顶的项
"""


class Stack:
    def __init__(self, size):
        self.size = size  # 静态数组实现可以判断栈是否满了，动态的话不行
        self.stack = []
        self.top = -1

    def push(self, x):  # 入栈之前检查栈是否已满
        if self.isfull():
            return 'full'
        else:
            self.stack.append(x)
            self.top += 1

    def pop(self):  # 出栈之前检查栈是否为空
        if self.isEmpty():
            return 'Empty'
        else:
            self.stack.pop()
            self.top -= 1

    def isfull(self):
        return self.top + 1 == self.size

    def isEmpty(self):
        return self.top == -1

    def showStack(self):
        return self.stack


s = Stack(10)
for i in range(6):
    s.push(i)
print(s.showStack())

for i in range(3):
    s.pop()
print(s.showStack())

"""
类中有top属性，用来指示栈的存储情况，初始值为-1，一旦插入一个元素，其值加1，利用top的值乐意判定栈是空还是满。
执行时先将0,1,2,3,4,5依次入栈，然后删除栈顶的前三个元素
[0, 1, 2, 3, 4, 5]
[0, 1, 2]
"""


class ArrayStack(object):
    """
    动态数组堆栈（Array Stack）
    堆栈的数组实现插到数组后面，因此基本都是对最后一个元素进行操作
    """

    def __init__(self):
        self._data = []  # 空的容器

    def __len__(self):  # size
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    # push进堆栈： O(1)
    def push(self, e):
        self._data.append(e)

    # 查看栈顶元素：O(1)
    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data[-1]

    # 弹出栈顶元素O(1)
    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.pop()

        # 打印堆栈

    def printstack(self):  # showStack
        for i in range(len(self._data)):
            print(self._data[i], end=' ')
        print()

    def showStack(self):
        return self._data


mystack = ArrayStack()
print('size was: ', str(len(mystack)))
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
print('size was: ', str(len(mystack)))
mystack.printstack()
mystack.pop()
mystack.pop()
print('size was: ', str(len(mystack)))
mystack.printstack()
print(mystack.top())
print('showStack was: ', mystack.showStack())
mystack.pop()
mystack.pop()
mystack.pop()
print('size was: ', str(len(mystack)))

"""
# 输出结果
size
was: 0
size
was: 5
2
3
4
5
size
was: 3
2
3
"""
