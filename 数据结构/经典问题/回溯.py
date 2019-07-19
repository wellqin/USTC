# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        回溯
Description :   
Author :          wellqin
date:             2019/7/19
Change Activity:  2019/7/19
-------------------------------------------------
"""

'''求集合{1, 2, 3, 4}的所有子集'''  # [[1, 3], [1], [2, 4], [2], [3], [4], []]
"""
n = 4
# a = ['a','b','c','d']
a = [1, 2, 3, 4]
x = []  # 一个解（n元0-1数组）
X = []  # 一组解


# 冲突检测：无
def conflict(k):
    global n, x, X, a

    return False  # 无冲突


# 一个例子
# 冲突检测：奇偶性相同，且和小于8的子集
def conflict2(k):
    global n, x, X, a

    if k == 0:
        return False

    # 根据部分解，构造部分集
    s = [y[0] for y in filter(lambda s: s[1] != 0, zip(a[:k + 1], x[:k + 1]))]
    if len(s) == 0:
        return False
    if 0 < sum(map(lambda y: y % 2, s)) < len(s) or sum(s) >= 8:  # 只比较 x[k] 与 x[k-1] 奇偶是否相间
        return True

    return False  # 无冲突


# 子集树递归模板
def subsets(k):  # 到达第k个元素
    global n, x, X

    if k >= n:  # 超出最尾的元素
        # print(x)
        X.append(x[:])  # 保存（一个解）
    else:
        for i in [1, 0]:  # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
            x.append(i)
            if not conflict2(k):  # 剪枝
                subsets(k + 1)
            x.pop()  # 回溯


# 根据一个解x，构造一个子集
def get_a_subset(x):
    global a

    return [y[0] for y in filter(lambda s: s[1] != 0, zip(a, x))]


# 根据一组解X, 构造一组子集
def get_all_subset(X):
    return [get_a_subset(x) for x in X]


# 测试
subsets(0)
print(X[2])
print(get_a_subset(X[2]))
print(get_all_subset(X))
"""


'''求[1,2,3,4]的全排列'''

"""
n = 4
x = [1, 2, 3, 4]  # 一个解
X = []  # 一组解


# 冲突检测：无
def conflict(k):
    global n, x, X

    return False  # 无冲突


# 一个例子
# 冲突检测：元素奇偶相间的排列
def conflict2(k):
    global n, x, X

    if k == 0:  # 第一个元素，肯定无冲突
        return False

    if x[k - 1] % 2 == x[k] % 2:  # 只比较 x[k] 与 x[k-1] 奇偶是否相同
        return True

    return False  # 无冲突


# 排列树递归模板
def backkrak(k):  # 到达第k个位置
    global n, x, X

    if k >= n:  # 超出最尾的位置
        print(x)
        # X.append(x[:]) # 注意x[:]
    else:
        for i in range(k, n):  # 遍历后面第 k~n-1 的位置
            x[k], x[i] = x[i], x[k]
            if not conflict2(k):  # 剪枝
                backkrak(k + 1)
            x[i], x[k] = x[k], x[i]  # 回溯


# 测试
backkrak(0)
"""

'''
8皇后问题
'''

"""
n = 8
x = []  # 一个解（n元数组）
X = []  # 一组解


# 冲突检测：判断 x[k] 是否与前 x[0~k-1] 冲突
def conflict(k):
    global x

    for i in range(k):  # 遍历前 x[0~k-1]
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):  # 判断是否与 x[k] 冲突
            return True
    return False


# 套用子集树模板
def queens(k):  # 到达第k行
    global n, x, X

    if k >= n:  # 超出最底行
        print(x)
        X.append(x[:])  # 保存（一个解），注意x[:]
    else:
        for i in range(n):  # 遍历第 0~n-1 列（即n个状态）
            x.append(i)  # 皇后置于第i列，入栈
            if not conflict(k):  # 剪枝
                queens(k + 1)
            x.pop()  # 回溯，出栈






# 解的可视化（根据一个解x，复原棋盘。'X'表示皇后）
def show(x):
    global n

    for i in range(n):
        print('. ' * (x[i]) + 'X ' + '. ' * (n - x[i] - 1))


# 测试
queens(0)  # 从第0行开始

print(X[-1], '\n')
show(X[-1])
"""


"""
# 迷宫（1是墙，0是通路）
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

m, n = 8, 10  # 8行，10列
entry = (1, 0)  # 迷宫入口
path = [entry]  # 一个解（路径）
paths = []  # 一组解

# 移动的方向（顺时针8个：N, EN, E, ES, S, WS, W, WN）
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


# 冲突检测
def conflict(nx, ny):
    global m, n, maze

    # 是否在迷宫中，以及是否可通行
    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
        return False

    return True


# 套用子集树模板
def walk(x, y):  # 到达(x,y)格子
    global entry, m, n, maze, path, paths, directions

    if (x, y) != entry and (x % (m - 1) == 0 or y % (n - 1) == 0):  # 出口
        # print(path)
        paths.append(path[:])  # 直接保存，未做最优化
    else:
        for d in directions:  # 遍历8个方向(亦即8个状态)
            nx, ny = x + d[0], y + d[1]
            path.append((nx, ny))  # 保存，新坐标入栈
            if not conflict(nx, ny):  # 剪枝
                maze[nx][ny] = 2  # 标记，已访问（奇怪，此两句只能放在if区块内！）
                walk(nx, ny)
                maze[nx][ny] = 0  # 回溯，恢复
            path.pop()  # 回溯，出栈


# 解的可视化（根据一个解x，复原迷宫路径，'2'表示通路）
def show(path):
    global maze

    import pprint, copy

    maze2 = copy.deepcopy(maze)

    for p in path:
        maze2[p[0]][p[1]] = 2  # 通路

    pprint.pprint(maze)  # 原迷宫
    print()
    pprint.pprint(maze2)  # 带通路的迷宫


# 测试
walk(1, 0)
print(paths[-1], '\n')  # 看看最后一条路径
show(paths[-1])
"""


# 无重复元素全排列问题
class Solution(object):
    def backtrack(self,nums):
        if not nums:
            return []
        res = []

        # res用来存储所有的返回所有排列，templist用来生成每个排列
        def helper(res, templist, nums):
            if (len(templist) == len(nums)):
                res.append(templist[:])
            else:
                for i in nums:
                    if i in templist:  # 如果在当前排列中已经有i了，就continue，相当于分支限界，即不对当前节点子树搜寻了
                        continue
                    templist.append(i)
                    helper(res, templist, nums)
                    templist.pop()  # 把结尾的元素用nums中的下一个值替换掉，遍历下一颗子树

        helper(res, [], nums)
        return res

nums = [1,2,3]
print(Solution().backtrack(nums))


# '''用子集树实现全排列'''
#
#
# a = [1,2,3]
# n = len(a)
#
# x = [0] * n  # 一个解（n元0-1数组）
# X = []  # 一组解
#
#
# # 冲突检测：无
# def conflict(k):
#     global n, x, X, a
#     return False  # 无冲突
#
#
# # 用子集树模板实现全排列
# def backtrack(k):  # 到达第k个元素
#     global n, a, x, X
#
#     if k >= n:  # 超出最尾的元素
#         X.append(x[:]) # 保存（一个解）
#     else:
#         for i in set(a) - set(x[:k]):  # 遍历，剩下的未排的所有元素看作元素x[k-1]的状态空间
#             x[k] = i
#             if not conflict(k):  # 剪枝
#                 backtrack(k + 1)
#     return X
#
#
# # 测试
# print(backtrack(0))  # 从x[0]开始


