# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        翻转整数
Description :   
Author :          wellqin
date:             2019/8/22
Change Activity:  2019/8/22
-------------------------------------------------
"""

class Solution:
    def reverse(self, x):
        flag = 1 if x >= 0 else -1 # 用flag记录整数正负
        new_x = 0
        abs_x = abs(x)
        while abs_x:
            new_x = new_x*10 + abs_x%10
            abs_x //= 10 # 注意这里用的是取整除//而非/，不然就返回的是12.3（比如输入是123），正确返回结果应该是12
        new_x = flag*new_x
        return new_x if new_x < 2147483648 and new_x >= -2147483648 else 0

print(Solution().reverse(12345))