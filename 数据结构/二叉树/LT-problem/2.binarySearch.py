# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        binarySearch
Description :   
Author :          wellqin
date:             2020/3/18
Change Activity:  2020/3/18
func :  二、 二叉树的搜索
        1. 二叉树最后一行最左边的值
        2. 在二叉树的每一行中找到最大的值
        3. 二叉树中第二小的节点(遍历排序找第二)

        # 4. 每个节点的右向指针I：[116]填充每个节点的下一个右侧节点指针
        # 5. 每个节点的右向指针II [117]

        6. 二叉树中增加一行
        7. 二叉树的层平均值
        8. 二叉树左叶子节点的和
        9. 二叉树的右视图

        10. 二叉树中两个节点的最低公共祖先(LCA)  +   BTS的最低公共祖先(LCA)
        11. 合并两个二叉树
        12. 最大值二叉树(由数组构建二叉树)
        13. 二叉树的坡度: 坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值
                        整个树的坡度就是其所有节点的坡度之和。




-------------------------------------------------
"""
from functools import reduce
from typing import List


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.left)
                queue.append(cur_node.right)

    def travel(self, root):
        def helper(node, level):
            if not node:
                return []
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            helper(node.left, level + 1)
            helper(node.right, level + 1)  # [[0], [1, 2], [3, 4, 5, 6]]

        res = [[]]
        helper(root, 1)
        return res[:-1]


tree = Tree()
for i in range(7):
    tree.add(i)
print(tree.travel(tree.root))
node = tree.root


class Solution(object):
    def findBottomLeftValue(self, root):  # 二叉树的最左下树
        # 层次遍历后，最后元素的第一个就是最左下树节点
        def helper(node, level):
            if not node:
                return []
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        res = [[]]
        helper(root, 1)

        return res[-2][0]

    def largestValues(self, root):  # 在二叉树的每一行中找到最大的值
        def helper(root, level):
            if not root:
                return []
            else:
                res[level - 1].append(root.val)
                if len(res) == level:
                    res.append([])
                helper(root.left, level + 1)
                helper(root.right, level + 1)

        res = [[]]
        helper(root, 1)
        return [max(i) for i in res[:-1]]

    def averageOfLevels(self, root):
        res = Tree().travel(root)
        return [sum(i) / len(i) for i in res]

    def sumOfLeftLeaves(self, root):
        # 不能用层序遍历的结果来进行左叶子之和统计
        # 比如：[1,null,2] 会输出2，而结果为0.就是因为当左子树不存在时，层序遍历的第一项为右子树，逻辑错误

        # res = Tree().travel(root)
        # print(res)
        # if len(res) > 1:
        #     total = reduce(lambda x, y: x + y, [i[0] for i in res[1:] if i])
        # else:
        #     total = root.val
        # return total

        """应该在遍历过程中进行处理，而不是对遍历结果进行处理,注意是有左叶子Nil"""

        def helper(root, level):
            if not root:
                return 0
            else:
                # 当前节点的左节点存在，并且！！！此左节点是Nil节点
                if root.left and not root.left.right and not root.left.left:
                    res.append(root.left.val)
                helper(root.left, level + 1)
                helper(root.right, level + 1)

        res = []
        helper(root, 1)
        return res

    def rightSideView(self, root):
        res = Tree().travel(root)
        return [i[-1] for i in res if i]

    def lowestCommonAncestor(self, root, p, q):  # 二叉树中两个节点的最低公共祖先(LCA)
        # solution 1 普通二叉树递归寻找
        """

        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

        """
        # solution 2 ：二叉搜索树分情形寻找，左小右大于root节点
        # 情形1：p, q一个大于root，一个小于root
        # 情形2：p, q都比root小，去左边找
        # 情形3：p, q都比root大，去右边找
        # 因为分区间寻找，所以递归结果直接返回，没有区分左右在进行判断
        if not root:
            return root
        if root.val > p.val and root.val > q.val:  # 情形2
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:  # 情形3
            return self.lowestCommonAncestor(root.right, p, q)
        return root  # 情形1

    def mergeTrees(self, t1: Node, t2: Node) -> Node:  # 合并两个二叉树
        if not t1 and t2:
            return t2
        elif t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def constructMaximumBinaryTree(self, nums: List[int]) -> Node:
        if not nums:
            return Node()
        root = Node(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums)) + 1:])
        return root

    def findTilt(self, root):
        res = [0]  # python中list作为全局变量无需global声明,若为变量则加上global声明

        # 二叉树的坡度: 坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值
        def tile(node):
            if not node:
                return 0
            left = tile(node.left)
            right = tile(node.right)
            res[0] += abs(left - right)  # global ret
            return left + right + node.val

        tile(root)
        return res[0]


print(Solution().findBottomLeftValue(node))
print(Solution().largestValues(node))
print(Solution().averageOfLevels(node))

print(Solution().sumOfLeftLeaves(node))
