#给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。 
#
# 示例 : 
#给定二叉树 
#
# 
#          1
#         / \
#        2   3
#       / \     
#      4   5    
# 
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。 
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树的 每个节点的左右子树的高度和 的最大值
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res[0] = max(res[0], left + right)
            return max(left, right) + 1


        helper(root)

        return res[0]

        