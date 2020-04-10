# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        levelOrder
Description :   
Author :          wellqin
date:             2020/1/31
Change Activity:  2020/1/31
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
        stack = [root]
        res = []
        while stack:
            node = stack.pop(0)
            res.append(node.val)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return res

    def traverseIteration(self, root):  # 层次遍历(不带结构)
        if root == None:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop(0)
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res

    def traverseRecursive(self, root):  # 递归(带结构)
        def helper(node, level):
            if not node:
                return
            else:
                res[level - 1].append(node.val)
                # 之字形
                # if level % 2 == 1:
                #     res[level - 1].append(node.val)
                # else:
                #     res[level - 1].insert(0, node.val)
                if len(res) == level:
                    res.append([])
                # 每层从右到左，只需要调换二个helper即可
                helper(node.left, level + 1)
                helper(node.right, level + 1)
        res = [[]]
        helper(root, 1)
        return res[:-1]

tree = Tree()
for i in range(7):
    tree.add(i)
print('层序遍历:', tree.traverse(tree.root))
print('层序遍历1:', tree.traverseIteration(tree.root))
print('层序遍历2:', tree.traverseRecursive(tree.root))
