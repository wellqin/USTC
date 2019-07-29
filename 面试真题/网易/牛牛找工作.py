# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        牛牛找工作
Description :   
Author :          wellqin
date:             2019/7/29
Change Activity:  2019/7/29
-------------------------------------------------
"""

"""
题目描述
为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力值的情况下，
牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，牛牛依然使用自己的标准来帮助小伙伴们。
牛牛的小伙伴太多了，于是他只好把这个任务交给了你。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。
示例1
输入

3 3               # 工作的数量N  和小伙伴的数量M
1 100             # 难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
10 1000           # 难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
1000000000 1001   # 难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
9 10 1000000000   # 分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。

输出
100 
1000 
1001
"""

"""
raw_input().strip().split()效果
raw_input()          #' insert 0 5     '
raw_input().strip()  #'insert 0 5'
raw_input().strip().strip()  #['insert', '0', '5']
"""
# 分析，类似于二分查找问题，给定难度值列表，将能力值往里面插入，找到最接近的返回，

import sys
import bisect

task = {}
# lines = sys.stdin.readlines()
with open('C:\\Users\QWust\Desktop\\abc.txt', encoding='utf-8') as f:
    lines = f.readlines()
n, m = map(int, lines[0].strip().split())  # 由于有空行，这句可以不写  ['3', '3']
for line in lines[1:-1]:
    if not line.strip().split():  # 存在空行，你能信...
        continue
    a, b = map(int, line.strip().split())    # ['1000000000', '1001']--> map 后为 1000000000 1001 数字
    task[a] = max(task.get(a, 0), b)
arr = sorted(task.keys())
print(task)
print(arr)

for i in range(1, len(arr)):
    if task[arr[i]] < task[arr[i -1]]:
        task[arr[i]] = task[arr[i -1]]
print(task)
print(arr)



skills = map(int, lines[-1].strip().split())
for skill in skills:
    if skill in task:
        print(task[skill])
    else:
        ind = bisect.bisect(arr, skill)
        if ind == 0:
            print(0)  # 没能力做任何工作
        else:
            print(task[arr[ind -1]])