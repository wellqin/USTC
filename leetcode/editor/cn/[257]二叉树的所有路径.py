# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。 
#
# 示例: 
#
# 输入:
#
#   1
# /   \
# 2     3
# \
#  5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, item):
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

    def binaryTreePaths(self, root):
        res = []
        if not root:
            return res
        for g in self.helper(root):
            res.append('->'.join(g))
        return res

    def helper(self, root, temp=[]):
        if root:
            temp.append(str(root.val))
            if not root.left and not root.right:
                yield temp
            yield from self.helper(root.left, temp)
            yield from self.helper(root.right, temp)
            temp.pop()


t = Tree()
for i in range(7):
    t.add(i)
print('先序遍历:', t.binaryTreePaths(t.root))
