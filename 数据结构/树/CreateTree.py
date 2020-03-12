# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        CreateTree
Description :   
Author :          wellqin
date:             2020/3/12
Change Activity:  2020/3/12
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

            if cur_node.left is None:
                cur_node.left = node
                return
            elif cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.left)
                queue.append(cur_node.right)

    def travel(self, root):
        def helper(node, level):
            if not node:
                return
            else:
                res[level - 1].append(node.val)
                # print(res)
                if len(res) == level:
                    res.append([])
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        res = [[]]
        helper(root, 1)

        return res


# t = Tree()
# for i in range(7):
#     t.add(i)
# print(t.travel(t.root))
"""
[[0]]
[[0], [1]]
[[0], [1], [3]]
[[0], [1], [3, 4], []]
[[0], [1, 2], [3, 4], []]
[[0], [1, 2], [3, 4, 5], []]
[[0], [1, 2], [3, 4, 5, 6], []]
[[0], [1, 2], [3, 4, 5, 6], []]
"""
