# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/12
Change Activity:  2019/7/12
-------------------------------------------------
"""


class ShortInputException(Exception):
    '''自定义的异常类'''
    def __init__(self, length, atleast):
        #super().__init__()
        self.length = length
        self.atleast = atleast
try:
    s = input('请输入 --> ')
    if len(s) < 3:
        # raise引发一个你定义的异常
        raise ShortInputException(len(s), 3)

except EOFError:
    print("你输入了一个结束标记EOF")
except ShortInputException as result:#x这个变量被绑定到了错误的实例
    print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
else:
    print('没有异常发生.')

