# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        二叉搜索树
Description :   
Author :          wellqin
date:             2019/8/2
Change Activity:  2019/8/2
-------------------------------------------------
"""
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorder(root):
            if not root:
                return []
            res = [root.val]
            left = inorder(root.left)
            right = inorder(root.right)

            return left + res + right

        if not root:
            return True
        node_order = inorder(root)
        while None in node_order:
            node_order.remove(None)

        for i in range(len(node_order) - 1):
            if node_order[i] >= node_order[i + 1]:
                return False
        return True

#二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
"""
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(N)******

先来个inorder然后再来一遍遍历看看哪两个node不符合inorder的顺序，再来一遍遍历swap这两个node就可以
"""
class Solution1:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []
        def midorder(root):
            if not root:
                return
            midorder(root.left)
            self.res.append(root.val)
            midorder(root.right)  # 请在不改变其结构的情况下，恢复这棵树。


        nodes = midorder(root)               # [1,3,null,null,2]
        sortedTrees = sorted(nodes)          # [3,1,null,null,2]

        diff = []
        for index, node in enumerate(nodes):
            if nodes[index] != sortedTrees[index]:
                diff.append(node)            # [1,3]

        def traverseAndSwap(root):
            if not root:
                return
            traverseAndSwap(root.left)
            if root.val == diff[0]:
                root.val = diff[1]
            elif root.val == diff[1]:
                root.val = diff[0]
        traverseAndSwap(root.right)

#给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
#输出: 5
#解释:
#给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
#

"""
思路 1

参照此处hint:

https://shenjie1993.gitbooks.io/leetcode-python/096%20Unique%20Binary%20Search%20Trees.html

首先明确n个不等的数它们能构成的二叉搜索树的种类都是相等的。而且1到n都可以作为二叉搜索树的根节点，
当k是根节点时，它的左边有k-1个不等的数，它的右边有n-k个不等的数。

以k为根节点的二叉搜索树的种类就是左右可能的种类的乘积。

用递推式表示就是 h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2) ，
其中h(0)=h(1)=1，因为0个或者1个数能组成的形状都只有一个。从1到n依次算出h(x)的值即可。此外这其实就是一个卡特兰数，
可以直接用数学公式计算，不过上面的方法更加直观一些。
"""


class Solution2(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            s = 0
            for k in range(i):
                s += dp[k]*dp[i-k-1]
            dp[i] = s
        return dp[-1]

#给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

#
# 示例:
#
# 输入: 3
#输出:
#[
#  [1,null,3,2],
#  [3,2,null,1],
#  [3,1,null,null,2],
#  [2,1,3],
#  [1,null,2,null,3]
#]
#解释:
#以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
#
#
"""
二叉搜索树（Binary Search Tree），也叫作二叉排序树（Binary Sort Tree），后文中统一简称为BST，顾名思义，它的每个结点的叶子数量不得超过两个

BST插入都是按照一定的规则顺序的，例如图中的结点，F的左边一定比F的值小，F右边一定比F的值大，当然这些都是可以自定义的，不过到头来，
总是要有一定的规则进行存储，这样才会方便我们用来检索需要的内容。

BST的基本操作相对于平衡树或者红黑树来讲算是非常简单的，BST并不在乎整个树的平衡性，仅仅保证了结点的有序规则不被打乱，
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
思路 1 - 时间复杂度: O(4^ N / sqrt(N))- 空间复杂度: O(4^ N / sqrt(N))******

因为知道这是一棵二叉搜索树，所以left.val < root.val < right.val
然后可以任意取一个node作为root，递归调用左边用返回的node作为left，递归调用右边用返回的node作为right
注意考虑n为0的情况，应该返回[]而不是[[]]

如果输入参数为有序数组，则很容易用递归法得到所有的二叉搜索树。故定义了一个 helper 函数。
小技巧：左右子树可能为空树，此时为了 for 循环能够正常进行，令其为 [None]。
"""

"""
求数目思路

参照此处hint:

https://shenjie1993.gitbooks.io/leetcode-python/096%20Unique%20Binary%20Search%20Trees.html

首先明确n个不等的数它们能构成的二叉搜索树的种类都是相等的。而且1到n都可以作为二叉搜索树的根节点，
当k是根节点时，它的左边有k-1个不等的数，它的右边有n-k个不等的数。

以k为根节点的二叉搜索树的种类就是左右可能的种类的乘积。

用递推式表示就是 h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2) ，
其中h(0)=h(1)=1，因为0个或者1个数能组成的形状都只有一个。从1到n依次算出h(x)的值即可。此外这其实就是一个卡特兰数，
可以直接用数学公式计算，不过上面的方法更加直观一些。
"""

"""
以n=5为例,枚举12345这五个根节点
1: 左:空 右:[2,3,4,5]组成的二叉搜索树
2: 左:[1] 右:[3,4,5]组成的二叉搜索树
3: 左:[1,2]组成的二叉搜索树, 右:[4,5]组成的二叉搜索树
4: 左:[1,2,3]组成的二叉搜索树,右:[5]
5: 左:[1,2,3,4]组成的二叉搜索树,右:空
定义函数helper(nums):作用为为给定的有序数组生成所有二叉搜索树
"""

class Solution4(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2, n+1):
            s = 0
            for k in range(i):
                s += dp[k]*dp[i-k-1]
            dp[i] = s

        print(dp[-1])
        return dp[-1]

    def generateTrees(self, n):
        if n == 0:
            return []

        # 为给定的有序数组生成所有二叉搜索树
        def helper(tree):
            # tree 为有序数组
            ans = []
            # 遍历可能的根结点
            for i, val in enumerate(tree):
                # left、right 分别为左右子树包含的结点
                left, right = tree[:i], tree[i + 1:]
                # 若左子树为 NULL，则令其为 [None]
                for ltree in helper(left) or [None]:
                    # 若右子树为 NULL，则令其为 [None]
                    for rtree in helper(right) or [None]:
                        root = TreeNode(val)
                        root.left, root.right = ltree, rtree
                        ans.append(root)
            return ans
        # print(helper(range(1, n + 1)))
        # print(len(helper(range(1, n + 1))))
        return helper(range(1, n + 1))

sl = Solution()
# sl.generateTrees(3)
# sl.numTrees(3)


#给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
#你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#输出: 1
#
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#输出: 3
#
# 进阶：
#如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1

        if not root:
            return None
        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left - 1)

t = Tree()
for i in [5,3,6,2,4,"None","None",1 ]:
    t.add(i)
print('kthSmallest:',t.kthSmallest(t.root, 7))




"""
代码基于python实现，时间击败100%
解题思路：
二叉搜索树的定义是：
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
它的左、右子树也分别为二叉排序树。

我们依旧使用递归
以不同的数作为root，
这就由i左边的数可以构成什么样的二叉搜索树，
i右边的数可以构成什么样的二叉搜索树决定。

接着我们就会在i的左边去找一个左子树root，在i的右边去找一个右子树的root，这就是递归的过程。
"""


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return list()

        mem = dict()
        self._generateTrees(1, n, mem)
        return mem[(1, n)]

    def _generateTrees(self, left, right, mem):
        if left > right:
            return [None]
        if (left, right) in mem:
            return mem[(left, right)]

        res = list()
        for i in range(left, right + 1):
            left_nodes = self._generateTrees(left, i - 1, mem)
            right_nodes = self._generateTrees(i + 1, right, mem)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)

        mem[(left, right)] = res
        return res

"""
更多leetcode解法更新在我的github上
如果我的代码对你有帮助，可不可以给我一个star
我的github地址：https://github.com/MayYoung1/leetcode
"""

#给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
#你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#输出: 1
#
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#输出: 3
#
# 进阶：
#如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node1:
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None

class Tree1:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node1(item)
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

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def count(node):
            if not node:
                return 0
            return count(node.left) + count(node.right) + 1

        if not root:
            return None
        left = count(root.left)
        if left == k - 1:
            return root.val
        elif left > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - left - 1)

t = Tree1()
for i in [5,3,6,2,4,"None","None",1 ]:
    t.add(i)
print('kthSmallest:',t.kthSmallest(t.root, 7))





def VerifySquenceOfBST(sequence):
    if sequence == []:
        return False
    if len(sequence) == 1 or len(sequence) == 2:
        return True
    else:
        root = sequence.pop(-1)
        sign = 0
        for i in range(len(sequence)):
            if sequence[i] > root:
                sign = 1
            if (sign == 1) and (sequence[i] < root):
                return False
        return VerifySquenceOfBST(sequence[:i]) and VerifySquenceOfBST(sequence[i:])

print('VerifySquenceOfBST:',VerifySquenceOfBST([4, 5, 2 , 3, 1]))




















