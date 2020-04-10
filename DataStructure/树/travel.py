# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        travel
Description :   
Author :          wellqin
date:             2020/3/12
Change Activity:  2020/3/12
-------------------------------------------------
"""
from DataStructure.树.CreateTree import Tree

t = Tree()
for i in range(7):
    t.add(i)
root = t.root
# print("层次遍历", t.travel(root)[:-1])
"""
     0
  1     2
3  4   5  6
"""


def preOrder(root):
    if not root:
        return []
    res = [root.val]
    left = preOrder(root.left)
    right = preOrder(root.right)
    return res + left + right


print("先序遍历-递归", preOrder(root))


# 先序遍历-迭代1，效率较低，不够灵性
def preOrderLteration1(root):
    if not root:
        return []
    stack = [root]
    res = []

    while stack:
        cur = stack.pop()
        res.append(cur.val)
        # print(res)
        # 顺序添加cur.right和cur.left
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res


# print("先序遍历-迭代1", preOrderLteration1(root))
"""
[0]
[0, 1]
[0, 1, 3]
[0, 1, 3, 4]
[0, 1, 3, 4, 2]
[0, 1, 3, 4, 2, 5]
[0, 1, 3, 4, 2, 5, 6]
"""


def preOrderLteration2(root):
    if not root:
        return []
    res, stack, cur = [], [], root

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res


"""
     0
  1     2
3  4   5  6

stack元素

 2    4   None
5 6
"""
# print("先序遍历-迭代2", preOrderLteration2(root))


def inOrder(root):
    if not root:
        return []
    res = [root.val]
    left = inOrder(root.left)
    right = inOrder(root.right)
    return left + res + right


# print("中序遍历-递归", inOrder(root))


def inOrderIteration(root):
    if not root:
        return []
    res, stack, cur = [], [], root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


# print("中序遍历-迭代", inOrderIteration(root))


def postOrder(root):
    if not root:
        return []
    res = [root.val]
    left = postOrder(root.left)
    right = postOrder(root.right)
    return left + right + res


print("后序遍历-递归", postOrder(root))


def postOrderIteration(root):
    if not root:
        return []
    res, stack, cur = [], [], root

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.left)
            cur = cur.right
        else:
            cur = stack.pop()
    print(res)  # [0, 2, 6, 5, 1, 4, 3]
    return res[::-1]


"""
     0
  1     2
3  4   5  6
"""
print("后序遍历-迭代", postOrderIteration(root))  # [3, 4, 1, 5, 6, 2, 0]



