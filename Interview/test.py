# li = list(map(int, input().split()))
# lit = list(map(int, input().split()))
# print(li)
# print(lit)

li = [9, 4]
lit = [2, 2, 1, 8]

# 第一题试一下
# li = list(map(int, input().split()))
# lit = list(map(int, input().split()))
m = li[0]  # 能力值
n = li[1]  # 怪物数量

money = 0
res = 0
nums = sorted(lit)
for i in nums:
    if m > nums[-1]:
        print(n - 1)
        break
    if m >= i:
        money += 1
        res = max(res, money)
    else:
        while m < i:
            if money > 0:
                money -= 1
                m += 1
            else:
                break
        if m >= i:
            money += 1
            res = max(res, money)
        else:
            break
print(res)


class Solution(object):

    def minPathSum(self, root):
        self.global_max = root.val if root else 0
        self.find(root)
        return self.global_max

    def find(self, node):
        if not node:
            return 0
        left = self.find(node.left)
        right = self.find(node.right)
        self.global_max = min(left + right + node.val, self.global_max)
        return min(left, right) + node.val


n = int(input())
lit = list(map(int, input().split()))
li = []
for i in range(n - 1):
    b = list(map(int, input().split()))
    li.append(b)

print(n - 1)
