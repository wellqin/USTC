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

class Solution(object):
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
sl.generateTrees(3)
# sl.numTrees(3)




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




















