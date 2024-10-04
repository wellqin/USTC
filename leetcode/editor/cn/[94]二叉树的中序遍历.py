#给定一个二叉树，返回它的中序遍历。
#
# 示例: 
#
# 输入: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
#输出: [1,3,2] 
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#

# Definition for a binary tree node.


class Node:
    def __init__(self, item):
        self.item = item
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

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res

    def traverse1(self, root):  # 层次遍历
        if root == None:
            return []
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.item)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def diedai(self,root):
        stack = []
        cur = root
        while cur:
            stack.append(root)
            cur = cur.left
        return stack



    def preorder(self,root):  # 先序遍历  中左右
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorderTraversal2(self, root):
        if not root:
            return []
        return [root.item] + self.inorderTraversal2(root.left) +  self.inorderTraversal2(root.right)

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if not root:
    #         return res
    #     if root.left:
    #         return res.extend(self.inorderTraversal(root.left))
    #     res.append(root.item)
    #     if root.right:
    #         return res.extend(self.inorderTraversal(root.right))
    #     return res
    #
    # def inorderTraversal1(self, root):
    #
    #     if root != None:
    #         self.inorderTraversal1(root.left)
    #         self.ret.append(root.item)
    #         self.inorderTraversal1(root.right)
    #
    #     return self.ret

    def inorderTraversal(self, root):  ## 前序遍历
        stack = []
        result = []
        curr = root
        while stack or curr:
            if curr:
                result.append(curr.item)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return result



    def inorder(self,root):  # 中序遍历 左中右
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self,root):  # 后序遍历  左右中
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result

    def postorderTraversal(self, root):  ## 前序遍历
        stack = []
        result = []
        curr = root
        while stack or curr:
            if curr:
                result.append(curr.item)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()
        return result[::-1]


t = Tree()
for i in range(7):
    t.add(i)
print('层序遍历:',t.traverse())
print('先序遍历:',t.preorder(t.root))
print('先序遍历:',t.inorderTraversal(t.root))
# print('先序遍历:',t.inorderTraversal1(t.root))
print('先序遍历:',t.inorderTraversal2(t.root))
print('中序遍历:',t.inorder(t.root))
print('后序遍历:',t.postorder(t.root))
print('postorderTraversal后序遍历:',t.postorderTraversal(t.root))
print("#############################")



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

    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    # 递归，瞬秒
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     res = []
    #     if not root:
    #         return res
    #     if root.left:
    #         return res.extend(self.inorderTraversal(root.left))
    #     res.append(root.val)
    #     if root.right:
    #         return res.extend(self.inorderTraversal(root.right))
    #     return res

    def inorderTraversal1(self, root):

        if root != None:
            self.inorderTraversal(root.left)
            self.ret.append(root.val)
            self.inorderTraversal(root.right)
        return self.ret

    def inorderTraversal2(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# tt = Solution()
# for i in range(10):
#     tt.add(i)
#
# # print('先序遍历:',t.inorderTraversal(t.root))
# print('先序遍历:',tt.inorderTraversal1(tt.root))
# print('先序遍历:',tt.inorderTraversal2(tt.root))





























        