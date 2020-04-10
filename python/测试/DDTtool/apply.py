# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        apply
Description :   
Author :          wellqin
date:             2020/2/9
Change Activity:  2020/2/9
-------------------------------------------------
"""
# DDT基础使用（一）：传递基础数据类型
# 导入ddt库下所有内容
import unittest
from ddt import *


# 在测试类前必须首先声明使用 ddt
@ddt
class imoocTest(unittest.TestCase):

    # int
    @data(1, 2, 3, 4)
    def test_int(self, i):
        print("test_int：", i)

    # str
    @data("1", "2", "3")
    def test_str(self, str):
        print("test_str：", str)