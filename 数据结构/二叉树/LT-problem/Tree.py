# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        Tree
Description :   
Author :          wellqin
date:             2020/3/18
Change Activity:  2020/3/18
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
            """
            # 加上奇偶判断可以实现锯齿遍历
            # [[0], [2, 1], [3, 4, 5, 6]] 
            # if level % 2 == 1:
            #     res[level - 1].append(node.val)
            # else:
            #     res[level - 1].insert(0, node.val)
            """
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            helper(node.left, level + 1)
            helper(node.right, level + 1)  # [[0], [1, 2], [3, 4, 5, 6]]

            """
            # left与right互换则是从右到左遍历
            # helper(node.right, level + 1)
            # helper(node.left, level + 1)  # [[0], [2, 1], [6, 5, 4, 3]]
            """

        res = [[]]
        helper(root, 1)
        return res[:-1]
