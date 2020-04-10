# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        遍历文件夹,也递归了子目录
Description :   
Author :          wellqin
date:             2019/7/27
Change Activity:  2019/7/27
-------------------------------------------------
"""

"""
os.walk() 方法用于通过在目录树种游走输出在目录中的文件名，向上或者向下。
使用 os.walk .这个方法返回的是一个三元tupple(dirpath, dirnames, filenames),
其中第一个为起始路径，
第二个为起始路径下的文件夹,
第三个是起始路径下的文件.

dirpath是一个string，代表目录的路径,
dirnames是一个list，包含了dirpath下所有子目录的名字,
filenames是一个list，包含了非目录文件的名字.这些名字不包含路径信息,如果需要得到全路径,需要使用 os.path.join(dirpath, name).
"""

# coding:utf-8
import os

def get_files(path, rule=".py"):
    all = []
    for dirpath, dirnames, filenames in os.walk(path):   # os.walk是获取所有的目录
        # print(dirpath)    # 所有的文件夹路径
        # print(dirnames)   # 遍历打印所有的文件夹名称
        # print(filenames)  # 遍历打印所有的文件名
        for f in filenames:
            filename = os.path.join(dirpath, f)
            if filename.endswith(rule):  # 判断是否是"xxx"结尾
                all.append(filename)
    return all

if __name__ == "__main__":
    b = get_files(r"/")
    for i in b:
        print(i)

    # get_files(r"C:\Users\QWust\Desktop\GitHub")