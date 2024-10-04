# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        二叉树转换
Description :   
Author :          wellqin
date:             2019/8/1
Change Activity:  2019/8/1
-------------------------------------------------
"""


# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#      0
#     / \
#   -3   9
#   /   /
# -10  5
#
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBST(nums[:len(nums) / 2])
        root.right = self.sortedArrayToBST(nums[len(nums) / 2 + 1:])
        return root


# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#      0
#     / \
#   -3   9
#   /   /
# -10  5
#
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sortedArrayToBST(nums):
            if not nums:
                return None
            if nums:
                mid = len(nums) / 2
                root = TreeNode(nums[mid])
                root.left = sortedArrayToBST(nums[:mid])
                root.right = sortedArrayToBST(nums[mid+1:])
                return root
        if not head:
            return None
        else:
            lst = []
            while head:
                lst.append(head.val)
                head = head.next
            return sortedArrayToBST(lst)

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
class Solution2(object):
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