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

# 路径和(三)-二叉树中路径和等于给定值的所有路径（任意两个节点）
class Solution1:
    def __init__(self):
        self.path_num = 0

    def pathSum(self, root, sum):
        """
        递归往下一次深度遍历根节点循环
        :param root:
        :param sum:
        :return:
        """
        if root == None:
            return self.path_num

        self.getPathNum(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)

        return self.path_num

    def getPathNum(self, root, sum):
        """
        依据当前树找目标值，进而找到路径数量
        :param root:
        :param sum:
        :return:
        """
        if root == None:
            return
        if root.val == sum:
            self.path_num += 1
        self.getPathNum(root.left, sum - root.val)
        self.getPathNum(root.right, sum - root.val)


# 二叉树中任意两个节点之间路径和的最大值（二叉树的最大路径和）
class Solution2(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.global_max = root.val if root else 0
        self.findmax(root)
        return self.global_max

    def findmax(self, node):
        if not node:
            return 0

        left = self.findmax(node.left)
        left = left if left > 0 else 0

        right = self.findmax(node.right)
        right = right if right > 0 else 0
        # 这句是精髓，只要判断出当前这个点作为root的path更长，就更新一下
        self.global_max = max(left + right + node.val, self.global_max)
        # 这里是因为sub_path只能为一条边，不然跟上面的root组合起来就不是path了
        return max(left, right) + node.val

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
class Solution3(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        对每一个点都求它自身的Diameter，最后取最大值
        """

        def maxDepth(root):
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        if not root:
            return 0
        return max(maxDepth(root.left) + maxDepth(root.right), self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right))

    def diameterOfBinaryTree1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        """
        刚才中间那些计算maxDepth的状态我们都可以时刻记录下来，即时刻更新res，这样时间可以下降到O(N)
        即我们可以在算maxDepth的时候不是像思路一一样每次都重新算，而是把他们都用L和R存起来
        """
        def maxDepth(node):
            if not node:
                return 0
            L = maxDepth(node.left)
            R = maxDepth(node.right)
            self.res = max(self.res, L + R)
            return max(L, R) + 1

        maxDepth(root)
        return self.res