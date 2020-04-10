# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        均分数组
Description :   
Author :          wellqin
date:             2020/3/6
Change Activity:  2020/3/6
-------------------------------------------------
"""


def split_list(arrry):
    nums = list(arrry)  # # 列表排序，全给第一个列表
    nums.sort()

    nums_2 = []
    half_total = sum(nums) / 2
    s = 0  # 临时和
    for i in range(len(nums) - 1, -1, -1):  # 从数值最大的数开始遍历列表
        ns = s + nums[i]
        if ns > half_total:  # 如果超出半和则跳过
            continue
        else:
            s += nums[i]  # 如果未超过半和,取该元素加和
            nums_2.append(nums[i])  # 从one_list中将元素转移到two_list
            nums.pop(i)
            if abs(s - (sum(nums) / 2)) < nums[0]:  # 如果最终和与半和之差,不够最小元素,则完成
                break
    return nums, nums_2


# 测试:
# [1,2,3,4,5] -> [1,2,5] & [3,4]
arr = [1, 2, 3, 4, 5]
print(split_list(arr))

import itertools


def funcProduct(a, b):
    for c in itertools.permutations(b):
        for d in itertools.product(*[list(itertools.permutations(x)) for x in zip(a, c)]):
            yield zip(*d)


a = [1, 2, 3, 4]
b = [5, 6, 700, 800]
print(min(funcProduct(a, b), key=lambda x: abs(sum(x[0]) - sum(x[1]))))
