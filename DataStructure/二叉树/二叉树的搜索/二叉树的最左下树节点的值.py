# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        二叉树的最左下树节点的值
Description :   
Author :          wellqin
date:             2020/1/31
Change Activity:  2020/1/31
-------------------------------------------------
"""
# https://www.cnblogs.com/ArsenalfanInECNU/p/5346751.html
# from .CreateTree import Tree
from DataStructure.二叉树.二叉树的搜索.CreateTree import Node, Tree


def traverse(root):  # 层次遍历
    if root is None:
        return []
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res


t = Tree()
for i in range(6):
    t.add(i)
print('层序遍历:', traverse(t.root))


def FindLeft(root):
    if not root:
        return -1
    cur = root
    while cur.left:
        cur = cur.left
    return cur.val


print(FindLeft(t.root))

