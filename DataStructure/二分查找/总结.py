# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        总结
Description :   
Author :          wellqin
date:             2020/1/24
Change Activity:  2020/1/24
-------------------------------------------------
"""
"""
我周围的人几乎都认为二分查找很简单，但事实真的如此吗？二分查找真的很简单吗？并不简单。看看 Knuth 大佬（发明 KMP 算法的那位）怎么说的：
Although the basic idea of binary search is comparatively straightforward, the details can be surprisingly tricky...
这句话可以这样理解：思路很简单，细节是魔鬼。

本文就来探究几个最常用的二分查找场景：寻找一个数、寻找左侧边界、寻找右侧边界。
而且，我们就是要深入细节，比如while循环中的不等号是否应该带等号，mid 是否应该加一等等。分析这些细节的差异以及出现这些差异的原因，
保证你能灵活准确地写出正确的二分查找算法。
"""


# 一、二分查找的框架： 寻找一个数（基本的二分搜索）
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    # 特殊判定
    if left == right or nums[right] < target: return -1
    if nums[left] == target or nums[right] == target:
        return True

    while left <= right:
        # 无符号位运算符的优先级较低，先括起来
        # mid = (left + right) / 2;
        # 在 left 和 right 很大的时候，会出现溢出的情况，从而导致数组访问出错。改进一般的做法是这样的：将加法变成减法。
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1
    # return left if nums[left] == target else -1


nums = [1, 2, 3, 4, 5]
#print(binarySearch(nums, 1))

"""
1. 为什么 while 循环的条件中是 <=，而不是 < ？ 
while(left <= right)的终止条件是 left == right + 1，写成区间的形式就是 [right + 1, right]，
或者带个具体的下标数字进去 [3, 2]，可见这时候搜索区间为空，因为没有数字既大于等于 3 又小于等于 2 的吧。
所以这时候 while 循环终止是正确的，直接返回 -1 即可。

while(left < right)的终止条件是 left == right，写成区间的形式就是 [right, right]，
或者带个具体的下标数字进去 [2, 2]，这时候搜索区间非空，还有一个数 2，但此时 while 循环终止了。
也就是说这区间 [2, 2] 被漏掉了，索引2没有被搜索，如果这时候直接返回 -1 就可能出现错误。

while(left < right)的补救措施： return nums[left] == target if left else -1 而不是原来的return -1
                              return left if nums[left] == target else -1  返回下标
"""

"""
2. 为什么 left = mid + 1，right = mid - 1？
因为 mid 已经搜索过，应该从搜索区间中去除。
"""

"""
# 3. 此算法有什么缺陷？  ======>  就是无法处理重复元素
"""

# 二、寻找左侧边界的二分搜索
# nums = [1,2,2,2,3]，target = 2，此算法返回的索引是 2，没错。但是如果我想得到 target 的左侧边界，
# 即索引 1，或者我想得到 target 的右侧边界，即索引 3，这样的话此算法是无法处理的。

def binarySearchLeft(numsleft, targetLsft):
    left = 0
    right = len(numsleft)  # Attention
    while left < right:    # Attention
        mid = left + ((right - left) >> 1)
        if nums[mid] == targetLsft:
            right = mid
        elif nums[mid] < targetLsft:
            left = mid + 1
        elif nums[mid] > targetLsft:
            right = mid
    return left

numsleft = [1,2,2,2,3,3,3]
print(binarySearchLeft(numsleft, 3))

"""
1. 为什么 while(left < right) 而不是 <= ?
答：用相同的方法分析，因为初始化 right = nums.length 而不是 nums.length - 1 。因此每次循环的「搜索区间」是 [left, right) 左闭右开。
while(left < right) 终止的条件是 left == right，此时搜索区间 [left, left) 恰巧为空，所以可以正确终止。


2. 为什么没有返回 -1 的操作？如果 nums 中不存在 target 这个值，怎么办？
"""