# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        testFile
Description :   
Author :          wellqin
date:             2020/1/30
Change Activity:  2020/1/30
-------------------------------------------------
"""
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
for i in range(6):
    tree.add(i)
print('层序遍历:', tree.traverse(tree.root))


