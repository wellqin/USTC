# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        均分列表
Description :   
Author :          wellqin
date:             2019/10/10
Change Activity:  2019/10/10
-------------------------------------------------
"""
import random

# def test_input():
#     arr = [-3000]
#     for i in range(1000):
#         n = random.randint(-10, 20)
#         if n < 0:
#             n -= 100
#         elif n > 0:
#             n += 100
#         else:
#             continue
#         arr.append(n)
#     return arr
# arr = test_input()
# arr = [1, 2, 3, 4, 10]
# 求和
# def sum(a):
#     s = 0
#     for i in a:
#         s += i
#     return s



# 分离数组
def split_array(arr):
    # 获取数组并排序
    a = list(arr)
    # a.sort()
    # 另一个数组

    b = list()
    # 以上a,b作为待返回的数组

    # 计算数组大小
    n = len(a)  # 1000

    # 求和
    smr = sum(a)

    # 和的一半,简称半和
    hs = smr / 2

    # 临时和
    s = 0

    # 从最大的数字开始遍历数组
    for i in range(-1, 0-n, -1):
        # 预判该数字加和结果

        ns = s + a[i]
        if ns > hs:
            # 如果超出半和则跳过
            continue
        else:
            # 如果未超过半和,则:
            # 1, 取该元素加和
            s += a[i]
            # 2, 从 a 中将元素转移到 b
            b.append(a[i])
            a.pop(i)
            # 如果最终和与半和之差,不够最小元素,则完成
            if abs(s - hs) <= a[-1]:
                break
    return [a, b]


if __name__ == '__main__':
    # 测试:
    # [1,2,3,4,5] -> [1,2,5] & [3,4]
    # arr = test_input()
    arr = [1, 2, 3, 4, 10]
    print(split_array(arr))
