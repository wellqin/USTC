# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        重复元素
Description :   
Author :          wellqin
date:             2019/8/28
Change Activity:  2019/8/28
-------------------------------------------------
"""
from collections import Counter
print([str(k) + ':'+ str(v) for k,v in dict(Counter({2: 3, 1: 1, 3: 1, 4: 1})).items() if v >1])


a = [29,36,57,12,79,43,23,56,28,11,14,15,16,37,24,35,17,24,33,15,39,46,52,13]
b = dict(Counter(a))
print('a = {}, b = {}'.format(a, b))
print ([key for key,value in b.items()if value > 1])  # 只展示重复元素
print ({key:value for key,value in b.items()if value > 1})  # 展现重复元素和重复次数

"""
解题思路：
1.直接对数组排序然后顺序遍历:时间复杂度 O(nlogn)

2.顺序扫描数组，利用哈希表记录是否出现过: 时间复杂度 O(n) 空间复杂度 O(n)

3.顺序扫描数组，在数组对应位置i上看数字是否为i： 
    若是，则继续扫描下一个
    若不是，记数字为m，比较i与m位置的数字：
    若相等，则找到重复数字
    若不相等，则交换i与m，m位置上数字已经确定，继续以上操作
    时间复杂度:O(n) 空间复杂度 O(1)

"""

class Solution:
    def _init_(self):
        pass
    # 防止无效输入
    def valid_check(self, a):
        if len(a) == 0:
            return False
        for i in range(len(a)):
            if a[i] < 0 or a[i] > len(a) - 1:
                return False
        return True

    def Method_1(self, a):
        if valid_check(a):
            a = sorted(a)
            for i in range(len(a) - 1):
                if a[i] == a[i + 1]:
                    return a[i]
        else:
            return False


    def Method_2(self, a):
        if valid_check(a):
            num_array = np.zeros(len(a))
            for i in range(len(a)):
                if num_array[a[i]] == 0:
                    num_array[a[i]] += 1
                else:
                    return a[i]
        else: return False

    def Method_3(self, a):
        if valid_check(a):
            for i in range(len(a)):
                while a[i] != i:
                    if a[a[i]] == a[i]:
                        return a[i]
                    else:
                        a[a[i]], a[i] = a[i], a[a[i]]
        else:
            return False
