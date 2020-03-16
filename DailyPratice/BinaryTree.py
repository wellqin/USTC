# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        BinaryTree
Description :   
Author :          wellqin
date:             2020/3/16
Change Activity:  2020/3/16
func :  创建树
        前中后序遍历（递归+迭代） + 层次遍历

-------------------------------------------------
"""


class Node:
    def __init__(self, val=None):
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
        while queue:
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
                return []
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        res = [[]]
        helper(root, 1)

        return res[:-1]


tree = Tree()
for i in range(7):
    tree.add(i)
print(tree.travel(tree.root))
node = tree.root


def preOrder(root):
    if not root:
        return []
    res = [root.val]
    left = preOrder(root.left)
    right = preOrder(root.right)
    return res + left + right


def preOrderIter(root):
    if not root:
        return []
    res, stack, cur = [], [], root
    while stack or cur:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res


print(preOrder(node))
print(preOrderIter(node))


def inOrder(root):
    if not root:
        return []
    res, stack, cur = [], [], root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


print(inOrder(node))


def postOrder(root):
    if not root:
        return []
    res, stack, cur = [], [], root
    while stack or cur:
        if cur:
            res.append(cur.val)
            stack.append(cur.left)
            cur = cur.right
        else:
            cur = stack.pop()
    return res[::-1]


def postOrderTraverse(root):
    res, stack, cur = [], [], [root]
    while len(cur) > 0:
        node = cur.pop()
        stack.append(node)
        if node.left:
            cur.append(node.left)
        if node.right:
            cur.append(node.right)

    while len(stack) > 0:
        res.append(stack.pop().val)
    return res


print(postOrder(node))
print(postOrderTraverse(node))

