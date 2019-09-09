#给出一个完全二叉树，求出该树的节点个数。 
#
# 说明： 
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。 
#
# 示例: 
#
# 输入: 
#    1
#   / \
#  2   3
# / \  /
#4  5 6
#
#输出: 6 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root:
            return 0

        stack = []
        node = root
        while node or (len(stack) > 0):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return len(res)

class Node:
    def __init__(self,item):
        self.item = item
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

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return 1 + left + right

    def countNodes1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        p, q = root, root

        lmh, rmh = 0, 0
        while p:
            p = p.left
            lmh += 1
        while q:
            q = q.right
            rmh += 1

        if lmh == rmh:
            return 2 ** lmh - 1
        else:
            return 1 + self.countNodes1(root.left) + self.countNodes1(root.right)

t = Tree()
for i in range(1, 7):
    t.add(i)
print('节点数:',t.countNodes(t.root))
print('节点数:',t.countNodes1(t.root))