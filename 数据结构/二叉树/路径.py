# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        路径
Description :   
Author :          wellqin
date:             2019/7/31
Change Activity:  2019/7/31
-------------------------------------------------
"""

#给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#给定如下二叉树，以及目标和 sum = 22，
#
#               5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1
#
#
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left or root.right:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        else:
            return root.val == sum

    def hasPathSum1(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        if not root:
            return []

        def dfs(root, cur_list):
            if root.left:
                dfs(root.left, cur_list + [root.left.val])
            if root.right:
                dfs(root.right, cur_list + [root.right.val])
            if not root.right and not root.left:
                if sum(cur_list) == Sum:
                    res.append(cur_list)

        dfs(root, [root.val])
        if res:
            return True
        return False

# 返回:
#
# [
#   [5,4,11,2],
#   [5,8,4,5]
#]
#

    def pathSum_dfs(self, root, Sum):
        res = []
        if not root:
            return []

        def dfs(root, cur_list):
            if root.left:
                dfs(root.left, cur_list + [root.left.item])
            if root.right:
                dfs(root.right, cur_list + [root.right.item])
            if not root.right and not root.left:
                if sum(cur_list) == Sum:
                    res.append(cur_list)

        dfs(root, [root.item])
        return res


    """
    #给定一个二叉树，返回所有从根节点到叶子节点的路径。 
    #
    # 说明: 叶子节点是指没有子节点的节点。 
    #
    # 示例: 
    #
    # 输入:
    #
    #   1
    # /   \
    #2     3
    # \
    #  5
    #
    #输出: ["1->2->5", "1->3"]
    #
    #解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3 
    """
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def helper(node, cur_path):
            if not node.left and not node.right:    ## 到leaf了
                res.append(cur_path + [node.val])
                return
            if node.left:
                helper(node.left, cur_path + [node.val])
            if node.right:
                helper(node.right, cur_path + [node.val])

        res = []
        if not root:
            return res
        helper(root, [])

        return ['->'.join([str(val) for val in path]) for path in res]
"""
    注意一点，很多人可能看到这里有好几次cur_path + [node.val]，觉得干嘛不直接写在最开头了，事实是这样做的话cur_path就已经变化了，因为要执行完if
    node.left才去执行if
    node.right，此时cur_path就不是原来的cur_path了。
"""