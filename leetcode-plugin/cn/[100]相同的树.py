#给定两个二叉树，编写一个函数来检验它们是否相同。 
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
#
# 示例 1: 
#
# 输入:       1         1
#          / \       / \
#         2   3     2   3
#
#        [1,2,3],   [1,2,3]
#
#输出: true 
#
# 示例 2: 
#
# 输入:      1          1
#          /           \
#         2             2
#
#        [1,2],     [1,null,2]
#
#输出: false
# 
#
# 示例 3: 
#
# 输入:       1         1
#          / \       / \
#         2   1     1   2
#
#        [1,2,1],   [1,1,2]
#
#输出: false
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):

        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False

        self.res = []

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)

            return self.res

        pNode = inorder(p)
        qNode = inorder(q)


        # 比较二个列表是否相同
        # L1 = [1, ('a', 3)]  # same value, unique objects
        # L2 = [1, ('a', 3)]
        # print(L1 == L2, L1 is L2)  # equivalent?, same object?
        # ==表示值相同， is代表是同一个对象

        return pNode == qNode

"""
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(1)******

递归
"""
class Solution0(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""一行版本"""

class Solution1(object):
    def isSameTree(self, p, q):
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

class Solution2:
    def isSameTree(self, p, q):
        """
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


aa = [1,2]
bb = [1,null,2]
if len(aa) == len(bb):
    print(aa == bb)
else:
    print(False)