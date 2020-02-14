# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        preorder
Description :   
Author :          wellqin
date:             2020/1/30
Change Activity:  2020/1/30
-------------------------------------------------
"""
# 构建了层序遍历: [0, 1, 2, 3, 4, 5, 6]的二叉树
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            while True:
                cur_node = queue.pop(0)
                if cur_node.left is None:
                    cur_node.left = node
                    return
                elif cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
    def traverse(self, root):  # 层次遍历
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return res
tree = Tree()
for i in range(7):
    tree.add(i)
print('层序遍历:', tree.traverse(tree.root))


# 递归：前序遍历
def preorder(root):
    if not root:
        return []
    res = [root.val]
    left = preorder(root.left)
    right = preorder(root.right)
    return res + left + right
print("递归：前序遍历", preorder(tree.root))

# 非递归：前序遍历
def preorder1(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
print("非递归：前序遍历", preorder1(tree.root))

# 非递归：前序遍历2 == 优化版
# 尾递归：是递归调用在递归实例体的尾部，这样的递归很容易化解为迭代，需要引入一个辅助栈即可
from memory_profiler import profile
@profile
def preorder2(root):
    if not root:
        return []
    stack = []
    res = []
    cur = root
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res
print("非递归：前序遍历2", preorder2(tree.root))

