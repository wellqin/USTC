# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3. buildTree
Description :   
Author :          wellqin
date:             2020/3/19
Change Activity:  2020/3/19
[105] Construct Binary Tree from Preorder and Inorder Traversal：先序和中序遍历可以唯一确定一棵二叉树
[106] Construct Binary Tree from Inorder and Postorder Traversal：中序和后序遍历可以唯一确定一棵二叉树
[606] Construct String from Binary Tree：根据二叉树构建字符串
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
        k = inorder.index(preorder[0])  # inorder中的root位置

        root.left = self.buildTree(preorder[1:k + 1], inorder[0:k])
        root.right = self.buildTree(preorder[k + 1:], inorder[k + 1:])
        return root


    """
    inorder 是 左 -> 根 -> 右
    postorder是 根 -> 左 ->  右
    """

    def buildTree1(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        k = inorder.index(postorder[-1])  # # inorder中的root位置

        root.left = self.buildTree(inorder[:k], postorder[:k])
        root.right = self.buildTree(inorder[k + 1:], postorder[k:-1])
        return root

    def tree2str(self, t: TreeNode) -> str:
        result = ''  # 外部函数中变量声明为global

        def Helper(root):
            nonlocal result  # nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明
            if not root:
                return None
            left = Helper(root.left)
            right = Helper(root.right)

            if left and right:
                result = str(root.val) + '(' + str(left) + ')' + '(' + str(right) + ')'
            elif not left and right:
                result = str(root.val) + '()' + '(' + str(right) + ')'
            elif left and not right:
                result = str(root.val) + '(' + str(left) + ')'
            else:
                result = str(root.val)
            return result

        Helper(t)
        return result

