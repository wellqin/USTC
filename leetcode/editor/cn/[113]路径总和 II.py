# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。 
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \    / \
#        7    2  5   1
# 
#
# 返回: 
#
# [
#   [5,4,11,2],
#   [5,8,4,5]
# ]
# 
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.vcur_list = x
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

    def pathSum0(self, root, sum):
        # 深搜，维护一个数组，这个数组包含根节点到尾节点的路径，如果该路径和正好等于sum, 则将该路径加入到总数组中
        res, temp = [], []
        self.f(root, sum, res, temp)
        return res

    def f(self, root, sum, L, temp):
        if not root:
            return
        temp.append(root.vcur_list)
        if root.left is None and root.right is None and sum == root.vcur_list:
            L.append(temp.copy())  # 这里是重点,append的对象必须是temp的拷贝而不是temp本身这个引用。
            # 牵涉到的问题是可变对象如列表，字典等是引用赋值，而不可变对象如整数，字符串，元组等是拷贝赋值，即增加新的内存。
            # 可以用切片 root = root[:]
        else:
            self.f(root.left, sum - root.vcur_list, L, temp)
            self.f(root.right, sum - root.vcur_list, L, temp)
        temp.pop()

    """
    执行用时 :88 ms, 在所有 Python3 提交中击败了35.74%的用户
    内存消耗 :18.8 MB, 在所有 Python3 提交中击败了13.77%的用户
    """

    def pathSum_dfs(self, root, Sum):
        res = []
        if not root:
            return []

        def dfs(root, cur_list):
            if root.left:
                dfs(root.left, cur_list + [root.left.item])
            if root.right:
                dfs(root.right, cur_list + [root.right.item])
            if not root.right and not root.left:
                if sum(cur_list) == Sum:
                    res.append(cur_list)

        dfs(root, [root.item])
        return res

    # 非递归
    def pathSum1(self, root, sum):
        res = list()
        st = list()
        while st or root:
            while root:
                st.append(root)
                sum -= root.vcur_list
                if root.left:
                    root = root.left
                else:
                    root = root.right
            if sum == 0 and not st[-1].right and not st[-1].left:
                res.append([elem.vcur_list for elem in st])
            root = st.pop()
            sum += root.vcur_list
            if st and st[-1].left is root:
                root = st[-1].right
            else:
                root = None
        return res

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.auxPathSum(root, sum, [], res)
        return res

    def auxPathSum(self, root, sum, cur_list, cur_lists):
        if not root:
            return
        sum -= root.item
        if sum == 0 and not root.left and not root.right:
            cur_lists.append(cur_list + [root.item])
            return
        if root.left:
            self.auxPathSum(root.left, sum, cur_list + [root.item], cur_lists)
        if root.right:
            self.auxPathSum(root.right, sum, cur_list + [root.item], cur_lists)


t = Solution()
for i in range(7):
    t.add(i)
print('遍历:', t.pathSum(t.root, 7))
print('dfs遍历:', t.pathSum_dfs(t.root, 7))
print('dfs遍历:', t.pathSum1(t.root, 7))
