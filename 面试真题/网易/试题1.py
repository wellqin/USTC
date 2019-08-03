# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        试题1
Description :   
Author :          wellqin
date:             2019/8/3
Change Activity:  2019/8/3
-------------------------------------------------
"""


# 1、倒数第Q个排列

# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    result = list()
    for v in values:
        result.append(n + 1 - v)
    result = [str(x) for x in result]
    print((' '.join(result)))


# 2、圆环
# 排序后只考虑最后一个是否满足即可；
# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    # t = int(sys.stdin.readline().strip())
    t = 1
    for i in range(t):
        result.sort()
        if nums[-1] < nums[-2] + nums[-3]:
            print("YES")
        else:
            print("NO")

# 核心点在于先将result排序


# 3、奇偶交换
# 如果有奇偶，则直接排序；否则，直接输出


# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    result = list()
    for v in values:
        result.append(v)
    temp1 = [x for x in result if x % 2 == 0]
    temp2 = [x for x in result if x % 2 != 0]
    if temp1 != [] and temp2 != []:
        result.sort()
    result = [str(x) for x in result]
    print((' '.join(result)))