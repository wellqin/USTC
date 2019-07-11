#给定一个二叉树，找出其最大深度。 
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
#
# 说明: 叶子节点是指没有子节点的节点。 
#
# 示例： 
#给定二叉树 [3,9,20,null,null,15,7]， 
#
#     3
#   / \
#  9  20
#    /  \
#   15   7 
#
# 返回它的最大深度 3 。 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

    def maxDepth(self, root):
        if root == None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

t = Tree()
for i in range(7):
    t.add(i)
print('maxDepth1:',t.maxDepth(t.root))

class Solution:
    def maxDepth(self, root):
        """

        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        level = 0
        node_list = []

        node_list.append(root)
        while node_list:
            node = node_list.pop(0)
            level += 1
            if node.left.val is not None:
                node_list.append(node.left)
            if node.right.val is not None:
                node_list.append(node.right)

        return level

    def maxDepth1(self, root):
        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

















