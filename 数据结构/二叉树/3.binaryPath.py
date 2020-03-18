# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.binaryPath
Description :   
Author :          wellqin
date:             2020/3/18
Change Activity:  2020/3/18

func :  三、 二叉树的路径

[112] Path Sum：路径和(一)-是否存在二叉树路径和等于给定值（根节点到叶子节点）-- 返回是否存在

[113] Path Sum II：路径和(二)-二叉树中路径和等于给定值的所有路径（根节点到叶子节点）-- 返回所有路径

[437] Path Sum III：路径和(三)-二叉树中路径和等于给定值的所有路径（任意两个节点）-- 返回所有路径

[257] Binary Tree Paths：二叉树从根节点到叶子节点的所有路径  -- 返回所有路径，不用是路径和为指定值

[124] Binary Tree Maximum Path Sum：二叉树中任意两个节点之间路径和的最大值（二叉树的最大路径和）

[129] Sum Root to Leaf Numbers：所有“根到叶子”路径和的和

[543] Diameter of Binary Tree：二叉树的直径（二叉树任意两个节点之间路径的最大长度）

[687] Longest Univalue Path：最长相同值路径

二叉树的最大距离（即相距最远的两个叶子节点）：https://blog.csdn.net/liuyi1207164339/article/details/50898902
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


tree = Tree()
for i in range(7):
    tree.add(i)
print(tree.travel(tree.root))
node = tree.root


class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False

        def helper(root, level):
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root, 1)

        res = [[]]
