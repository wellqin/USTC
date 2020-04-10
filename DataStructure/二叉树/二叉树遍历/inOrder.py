# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        inOrder
Description :   
Author :          wellqin
date:             2020/1/30
Change Activity:  2020/1/30
-------------------------------------------------
"""

# 构建了层序遍历: [0, 1, 2, 3, 4, 5, 6]的二叉树
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            while True:
                cur_node = queue.pop(0)
                if cur_node.left is None:
                    cur_node.left = node
                    return
                elif cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
    def traverse(self, root):  # 层次遍历
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return res
tree = Tree()
for i in range(7):
    tree.add(i)
print('层序遍历:', tree.traverse(tree.root))

# 递归
def inOrder(root):
    if not root:
        return []
    res = [root.val]
    left = inOrder(root.left)
    right = inOrder(root.right)
    return left + res + right
print("Recursive", inOrder(tree.root))

# 迭代
def inOrderIteration(root):
    if not root:
        return []
    stack = []
    res = []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res
print("Iteration", inOrderIteration(tree.root))

