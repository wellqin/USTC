# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        travelTest
Description :   
Author :          wellqin
date:             2020/3/13
Change Activity:  2020/3/13
-------------------------------------------------
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while True:
            cur_node = queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.left)
                queue.append(cur_node.right)

    def travel(self, root):
        def helper(node, level):
            if not node:
                return
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        res = [[]]
        helper(root, 1)

        return res[:-1]


t = Tree()
for i in range(7):
    t.add(i)
print(t.travel(t.root))


def preOrder(root):
    if not root:
        return []
    res = [root.val]
    left = preOrder(root.left)
    right = preOrder(root.right)
    return res + left + right


print(preOrder(t.root))


def preOrderIteration(root):
    if not root:
        return []
    stack, res = [], []
    cur = root
    while stack or cur:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res


print(preOrderIteration(t.root))


def inOrderIteration(root):
    stack, res, cur = [], [], root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


print(inOrderIteration(t.root))


def postOrderIteration(root):
    stack, res, cur = [], [], root
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.left)
            cur = cur.right
        else:
            cur = stack.pop()
    return res[::-1]


print(postOrderIteration(t.root))
