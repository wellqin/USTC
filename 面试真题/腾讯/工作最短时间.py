# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        工作最短时间
Description :   
Author :          wellqin
date:             2019/9/20
Change Activity:  2019/9/20
-------------------------------------------------
"""

# n = int(input())
# li = []
# for i in range(n):
#     li.append(list(map(int, input().split())))

n = 3
li = [[1, 8], [2, 5], [1, 2]]
print(sorted(li, key=lambda x: x[1])) # [[1, 2], [2, 5], [1, 8]]
if not n or not li:
    print('')


sortlist = li

first = sortlist[0][1]
end = sortlist[-1][1]

for i in range(n):
    while sortlist[i][0] != 1:
        sortlist[i][0] -= 1
        sortlist.append([1, sortlist[i][1]])

nums = sorted(li, key=lambda x: x[1])  # [[1, 8], [1, 5], [1, 2], [1, 5]]
# print(nums)  # [[1, 2], [1, 5], [1, 5], [1, 8]]
min = 0

first = nums[0][1]
end = nums[-1][1]
print(first + end)














#
# count = []
# stime = []
# for i in li:
#     count.append(i[0])
#     stime.append(i[1])
# total = sum(count) // 2
# if total % 2 != 0:
#     print('')
#
# sums = []
# for i in range(n):
#     sums.append(count[i] * stime[i])  # [8,10,2]
# print(sum(sums) // total)
