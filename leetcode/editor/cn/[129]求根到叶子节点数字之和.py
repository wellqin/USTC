# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。 
#
# 计算从根到叶子节点生成的所有数字之和。 
#
# 说明: 叶子节点是指没有子节点的节点。 
#
# 示例 1: 
#
# 输入: [1,2,3]
#    1
#   / \
#  2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
# 示例 2: 
#
# 输入: [4,9,0,5,1]
#    4
#   / \
#  9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Solution:

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

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
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


t = Solution()
for i in range(1, 4):
    t.add(i)
print('遍历:', t.sumNumbers(t.root))
