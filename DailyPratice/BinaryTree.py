# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        BinaryTree
Description :   
Author :          wellqin
date:             2020/3/16
Change Activity:  2020/3/16
func :  (1) 基础篇
        创建树
        前中后序遍历（递归+迭代） + 层次遍历（递归+迭代）
        层次遍历拓展：反向遍历  +  之字形遍历（锯齿遍历）
        二叉树所有路径（root --> nil）

-------------------------------------------------
"""


# class Node:
#     def __init__(self, val=None):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, val):
#         node = Node(val)
#         if not self.root:
#             self.root = node
#             return
#         queue = [self.root]
#         while queue:
#             cur_node = queue.pop(0)
#             if not cur_node.left:
#                 cur_node.left = node
#                 return
#             elif not cur_node.right:
#                 cur_node.right = node
#                 return
#             else:
#                 queue.append(cur_node.left)
#                 queue.append(cur_node.right)
#
#     def travel(self, root):
#
#         def helper(node, level):
#             if not node:
#                 return []
#             """
#             # 加上奇偶判断可以实现锯齿遍历
#             # [[0], [2, 1], [3, 4, 5, 6]]
#             # if level % 2 == 1:
#             #     res[level - 1].append(node.val)
#             # else:
#             #     res[level - 1].insert(0, node.val)
#             """
#             res[level - 1].append(node.val)
#             if len(res) == level:
#                 res.append([])
#             helper(node.left, level + 1)
#             helper(node.right, level + 1)   # [[0], [1, 2], [3, 4, 5, 6]]
#
#             """
#             # left与right互换则是从右到左遍历
#             # helper(node.right, level + 1)
#             # helper(node.left, level + 1)  # [[0], [2, 1], [6, 5, 4, 3]]
#             """
#
#         res = [[]]
#         helper(root, 1)
#         return res[:-1]
#
#     def travelIter(self, root):
#         res = []
#         stack = [root]
#         while stack:
#             cur = stack.pop(0)
#             res.append(cur.val)
#             if cur.left:
#                 stack.append(cur.left)
#             if cur.right:
#                 stack.append(cur.right)
#         return res
#
#     def allPath(self, root):
#         if not root.left and not root.right:
#             return [str(root.val)]
#         left, right = [], []
#         if root.left:
#             left = [str(root.val) + i for i in self.allPath(root.left)]
#         if root.right:
#             right = [str(root.val) + i for i in self.allPath(root.right)]
#         return left + right
#
#
#
# tree = Tree()
# for i in range(7):
#     tree.add(i)
# print(tree.travel(tree.root))
# print(tree.travelIter(tree.root))
# print(tree.allPath(tree.root))
# node = tree.root
#
#
# def preOrder(root):
#     if not root:
#         return []
#     res = [root.val]
#     left = preOrder(root.left)
#     right = preOrder(root.right)
#     return res + left + right
#
#
# def preOrderIter(root):
#     if not root:
#         return []
#     res, stack, cur = [], [], root
#     while stack or cur:
#         if cur:
#             res.append(cur.val)
#             stack.append(cur.right)
#             cur = cur.left
#         else:
#             cur = stack.pop()
#     return res
#
#
# print(preOrder(node))
# print(preOrderIter(node))
#
#
# def inOrder(root):
#     if not root:
#         return []
#     res, stack, cur = [], [], root
#     while stack or cur:
#         if cur:
#             stack.append(cur)
#             cur = cur.left
#         else:
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right
#     return res
#
#
# print(inOrder(node))
#
#
# def postOrder(root):
#     if not root:
#         return []
#     res, stack, cur = [], [], root
#     while stack or cur:
#         if cur:
#             res.append(cur.val)
#             stack.append(cur.left)
#             cur = cur.right
#         else:
#             cur = stack.pop()
#     return res[::-1]
#
#
# def postOrderTraverse(root):
#     res, stack, cur = [], [], [root]
#     while cur:
#         node = cur.pop()
#         stack.append(node)
#         if node.left:
#             cur.append(node.left)
#         if node.right:
#             cur.append(node.right)
#
#     while len(stack) > 0:
#         res.append(stack.pop().val)
#     return res
#
#
# print(postOrder(node))
# print(postOrderTraverse(node))


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
        def helper(root, level):
            if not root:
                return []
            res[level - 1].append(root.val)
            if len(res) == level:
                res.append([])
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        res = [[]]
        helper(root, 1)
        return res[:-1]

    def travelIter(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur_node = stack.pop(0)
            res.append(cur_node.val)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return res

    def preOrder(self, root):
        if not root:
            return []
        res = [root.val]
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)

        return res + left + right

    def preorderTraversal(self, root):
        if not root:
            return []
        stack, res = [root, ], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def preOrderIter(self, root):
        # 迭代的优化版本
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

    def inOrderIter(self, root):
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

    def postOrderIter(self, root):
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
        return res[::-1]


t = Tree()
for i in range(7):
    t.add(i)
print(t.travel(t.root))
print(t.travelIter(t.root))
print(t.preOrder(t.root))
print(t.preOrderIter(t.root))
print(t.inOrderIter(t.root))
print(t.postOrderIter(t.root))
print(t.preorderTraversal(t.root))
