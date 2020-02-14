# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        our_testcase.py
Description :   
Author :          wellqin
date:             2020/2/8
Change Activity:  2020/2/8
-------------------------------------------------
# python单元测试用例设计
    正常值功能测试
    边界值（比如最大最小，最左最右值）
    异常值（比如 None，空值，非法值）
    逻辑功能测试（白盒）

"""
import unittest
from .test_func import *


class TestFunc(unittest.TestCase):
    """Test test_func.py"""

    def setUp(self):
        print("do something before testcase")

    @unittest.skip('do not run this case')  # 如果我们临时想要跳过某个case不执行，unitest也有相应的方法:  1、skip装饰器
    def test_add(self):
        """Test func add"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(1, 3))
        # 2、TestCase.skipTest()方法
        # self.skipTest("do not run this case")

    def test_multi(self):
        """Test func multi"""
        self.assertEqual(6, multi(2, 3))
        self.assertNotEqual(8, multi(3, 3))

    def test_lower_str(self):
        """Test func lower_str"""
        self.assertEqual("abc", lower_str("ABC"))
        self.assertNotEqual("Dce", lower_str("DCE"))

    def test_square(self):
        """Test func square"""
        self.assertEqual(17, square(4))  # 这里故意设计一个会出错的用例，测试4的平方等于17，实际上并不等于。
        self.assertNotEqual(35, square(6))

    def tearDownClass(self):
        print("do something after testcase")


if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)

"""
在unitest.main()中加上verbosity参数可以控制输出的错误报告的详细程序，
默认是1，如果设为0，则不输出每一用例的执行结果，即上面的第一行的执行结果内容。如果设为2，则输出详细的执行结果。
"""

"""
可以发现setUp()和tearDown()在每个case前后都执行了一次。
如果要在所有case执行之前和所有case执行之后准备和清理环境，我们可以使用setUpClass() 与 tearDownClass()
"""
