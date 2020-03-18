# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
#
# 示例 1: 
#
# 输入:
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 
#
# 注意： 
#
# 
# 节点值的范围在32位有符号整数范围内。 
# 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def helper(node, level):
            if not node:
                return
            else:
                # 层次遍历
                sol[level - 1].append((node.val))

                # # 锯齿遍历
                # if level % 2 == 1:
                #     sol[level - 1].append(node.val)
                # else:
                #     sol[level - 1].insert(0, node.val)

                if len(sol) == level:  # 遍历到新层时，只有最左边的结点使得等式成立
                    sol.append([])
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        sol = [[]]
        helper(root, 1)
        qw = sol[:-1]
        result = []
        for l in qw:
            result.append(sum(l) / len(l))
        # return [sum(i)/len(i) for i in res]
        return result
