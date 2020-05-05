"""
-------------------------------------------------
File Name:        mypak
Author :          wellqin
date:             2020/4/24
-------------------------------------------------
"""

# 此时想要跨目录导入文件/包函数
# 1.【绝对查找路径】-- 加入sys，设置查找路径变量
# import sys
#
# BASE_DIR = "C:\\Users\\QWust\\Desktop\\GitHub\\PythonBasic"
# sys.path.append(BASE_DIR)
#
# from PythonBasic.packageTest import mypake
#
# print("mypkg")
# print(mypake.mypake())
#
# """
# pkg, init
# mypkg
# this is mypake
# """


# 2.【相对查找路径】-- 一般从爷爷目录开始起步导入
# print("__file__", __file__)  # 获取当前文件的相对目录__file__
# # C:/Users/QWust/Desktop/GitHub/PythonBasic/packageTest/mypak.py  pycharm执行结果是绝对路径，在命令行中运行
# import os, sys
# base_dir = os.path.dirname(__file__)
# print(base_dir)  # C:/Users/QWust/Desktop/GitHub/PythonBasic/packageTest
# sys.path.append(base_dir)  # 动态实现


# 3.官方推荐：相对导入
from PythonBasic.importpackageTest import mypake

# print("mypkg")
# print(mypake.mypake())
