# 计算给定二叉树的所有左叶子之和。
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
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
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
from functools import reduce


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     def helper(root, level):
    #         if not root:
    #             return []
    #         else:
    #             res[level - 1].append(root.val)
    #             if len(res) == level:
    #                 res.append([])
    #             helper(root.left, level + 1)
    #             helper(root.right, level + 1)
    #
    #     res = [[]]
    #     helper(root, 1)
    #
    #
    #     total = reduce(lambda x, y: x + y, [i[0] for i in res if i])
    #     return total
