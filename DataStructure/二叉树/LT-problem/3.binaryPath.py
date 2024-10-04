# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.binaryPath
Description :   
Author :          wellqin
date:             2020/3/18
Change Activity:  2020/3/18

func :  三、 二叉树的路径

[112] Path Sum：路径和(一)-是否存在二叉树路径和等于给定值（根节点到叶子节点）-- 返回是否存在

[113] Path Sum II：路径和(二)-二叉树中路径和等于给定值的所有路径（根节点到叶子节点）-- 返回所有路径

[437] Path Sum III：路径和(三)-二叉树中路径和等于给定值的所有路径（任意两个节点）-- 返回所有路径
        路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）

[257] Binary Tree Paths：二叉树从根节点到叶子节点的所有路径  -- 返回所有路径，不用是路径和为指定值

[124] Binary Tree Maximum Path Sum：二叉树中任意两个节点之间路径和的最大值（二叉树的最大路径和）

[129] Sum Root to Leaf Numbers：所有“根到叶子”路径和的和

[543] Diameter of Binary Tree：二叉树的直径（二叉树任意两个节点之间路径的最大长度）
        一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

[687] Longest Univalue Path：最长相同值路径

二叉树的最大距离（即相距最远的两个叶子节点）：https://blog.csdn.net/liuyi1207164339/article/details/50898902
-------------------------------------------------
"""


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
            """
            # 加上奇偶判断可以实现锯齿遍历
            # [[0], [2, 1], [3, 4, 5, 6]] 
            # if level % 2 == 1:
            #     res[level - 1].append(node.val)
            # else:
            #     res[level - 1].insert(0, node.val)
            """
            res[level - 1].append(node.val)
            if len(res) == level:
                res.append([])
            helper(node.left, level + 1)
            helper(node.right, level + 1)  # [[0], [1, 2], [3, 4, 5, 6]]

            """
            # left与right互换则是从右到左遍历
            # helper(node.right, level + 1)
            # helper(node.left, level + 1)  # [[0], [2, 1], [6, 5, 4, 3]]
            """

        res = [[]]
        helper(root, 1)
        return res[:-1]


tree = Tree()
for i in range(7):
    tree.add(i)
print(tree.travel(tree.root))
node = tree.root


class Solution(object):
    # 路径和(一) - 是否存在二叉树路径和等于给定值（根节点到叶子节点）-- 返回是否存在
    # 路径和(二) - 二叉树中路径和等于给定值的所有路径（根节点到叶子节点）-- 返回所有路径
    def hasPathSum1(self, root, sum):
        if not root:
            return False

        if root.left or root.right:
            return self.hasPathSum1(root.left, sum - root.val) or self.hasPathSum1(root.right, sum - root.val)
        else:
            return root.val == sum  # 递归出口

    def hasPathSum2(self, root, Sum):
        if not root:
            return False

        def helper(root, cur):

            if root.left:
                helper(root.left, cur + [root.left.val])
            if root.right:
                helper(root.right, cur + [root.right.val])
            if not root.right and not root.left:  # 已经到了Nil节点才进行判断
                if sum(cur) == Sum:
                    res.append(cur)  # 返回所有路径

        res = []
        helper(root, [root.val])
        return res

    # 路径和(三)-二叉树中路径和等于给定值的所有路径（任意两个节点）-- 返回所有路径
    # 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）
    def hasPathSum3(self, root, sum):
        # 递归往下一次深度遍历根节点循环
        res = [0]
        if root is None:
            return res[0]

        def getPathNum(root, Sum):
            # 依据当前树找目标值，进而找到路径数量
            if root is None:
                return
            if root.val == Sum:
                res[0] += 1

            getPathNum(root.left, Sum - root.val)
            getPathNum(root.right, Sum - root.val)

        # 以当前点为起点往下是否有path + 以当前点的左节点为起点往下是否有path + 当前点的右节点为起点往下是否有path
        getPathNum(root, sum)
        self.hasPathSum3(root.left, sum)
        self.hasPathSum3(root.right, sum)

        return res[0]

    def hasPathSum31(self, root, Sum):
        res = []
        if not root:
            return []

        def getPathNum(root, cur):
            # 依据当前树找目标值，进而找到具体路径
            if not root:
                return
            if root.left:
                getPathNum(root.left, cur + [root.left.val])
            if root.right:
                getPathNum(root.right, cur + [root.right.val])
            if sum(cur) == Sum:  # 不用到了Nil节点才进行判断
                res.append(cur)

        # 以当前点为起点往下是否有path + 以当前点的左节点为起点往下是否有path + 当前点的右节点为起点往下是否有path
        getPathNum(root, [root.val])
        self.hasPathSum31(root.left, Sum)
        self.hasPathSum31(root.right, Sum)

        return res

    def binaryTreePaths(self, root):
        # 二叉树从根节点到叶子节点的所有路径  -- 返回所有路径，不用是路径和为指定值

        def helper(root, cur):
            if not root:
                return []
            if root.left:
                helper(root.left, cur + [root.left.val])
            if root.right:
                helper(root.right, cur + [root.right.val])
            if not root.left and not root.right:
                res.append(cur)

        res = []
        helper(root, [root.val])
        print(res)  # [[0, 1, 3], [0, 1, 4], [0, 2, 5], [0, 2, 6]]
        result = ['->'.join([str(i) for i in item]) for item in res]

        return result

    # 二叉树中任意两个节点之间路径和的最大值（二叉树的最大路径和）
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue(root)
        return self.result

    """
    最大路径和：根据当前节点的角色，路径和可分为两种情况：
    一：以当前节点为根节点
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    4.当前节点+左右子树    
    这四种情况的最大值即为以当前节点为根的最大路径和
    此最大值要和已经保存的最大值比较，得到整个树的最大路径值

    二：当前节点作为父节点的一个子节点
    和父节点连接的话则需取【单端的最大值】
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    这三种情况的最大值    
    """

    def maxValue(self, root):
        if root is None:
            return 0

        leftValue = self.maxValue(root.left)
        rightValue = self.maxValue(root.right)

        value1 = root.val
        value2 = root.val + leftValue
        value3 = root.val + rightValue
        value4 = root.val + rightValue + leftValue

        # 以此节点为根节点的最大值
        maxValue = max([value1, value2, value3, value4])

        # 当前遍历树的最大值
        self.result = max(maxValue, self.result)

        # 要和父节点关联，则需要取去除情况4的最大值
        return max([value1, value2, value3])

    # 所有“根到叶子”路径和的和
    def sumNumbers1(self, root):

        def helper(root, cur):
            if not root:
                return 0
            if root.left:
                helper(root.left, cur + [root.left.val])
            if root.right:
                helper(root.right, cur + [root.right.val])
            if not root.left and not root.right:
                res.append(cur)

        res = []
        helper(root, [root.val])
        # ['->'.join([str(i) for i in item]) for item in res]
        result = map(int, ["".join([str(i) for i in item]) for item in res])
        # print(sum(list(result)))
        return sum(list(result))

    def sumNumbers2(self, root):
        res = []
        self.auxPathSum(root, [], res)
        return sum(res)

    def auxPathSum(self, root, cur_list, cur_lists):
        if not root:
            return
        if not root.left and not root.right:
            # cur_lists.append(cur_list + [root.item])
            cur_lists.append(int(''.join(str(i) for i in cur_list + [root.item])))
            return
        if root.left:
            self.auxPathSum(root.left, cur_list + [root.item], cur_lists)
        if root.right:
            self.auxPathSum(root.right, cur_list + [root.item], cur_lists)

    # 二叉树的直径（二叉树任意两个节点之间路径的最大长度）:边的数目表示
    # 一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
    # 根节点为root的二叉树的直径 = max(root->left的直径，root->right的直径，root->left的最大深度+root->right的最大深度+1)
    def diameterOfBinaryTree(self, root: Node) -> int:
        res = [0]

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res[0] = max(res[0], left + right)
            return max(left, right) + 1

        helper(root)
        return res[0]


print(Solution().hasPathSum1(node, 7))
print(Solution().hasPathSum2(node, 7))
print(Solution().hasPathSum3(node, 7))
print(Solution().hasPathSum31(node, 7))
print(Solution().binaryTreePaths(node))
print(Solution().sumNumbers1(node))
print(Solution().diameterOfBinaryTree(node))
