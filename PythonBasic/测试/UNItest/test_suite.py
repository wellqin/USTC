# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test_suite.py
Description :   
Author :          wellqin
date:             2020/2/8
Change Activity:  2020/2/8
-------------------------------------------------
"""
import unittest


"""
按照上面的测试方法，我们无法控制用例执行的顺序，这样显然是不合理的，因为在一些测试过程中，我们肯定需要控制先测试某些用例，
再测试某些用例，这些用例有先后的因果关系。在这里，我们就需要用到TestSuite。我们添加到TestSuite中的case是会按照添加的顺序执行的。

还有一个问题是，我们现在只有一个测试文件，我们直接执行该文件即可，
但如果有多个测试文件，怎么进行组织，总不能一个个文件执行吧，答案也在TestSuite中。
"""

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     tests = [TestFunc("test_square"), TestFunc("test_lower_str"), TestFunc("test_multi")]
#     suite.addTests(tests)
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

"""
# 这样，用例执行的顺序就是按照我们添加进去的顺序来执行的了。
# 上面使用的是TestSuite的addTests()方法，并直接传入TestCase列表，也有一些其他的方法可以向TestSuite中添加用例

# 直接用addTest方法添加单个TestCase
suite.addTest(TestMathFunc("test_multi"))


# 使用loadTestFromName,传入模块名.TestCase名，下面俩方法效果相同
suite.addTests(unittest.TestLoader().loadTestsFromName('our_testcase.TestFunc'))
suite.addTests(unittest.TestLoader().loadTestsFromNames(['our_testcase.TestFunc']))


# loadTestsFromTestCase()，传入TestCase
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFunc))

用TestLoader的方法是无法对case进行排序的，同时，suite中也可以套suite。
"""
# 用例组织好了，但是结果只能输出到控制台，这样没办法查看之前的执行记录，我们想将结果输出到文件


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestFunc("test_square"), TestFunc("test_lower_str"), TestFunc("test_multi")]
    suite.addTests(tests)

    with open('UnitestTextReport.txt', 'a') as f:   # 在当前目录下生成UnitestTextReport.txt存放测试结果
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)


# 在之前的测试中，可能会存在这样的问题：如果要在测试之前准备环境，测试完成之后做一些清理怎么办？这里需要用到的是setUp()和tearDown()。
# 修改our_testcase.py
