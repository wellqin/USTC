#二叉搜索树中的两个节点被错误地交换。 
#
# 请在不改变其结构的情况下，恢复这棵树。 
#
# 示例 1: 
#
# 输入: [1,3,null,null,2]
#
#   1
#  /
# 3
#  \
#   2
#
#输出: [3,1,null,null,2]
#
#   3
#  /
# 1
#  \
#   2
# 
#
# 示例 2: 
#
# 输入: [3,1,4,null,null,2]
#
#  3
# / \
#1   4
#   /
#  2
#
#输出: [2,1,4,null,null,3]
#
#  2
# / \
#1   4
#   /
#  3 
#
# 进阶: 
#
# 
# 使用 O(n) 空间复杂度的解法很容易实现。 
# 你能想出一个只使用常数空间的解决方案吗？ 
# 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(N)******

先来个inorder然后再来一遍遍历看看哪两个node不符合inorder的顺序，再来一遍遍历swap这两个node就可以
"""
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []
        def midorder(root):
            if not root:
                return
            midorder(root.left)
            self.res.append(root.val)
            midorder(root.right)


        nodes = midorder(root)               # [1,3,null,null,2]
        sortedTrees = sorted(nodes)          # [3,1,null,null,2]

        diff = []
        for index, node in enumerate(nodes):
            if nodes[index] != sortedTrees[index]:
                diff.append(node)            # [1,3]

        def traverseAndSwap(root):
            if not root:
                return
            traverseAndSwap(root.left)
            if root.val == diff[0]:
                root.val = diff[1]
            elif root.val == diff[1]:
                root.val = diff[0]
        traverseAndSwap(root.right)


class Solution0:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.res = []

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)
            return self.res

        nodes = inorder(root)  # get real order of binary tree
        sorted_nodes = sorted(nodes)  # get correct order of inary tree

        diff = []
        for i in range(len(nodes)):  # get those two mistake node
            if nodes[i] != sorted_nodes[i]:
                diff.append(nodes[i])

        def traverseAndSwap(root):  # traverse and swap those two ndoes
            if not root:
                return
            traverseAndSwap(root.left)
            if root.val == diff[0]:
                root.val = diff[1]
            elif root.val == diff[1]:
                root.val = diff[0]
            traverseAndSwap(root.right)

        traverseAndSwap(root)

"""
思路
2 - 时间复杂度: O(N) - 空间复杂度: O(N) ** ** **

迭代

beats
95.10 %
"""

class Solution1:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        first, second, prev = None, None, None
        stack = []
        cur = root
        while stack or cur:
            if cur:  # visit curr's left subtree
                stack.append(cur)
                cur = cur.left
            else:  # done left subtree of curr Node
                cur = stack.pop()
                # compare curr.val with prev.val if we have one
                if prev and cur.val < prev.val:
                    if not first:  # incorrect smaller node is always found as prev node
                        first = prev
                    second = cur  # incorrect larger node is always found as curr node
                # visit curr's right subtree
                prev = cur
                cur = cur.right
        first.val, second.val = second.val, first.val  # recover swapped nodes

"""
思路
3 - 时间复杂度: O(N) - 空间复杂度: O(1) ** ** **

Morris
traversal, 每次都用pred记录下当前访问点cur的左子树中right - most的那个点，将pred与cur连接起来
访问完cur的左子树之后，我们要利用pred回到cur，继而继续访问cur的右子树

这样可以不需要递归的栈调用，也不需要迭代的stack，空间可以省到O(1)

beats
99.32 %
"""

class Solution2:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        first, second, prev = None, None, None
        pred = None  # rightmost node in left tree

        cur = root
        while cur:
            # for each node, we compare it with prev node as we did in in-order-traversal
            if prev and cur.val < prev.val:
                if not first:
                    first = prev
                # we may have corner case that two incorrect nodes are in same pair.
                # so we assign second with a new node at each time
                second = cur
            if cur.left:  # got left tree, then let's locate its rightmost node in left tree
                pred = cur.left
                # we may have visited the left tree before, 
                # and connect the rightmost node with curr node (root node)
                while pred.right and pred.right != cur:
                    pred = pred.right
                if pred.right == cur:  # this condition happens if and only if we have visited left tree before
                    # if this left tree has been visited before, then we are done with it
                    # cut the connection with currNode and start visit curr's right tree
                    pred.right = None
                    prev = cur
                    cur = cur.right
                else:
                    # if this left tree has not been visited before, 
                    # then we create a back edge from rightmost node to curr node, 
                    # so we can return to the start point after done the left tree
                    pred.right = cur
                    cur = cur.left
            else:  # no left tree, then just visit its right tree
                prev = cur
                cur = cur.right
        first.val, second.val = second.val, first.val

























        