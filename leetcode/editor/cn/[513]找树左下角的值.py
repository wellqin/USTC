# 给定一个二叉树，在树的最后一行找到最左边的值。
#
# 示例 1: 
#
# 
# 输入:
#
#    2
#   / \
#  1   3
#
# 输出:
# 1
# 
#
# 
#
# 示例 2: 
#
# 
# 输入:
#
#        1
#       / \
#      2   3
#     /   / \
#    4   5   6
#       /
#      7
#
# 输出:
# 7
# 
#
# 
#
# 注意: 您可以假设树（即给定的根节点）不为 NULL。 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return

        def helper(root, level):
            if not root:
                return
            else:
                res[level - 1].append(root.val)
                if len(res) == level:
                    res.append([])
                helper(root.left, level + 1)
                helper(root.right, level + 1)

        res = [[]]
        helper(root, 1)
        res = res[:-1]
        n = len(res)

        return res[n - 1][0]
