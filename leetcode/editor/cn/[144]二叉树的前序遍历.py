#给定一个二叉树，返回它的 前序 遍历。 
#
# 示例: 
#
# 输入: [1,null,2,3]  
#   1
#    \
#     2
#    /
#   3 
#
#输出: [1,2,3]
# 
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return res + left + right


class Solution1:
    def preorderTraversal1(self, root):
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res
