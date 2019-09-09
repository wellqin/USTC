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

    def maxDepth1(self, root):
        """

        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        level1 = 0
        level2 = 0
        node_list = []
        node_list.append(root)
        while node_list:
            node = node_list.pop(0)
            if node.left:
                level1 += 1
                node_list.append(node.left)
            if node.right:
                level2 += 1
                node_list.append(node.right)

        return max(level1, level2)

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

t = Tree()
for i in range(7):
    t.add(i)
print('maxDepth:',t.maxDepth(t.root))
print('maxDepth1:',t.maxDepth1(t.root))
print('maxDepth13:',t.maxDepth3(t.root))

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
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

















