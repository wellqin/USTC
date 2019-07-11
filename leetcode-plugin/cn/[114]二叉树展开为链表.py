#给定一个二叉树，原地将它展开为链表。 
#
# 例如，给定二叉树 
#
#     1
#   / \
#  2   5
# / \   \
#3   4   6 
#
# 将其展开为： 
#
# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root or (not root.left and not root.right):
            return

        # 先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right  # 把捋直的右子树备份一下

        root.right = root.left  # 把捋直的左子树放到右边
        root.left = None  # 记得把左子树置空
        while (root.right):  # 找到现在右子树的最后一个node
            root = root.right
        root.right = tmp  # 把捋直的原来的右子树接上去

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def preRoot(root, res):
            if not root:
                return
            res.append(root.val)
            preRoot(root.left, res)
            preRoot(root.right, res)

        if not root:
            return
        res = []
        preRoot(root, res)
        if root.left:
            root.left = None
        parent = root
        for i in range(1, len(res)):
            parent.right = TreeNode(res[i])
            parent = parent.right
        return

class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def preorder(root):
            res = []
            if not root:
                return res
            res.append(root)
            if root.left:
                res.extend(preorder(root.left))
            if root.right:
                res.extend(preorder(root.right))
            return res
        if not root:
            return
        node_order = preorder(root)
        for i in range(len(node_order)-1):
            node_order[i].left = None
            node_order[i].right = node_order[i+1]
        node_order[-1].left = None
        node_order[-1].right = None