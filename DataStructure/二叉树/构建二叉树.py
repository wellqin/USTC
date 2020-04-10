# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        构建二叉树
Description :   
Author :          wellqin
date:             2019/8/1
Change Activity:  2019/8/1
-------------------------------------------------
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
一句话，看到树🌲就要想到递归

preorder 是 根 -> 左 -> 右
inorder 是 左 -> 根 -> 右
首先pre的第一个就是整个树的root, 假设 preorder[0] = inorder[k],那么inorder的前k-1个就是树的左子树，后面部分就是树的右子树
"""


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        k = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:k + 1], inorder[0:k])
        root.right = self.buildTree(preorder[k + 1:], inorder[k + 1:])
        return root


"""
inorder 是 左 -> 根 -> 右
postorder是 根 -> 左 ->  右
"""


class Solution1(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        k = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:k], postorder[:k])
        root.right = self.buildTree(inorder[k + 1:], postorder[k:-1])
        return root