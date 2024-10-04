# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.WhatsObject
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.1、python中的变量是什么？
python和java中的变量本质不一样，java中的变量声明首先要声明变量类型（int|string），虚拟机就会在内存中申请空间，空间的大小和类型相关。
java中的变量就像一个有大小的盒子一样。

然而python中的变量与java不一样，python的变量实质上是一个指针。
a = "cdas" # python变量
# 上面是 a指向cdas存储的地址
"""
import copy

# 先生成对象，然后指向地址位置
a = "cdas"
print(id(a))  # 1790479789728


a = [1, 2, 3, 4]
b = a
b.append(5)
print(a)  # [1, 2, 3, 4, 5],b上添加了5,此时a也变了，可见二者指向同一片物理区域
print(a is b)  # True 即二者为同一个对象

c = [1, 2, 3, 4]
d = c.copy()
# d = copy.deepcopy(c)  # [1, 2, 3, 4]
d.append(5)
print(c)  # [1, 2, 3, 4]
print(d)  # [1, 2, 3, 4, 5]
print(c is d)  # Falses
