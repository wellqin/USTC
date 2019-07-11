#给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。 
#
# 说明： 
#你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。 
#
# 示例 1: 
#
# 输入: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#输出: 1 
#
# 示例 2: 
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#输出: 3 
#
# 进阶： 
#如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？ 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1

        if not root:
            return None
        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left - 1)

t = Tree()
for i in [5,3,6,2,4,"None","None",1 ]:
    t.add(i)
print('kthSmallest:',t.kthSmallest(t.root, 7))