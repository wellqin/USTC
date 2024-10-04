#给定一个二叉树，检查它是否是镜像对称的。 
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
#
#     1
#   / \
#  2   2
# / \ / \
#3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
#
#     1
#   / \
#  2   2
#   \   \
#   3    3
# 
#
# 说明: 
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
解题方案
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(1)******

递归

两棵树symmetric， 有几种可能：

均为None ，symmetric
左孩子，右孩子都不存在，并且值相等， symmetric
右子树 和 另一棵树的左子树相等，左子树 和另一颗树的右子树相等 🌲
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, l1, l2):
        if not l1 or not l2:
            if not l1 and not l2:
                return True
            else:
                return False
        if l1.val == l2.val:
            return self.symmetric(l1.left, l2.right) and self.symmetric(l1.right, l2.left)
        else:
            return False


"""
思路 2 - 时间复杂度: O(N)- 空间复杂度: O(1)******

迭代
"""
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lst = []
        lst.append(root)
        lst.append(root)
        while lst:
            t1 = lst.pop() if lst else None
            t2 = lst.pop() if lst else None
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            lst.append(t1.left)
            lst.append(t2.right)
            lst.append(t1.right)
            lst.append(t2.left)
        return True


        