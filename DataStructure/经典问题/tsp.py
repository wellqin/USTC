# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        tsp
Description :   
Author :          wellqin
date:             2019/7/19
Change Activity:  2019/7/19
-------------------------------------------------
"""
"""
tsp问题-遍历算法/随机算法
旅行商问题，即TSP问题（Traveling Salesman Problem）又译为旅行推销员问题、货郎担问题，是数学领域中著名问题之一。
假设有一个旅行商人要拜访n个城市，他必须选择所要走的路径，路径的限制是每个城市只能拜访一次，而且最后要回到原来出发的城市。
路径的选择目标是要求得的路径路程为所有路径之中的最小值。


"""

# TSP旅行商问题：若干个城市，任意两个城市之间距离确定，要求一旅行商从某城市
# 出发必须经过每一个城市且只能在每个城市逗留一次，最后回到原出发城市，试
# 确定一条最短路径使旅行费用最少

# 遍历算法

# 给定某条路径，计算它的成本

def distcal(path, dist):
    # 计算路径成本（路径，距离）
    sum_dist = 0  # 总成本
    for j in range(0, len(path) - 1):
        di = dist[int(path[j]) - 1][int(path[j + 1]) - 1]  # 查找第j和j+1个城市之间的成本
        sum_dist = sum_dist + di  # 累加
    di = dist[int(path[len(path) - 1]) - 1][path[0] - 1]  # 最后一个城市回到初始城市的成本
    sum_dist = sum_dist + di
    return sum_dist  # 返回路径的成本


# 递归,构造所有可能路径
def perm(l):  # 构造路径（城市列表）
    if (len(l)) <= 1:  # 只有一个城市，选择这个城市
        return [l]
    r = []  # 空列表
    for i in range(len(l)):  # 对每个城市，构建不包括这个城市的所有可能序列
        s = l[:i] + l[i + 1:]  # 去除当前城市的列表
        p = perm(s)  # 调用自身，构造不包含这个城市的序列
        for x in p:
            r.append(l[i:i + 1] + x)  # 将序列和该城市合并，得到完整的序列
    return r


if __name__ == '__main__':
    city = [1, 2, 3, 4, 5]

    dist = ((0, 1, 3, 4, 5),
            (1, 0, 1, 2, 3),
            (3, 1, 0, 1, 2),
            (4, 2, 1, 0, 1),
            (5, 3, 2, 1, 0))

    for i in range(0, 5):
        print(dist[i][:])

    print('=============')

    allpath = perm(city)  # 调用路径产生函数，产生所有可能的路径

    optimal = 1000000  # 初始化最优路径的总成本和索引号

    index = 1

    for i in range(0, len(allpath)):
        pd = distcal(allpath[i], dist)
        if pd < optimal:  # 比较是否总成本更低，如果是替换最优解
            optimal = pd
            index = i
        # print(pd)

    print(optimal)
    print(allpath[index])



import random
# 随机算法
# 给定某条路径，计算它的成本
def distcal(path, dist):
    # 计算路径成本（路径，距离）
    sum_dist = 0  # 总成本
    for j in range(0, len(path) - 1):
        di = dist[int(path[j]) - 1][int(path[j + 1]) - 1]  # 查找第j和j+1个城市之间的成本
        sum_dist = sum_dist + di  # 累加
    di = dist[int(path[len(path) - 1]) - 1][path[0] - 1]  # 最后一个城市回到初始城市的成本
    sum_dist = sum_dist + di
    return sum_dist  # 返回路径的成本

# 构造随机路径
def randompath(inc):  # Inc城市列表
    allcity = inc[:]  # 城市列表
    path = []  # 路径
    loop = True
    while loop:
        if 1 == len(allcity):  # 如果是最后一个城市
            tmp = random.choice(allcity)
            path.append(tmp)
            loop = False  # 结束
        else:  # 如果不是最后一个城市
            tmp = random.choice(allcity)  # 在城市列表中随机选择一个城市
            path.append(tmp)  # 添加路径
            allcity.remove(tmp)  # 在城市列表中移除该城市
    return path

if __name__ == '__main__':
    city = [1, 2, 3, 4, 5]

    dist = ((0, 1, 3, 4, 5),
            (1, 0, 1, 2, 3),
            (3, 1, 0, 1, 2),
            (4, 2, 1, 0, 1),
            (5, 3, 2, 1, 0))

    for i in range(0, 5):
        print(dist[i][:])

    print('=============')

    num = 10  # 随机产生10条路径

    optimal = 1000000  # 初始化最优路径的总成本和索引号

    for i in range(0, num):
        pd = distcal(randompath(city), dist)
        if pd < optimal:  # 比较是否总成本更低，如果是替换最优解
            optimal = pd
        print(pd)

    print(optimal)