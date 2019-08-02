# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        构造树
Description :   
Author :          wellqin
date:             2019/8/1
Change Activity:  2019/8/1
-------------------------------------------------
"""

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

    def traverse(self, root):  # 层次遍历
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.item)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return res

t = Tree()
for i in range(7):
    t.add(i)
print('层序遍历:',t.traverse(t.root))
