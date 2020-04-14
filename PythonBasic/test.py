# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        test
Description :   
Author :          wellqin
date:             2019/7/17
Change Activity:  2019/7/17
-------------------------------------------------
"""

min([1,-2,3,-4,5])                        #-4
min([1,-2,3,-4,5],key=abs)                # 按照绝对值的大小，返回此序列最小值 1
min(1,2,-5,6,-3,key=lambda x:abs(x))      # 可以设置很多参数比较大小
ls=[('spring',100),('summer',18),('winter',500)]
def func(x):
    return x[1]
print(min(ls,key=func))              #('summer',18)


dic = {'a': 3, 'b': 2, 'c': 1}
def func1(x):
    return dic[x]
print(min(dic,key=func1))          #c
# x为dic的key，lambda的返回值（即dic的值进行比较）返回最小的值对应的键
dic = {'a':3,'b':2,'c':1}
print(min(dic,key=lambda x:dic[x]))
