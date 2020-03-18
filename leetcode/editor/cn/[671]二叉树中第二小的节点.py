# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。
#
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。 
#
# 示例 1: 
#
# 
# 输入:
#    2
#   / \
#  2   5
#     / \
#    5   7
#
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 
#
# 示例 2: 
#
# 
# 输入:
#    2
#   / \
#  2   2
#
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inOrder(self, root: TreeNode):
        res = []
        if root != None:
            res = res + self.inOrder(root.left)
            res.append(root.val)
            res = res + self.inOrder(root.right)
        return res

    def findSecondMinimumValue(self, root: TreeNode):
        listNode = set(self.inOrder(root))
        sortedNode = sorted(listNode)
        if (len(listNode) == 1):
            return -1
        else:
            return sortedNode[1]


class Solution1:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        def helper(self, root, value):
            if not root:
                return -1
            if root.val > value:
                return root.val
            l = helper(root.left, value)
            r = helper(root.right, value)
            if l == -1:
                return r
            if r == -1:
                return l
            return min(r, l)

        return helper(root, root.val)
