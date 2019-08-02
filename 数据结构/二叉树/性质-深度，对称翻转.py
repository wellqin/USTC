# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        性质-深度，对称翻转
Description :   
Author :          wellqin
date:             2019/8/2
Change Activity:  2019/8/2
-------------------------------------------------
"""

import collections

class Node:
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def maxDepth(self, root):
        if root == None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

    """
    BFS广度优先搜索，使用双端队列deque（因为性能比另外两种Queue好得多），
    在大循环内对二叉树的每个层做一次遍历，range(len(queue))使只遍历当前的层，
    每次大循环ans加1。由于每个节点仅访问一次，所以时间复杂度O(n)
    """
    def maxDepth3(self, root):
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 1

    def isSameTree(self, p, q):
        """
        时间复杂度: O(N)- 空间复杂度: O(1)******
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False

    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

        元素除了是 0、空、None、False 外都算 True。

        map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数  [1, 4, 9, 16, 25]
        map() 会根据提供的函数对指定序列做映射。
        """
        return p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) if p and q else p is q


# #给定一个二叉树，检查它是否是镜像对称的。
# #
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

    def isSymmetric1(self, root):
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


#翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#
# 输出：
#
#      4
#   /   \
#  7     2
# / \   / \
#9   6 3   1
#
# 备注:
#这个问题是受到 Max Howell 的 原问题 启发的 ：
#
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

"""
一个树是另一个树的子树 则

要么这两个树相等
要么这个树是左树的子树
要么这个树hi右树的子树
"""
class Solution12:
    def isSubtree(self, s, t):
        ss = []
        st = []

        def pre_order(node, res):
            if node:
                res.append(',' + str(node.val))
                pre_order(node.left, res)
                pre_order(node.right, res)
            else:
                res.append(',#')

        pre_order(s, ss)
        pre_order(t, st)

        return ''.join(st) in ''.join(ss)


t = Tree()
for i in range(7):
    t.add(i)
print('maxDepth:',t.maxDepth(t.root))
print('maxDepth13:',t.maxDepth3(t.root))
print('maxDepth13:',t.minDepth(t.root))