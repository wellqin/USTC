#您需要在二叉树的每一行中找到最大的值。 
#
# 示例： 
#
# 
#输入: 
#
#          1
#         / \
#        3   2
#       / \   \  
#      5   3   9 
#
#输出: [1, 3, 9]
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root, level):
            if not root:
                return []
            else:
                res[level - 1].append(root.val)
                if len(res) == level:
                    res.append([])
                helper(root.left, level + 1)
                helper(root.right, level + 1)

        res = [[]]
        helper(root, 1)

        return [max(i) for i in res[:-1]]


        