#计算给定二叉树的所有左叶子之和。 
#
# 示例： 
#
# 
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
#在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24 
#
# 
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def sumof(root):
            if not root:
                return
            if root.left and not root.left.right and not root.left.left:
                self.res += root.left.val
            sumof(root.left)
            sumof(root.right)

        sumof(root)
        return self.res

        