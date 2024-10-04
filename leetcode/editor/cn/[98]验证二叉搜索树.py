#给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
#
# 假设一个二叉搜索树具有如下特征： 
#
# 
# 节点的左子树只包含小于当前节点的数。 
# 节点的右子树只包含大于当前节点的数。 
# 所有左子树和右子树自身必须也是二叉搜索树。 
# 
#
# 示例 1: 
#
# 输入:
#    2
#   / \
#  1   3
#输出: true
# 
#
# 示例 2: 
#
# 输入:
#    5
#   / \
#  1   4
#     / \
#    3   6
#输出: false
#解释: 输入为: [5,1,4,null,null,3,6]。
#     根节点的值为 5 ，但是其右子节点值为 4 。
# 
#
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
思路 1 - 时间复杂度: O(N)- 空间复杂度: O(N)******
中序遍历一次，看看list是否严格满足递增
"""

class Solution:

    def __init__(self):
        self.root = None

    def add(self, val):
        node = TreeNode(val)
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

    def isValidBST(self, root):

        def inorder(root):
            if not root:    # 递归终止条件，不返回值，默认none，到叶子节点就终止了
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)      # 不用return

        res = []   # 排好序的节点存在着里面，是节点，不是节点的值,res.append(root.val)就是节点值了

        """
        self.res = []

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)
            return self.res         # 这种写法也可以，不过需要返回return self.res
        """

        if not root:
            return True
        inorder(root)
        for i in range(1, len(res)):
            if res[i].val <= res[i - 1].val:
                return False
        return True

    def isValidBST1(self, root):  # 实际上就是每次往下看，node都确保被夹在一个范围。
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(root, smallest, largest):
            if not root:
                return True
            if smallest >= root.val or largest <= root.val:
                return False
            return valid(root.left, smallest, root.val) and valid(root.right, root.val, largest)

        if not root:
            return True
        return valid(root, -sys.maxsize, sys.maxsize)



    def isValidBST123(self, root):
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

t = Solution()
for i in [5, 1, 4, None, None, 3, 6]:
    t.add(i)

# print('isValidBST:',t.isValidBST(t.root))
print('isValidBST:',t.isValidBST123(t.root))





















        