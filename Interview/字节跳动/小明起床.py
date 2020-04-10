# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        小明起床
Description :   
Author :          wellqin
date:             2019/8/11
Change Activity:  2019/8/11
-------------------------------------------------
"""
N = int(input())

li = []                        # 起床鬧鐘時間
for i in range(N):
    b = list(map(int, input().split()))
    li.append(b)

X = int(input())               # 到達教室
AB = list(map(int, input().split()))

value = AB[0]*60 + AB[1]


# print(N, li, X, AB)


res = []
for i in li:
    value_i = i[0] * 60 + i[1]  + X
    res.append(value_i)
# print(res)


def find_close(arr, target):

    low = 0
    high = len(arr) - 1
    idx = -1

    while low <= high:
        mid = int((low + high) / 2)
        if target == arr[mid] or mid == low:
            idx = mid
            break
        elif target > arr[mid]:
            low = mid
        elif target < arr[mid]:
            high = mid

    if idx + 1 < len(arr) and abs(target - arr[idx]) > abs(target - arr[idx + 1]):
        idx += 1
    return idx



idx = find_close(res, value)
print(li[idx][0], li[idx][1])

# idx1 = sortList(res, value)
# print(li[idx1][0], li[idx1][1])
# def sortList(arr, target):
#     res.sort()
#     for i in range(len(res)):
#         if res[i] <= target:
#             return i

for i in reversed([1,3,4,5]):
    print(i)






