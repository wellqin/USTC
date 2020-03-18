# 给定一个二叉树，计算整个树的坡度。
#
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。 
#
# 整个树的坡度就是其所有节点的坡度之和。 
#
# 示例: 
#
# 
# 输入:
#         1
#       /   \
#      2     3
# 输出: 1
# 解释:
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
# 
#
# 注意: 
#
# 
# 任何子树的结点的和不会超过32位整数的范围。 
# 坡度的值不会超过32位整数的范围。 
# 
#

# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
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

    def findTilt(self, root):
        ret = [0]  # python中list作为全局变量无需global声明

        def tile(node):
            if not node: return 0
            left = tile(node.left)
            right = tile(node.right)
            ret[0] += abs(left - right)
            return left + right + node.val

        tile(root)

        return ret[0]


tt = Solution()
for i in range(1, 4):
    tt.add(i)

print('findTilt:', tt.findTilt(tt.root))
