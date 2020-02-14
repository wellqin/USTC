# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        introduction
Description :   
Author :          wellqin
date:             2020/2/8
Change Activity:  2020/2/8
-------------------------------------------------
"""
# python中很常用的单元测试框架unitest

"""
unitest主要功能模块介绍
    unitest主要包含TestCase、TestSuite、TestLoader、TextTestRunner、TextTestResult这几个功能模块。
        TestCase：一个TestCase实例就是一个测试用例，一个测试用例就是一个完整的测试流程，
                 包括测试前环境的搭建，测试代码的执行，以及测试后环境的还原或者销毁。元测试的本质也就在这里，
                 一个测试用例是一个完整的测试单元，可以对某一具体问题进行检查验证。
        TestSuite：多个测试用例集合在一起就是TestSuite，TestSuite也可以嵌套TestSuite。
        TestLoader：TestLoader的作用是将Testcase加载到TestSuite中。
        TextTestRunner：TextTestRunner是用来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。
        TextTestResult：TextTestResult用来保存测试结果，其中包括运行了多少测试用例，成功了多少，失败了多少等信息。

整个流程为：写好TestCase，然后由TestLoader加载TestCase到TestSuite，
然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中
"""