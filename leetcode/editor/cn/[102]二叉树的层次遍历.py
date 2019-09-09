#coding:utf-8
#给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如: 
#给定二叉树: [3,9,20,null,null,15,7], 
#
#     3
#   / \
#  9  20
#    /  \
#   15   7
# 
#
# 返回其层次遍历结果： 
#
# [
#  [3],
#  [9,20],
#  [15,7]
#]
# 
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
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

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node, level):
            if not node:
                return
            else:
                # 层次遍历
                sol[level-1].append(node.val)

                # # 锯齿遍历
                # if level % 2 == 1:
                #     sol[level - 1].append(node.val)
                # else:
                #     sol[level - 1].insert(0, node.val)

                if len(sol) == level:  # 遍历到新层时，只有最左边的结点使得等式成立
                    sol.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
        sol = [[]]
        helper(root, 1)
        return sol[:-1]

    def traverse(self, root):  # 层次遍历
        if root is None:
            return None
        q = [root]
        res = [root.val]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.val)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.val)
        return res

    def traverse_route(self, node):
        if not node.left and not node.right:
            return [str(node.val)]
        left, right = [], []
        if node.left:
            left = [str(node.val) + x for x in self.traverse_route(node.left)]
        if node.right:
            right = [str(node.val) + x for x in self.traverse_route(node.right)]

        return left + right

    # 思路 1 - 时间复杂度: O(N)- 空间复杂度: O(N)******
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res, cur_level, level_count = [], [root], 0
        while cur_level:
            next_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_count % 2 == 0:
                res.append(tmp_res)
            else:
                tmp_res.reverse()
                res.append(tmp_res)
            level_count += 1
            cur_level = next_level

        return res

    # 二叉树深度
    def maxDepth(self, root):
        """

        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        level = 0
        node_list = []

        node_list.append(root)
        while node_list:
            node = node_list.pop(0)
            level += 1
            if node.left is not None:
                node_list.append(node.left)

            if node.right is not None:
                node_list.append(node.right)

        return level
    """
    同样是利用递归的方法来解决此题，根结点不为空，我们就递归遍历左子树和右子树，看哪一个子树的层数更多，最后直至遍历到叶子结点；

    运用一条语句技巧性的实现：return nleft > nright ? nleft + 1 : nright + 1;
    其实此方法的主要思想就是：只要递归遍历一直到此树的叶子结点，最后只要从叶子结点开始一直向根结点回溯并+1，结果就是回溯经过的路径长度+1.
    """
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(map(self.maxDepth, [root.left, root.right])) \
            if root != None else 0

        # if root == None:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        if root == None:
            return 0
        left = self.maxDepth2(root.left)
        right = self.maxDepth2(root.right)

        return 1 + max(left, right)

t = Solution()
for i in range(10):
    t.add(i)

print('levelOrder:',t.levelOrder(t.root))
print('levelOrder:',t.traverse(t.root))
print('锯齿遍历:',t.zigzagLevelOrder(t.root))
print('路径遍历:',t.traverse_route(t.root))
print('maxDepth:',t.maxDepth(t.root))
print('maxDepth1:',t.maxDepth1(t.root))
print('maxDepth2:',t.maxDepth2(t.root))