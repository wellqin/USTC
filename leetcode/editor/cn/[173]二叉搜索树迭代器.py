#实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。 
#
# 调用 next() 将返回二叉搜索树中的下一个最小的数。 
#
# 
#
# 示例： 
#
# 
#
# BSTIterator iterator = new BSTIterator(root);
#iterator.next();    // 返回 3
#iterator.next();    // 返回 7
#iterator.hasNext(); // 返回 true
#iterator.next();    // 返回 9
#iterator.hasNext(); // 返回 true
#iterator.next();    // 返回 15
#iterator.hasNext(); // 返回 true
#iterator.next();    // 返回 20
#iterator.hasNext(); // 返回 false 
#
# 
#
# 提示： 
#
# 
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。 
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。 
# 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        temp = self.stack.pop()
        res = temp.val
        temp = temp.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return res

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack != []

# 一开始就取巧，用InOrder，这样得到BSF有序排列，然后使用
class BSTIterator1(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.pushAllLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            cur = self.stack.pop()
            if cur.right:
                self.pushAllLeft(cur.right)
            return cur.val

    def pushAllLeft(self, node):
        """
        :type node: TreeNode
        """
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left


"""
谷歌了一下，得到如何满足题目要求的hint，从root开始，往左走，把左孩子压入stack，直到左边为空。
然后开始取node，如果node有右孩子，则同样要把node的右孩子的所有左孩子全部append入stack，画了一个图，可行。
"""
class BSTIterator2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.pushAllLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            cur = self.stack.pop()
            if cur.right:
                self.pushAllLeft(cur.right)
            return cur.val

    def pushAllLeft(self, node):
        """
        :type node: TreeNode
        """
        cur = node
        while cur:
            self.stack.append(cur)
            cur = cur.left
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()