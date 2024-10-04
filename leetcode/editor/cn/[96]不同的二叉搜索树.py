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
        return dp[-1]
        