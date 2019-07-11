# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        二叉查找树
Description :   
Author :          wellqin
date:             2019/7/9
Change Activity:  2019/7/9
-------------------------------------------------
"""

"""
1. 二叉查找树的定义：
左子树不为空的时候。左子树的结点值小于根节点，右子树不为空时，右子树的结点值大于根节点。左右子树分别为二叉查找树

2. 二叉查找树的最左边的结点即为最小值，要查找最小值。仅仅需遍历左子树的结点直到为空为止。同理，最右边的结点结尾最大值。
要查找最大值，仅仅需遍历右子树的结点直到为空为止。

二叉查找树的插入查找和删除都是通过递归的方式来实现的，删除一个结点的时候，先找到这个结点S，假设这个结点左右孩子都不为空，
这时并非真正的删除这个结点S，而是在其右子树找到后继结点，将后继结点的值付给S，然后删除这个后继结点就可以。

假设结点S的左孩子或者右孩子为空，能够直接删除这个结点S。
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        root = TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)  # 递归地插入元素
        elif val > root.val:
            root.right = insert(root.right, val)
    return root


def query(root, val):
    if root is None:
        return
    if root.val is val:
        return True
    if root.val < val:
        return query(root.right, val)  # 递归地查询
    else:
        return query(root.left, val)


def findmin(root):
    if root.left:
        return findmin(root.left)
    else:
        return root

def delnum(root, val):
    if root is None:
        return
    if val < root.val:
        return delnum(root.left, val)
    elif val > root.val:
        return delnum(root.right, val)
    else:  # 删除要区分左右孩子是否为空的情况
        if (root.left and root.right):
            tmp = findmin(root.right)  # 找到后继结点
            root.val = tmp.val
            root.right = delnum(root.right, val)  # 实际删除的是这个后继结点

        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
    return root


# 測试代码
root = TreeNode(3)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 4)
print(root)
print(query(root,5))
print(query(root, 1))
root = delnum(root, 1)
print(query(root, 1))



"""
# encoding=utf-8
import queue


class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.father = None


class BST(object):
    def __init__(self, nodeList):
        self.root = None
        for node in nodeList:
            self.bfs_insert(node)

    def bfs_insert(self, node):
        father = None
        cur = self.root

        while cur != None:
            if cur.value == node.value:
                return -1
            father = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        node.father = father
        if father == None:
            self.root = node
        elif node.value < father.value:
            father.left = node
        else:
            father.right = node

    def bfs(self):
        if self.root == None:
            return None
        retList = []
        q = queue.Queue()
        q.put(self.root)
        while q.empty() is not True:
            node = q.get()
            retList.append(node.value)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
        return retList

    def bfs_search(self, value):
        cur = self.root
        while cur != None:
            if cur.value == value:
                return cur
            elif cur.value < value:
                cur = cur.right
            else:
                cur = cur.left
        return None

    def bfs_delete(self, node):
        father = node.father
        if node.left == None:
            if father == None:
                self.root = node.right
                if node.right != None:
                    node.right.father = None
            elif father.left == node:
                father.left = node.right
                if node.right != None:
                    node.right.father = father
            else:
                father.right = node.right
                if node.right != None:
                    node.right.father = father
            return 'delete successfully'
        tmpNode = node.left
        while tmpNode.right != None:
            tmpNode = tmpNode.right

        tmpNode.right = node.right
        if node.right != None:
            node.right.father = tmpNode

        if father == None:
            self.root = node.left
            node.left.father = None
        elif father.left == node:
            father.left = node.left
            node.left.father = father
        else:
            father.right = node.left
            node.left.father = father
        node = None
        return 'delete successfully'


if __name__ == '__main__':
    varList = [24, 34, 5, 4, 8, 23, 45, 35, 28, 6, 29]
    nodeList = [TreeNode(var) for var in varList]
    bst = BST(nodeList)
    print(bst.bfs())
    node = bst.bfs_search(34)
    bst.bfs_delete(node)
    print(bst.bfs())
"""