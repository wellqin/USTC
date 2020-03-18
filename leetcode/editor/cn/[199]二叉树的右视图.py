# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例: 
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#   1            <---
# /   \
# 2     3         <---
# \     \
#  5     4       <---
# 
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

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        cur_level = [root]
        while cur_level:
            next_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp_res)
            cur_level = next_level
        return res

    def rightSideView1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        def helper(root, level):
            if not root:
                return []
            res[level - 1].append(root.val)
            if len(res) == level:
                res.append([])
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        res = [[]]
        helper(root, 1)
        res = res[:-1]
        result = []
        for i in res:
            result.append(i[-1])
        return result

    def leftSideView1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        def helper(root, level):
            if not root:
                return []
            res[level - 1].append(root.val)
            if len(res) == level:
                res.append([])
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        res = [[]]
        helper(root, 1)
        res = res[:-1]
        result = []
        for i in res:
            result.append(i[0])
        return result

    def traverse1(self, root):  # 层次遍历
        if root == None:
            return []
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return res


t = Tree()
for i in range(1, 7):
    t.add(i)
print('cengci遍历:', t.rightSideView(t.root))
print('traverse1遍历:', t.traverse1(t.root))
print('rightSideView1:', t.rightSideView1(t.root))
print('leftSideView1:', t.leftSideView1(t.root))
