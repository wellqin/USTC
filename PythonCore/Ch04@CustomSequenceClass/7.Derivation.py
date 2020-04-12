# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        7.Derivation
Description :   
Author :          wellqin
date:             2020/4/12
Change Activity:  2020/4/12
-------------------------------------------------

1.7、列表推导式、生成器表达式、字典推导式
当在应用的时候，逻辑简单的时候，能用推导式就直接用推导式，推导式的效率以及灵活性都很强。
"""

# 列表生成式（列表推导式）
# 提取1-20之间的奇数
odd_list = []
for i in range(21):
    if i % 2 == 1:
        odd_list.append(i)
print(odd_list)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
add_list = [i for i in range(21) if i % 2 == 1]
print(add_list)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# 逻辑复杂的时候
def handle_num(item):
    return item * item


dd_list = [handle_num(i) for i in range(21) if i % 2 == 1]
dd_list1 = [i**2 for i in range(21) if i % 2 == 1]
print(dd_list)  # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
print(dd_list1)  # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
# **************列表生成式效率高于列表操作************

# 生成器表达式: 注意小括号就是生成器
add_gen = (i for i in range(21) if i % 2 == 1)
print(type(add_gen))  # <class 'generator'>
print(add_gen)  # <generator object <genexpr> at 0x000002393740CBC8>

# for m in add_gen:
#     print(m, end=' ')  # 1 3 5 7 9 11 13 15 17 19 生成器是可迭代对象
# print()
# 注意：这里for循环迭代生成器，里面元素被迭代完后，生成器为空，下面的list转换就是[]

add_gen = list(add_gen)  # 生成器类型转化为列表类型：使用list强制转化就行
print("add_gen", add_gen)  # []? 上面for循环迭代后为空，没有for循环则正常输出
print(type(add_gen))  # <class 'list'>

# 字典推导式
my_dict = {"li": 1, "li2": 2, "li3": 3}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)  # {1: 'li', 2: 'li2', 3: 'li3'}

# 集合推导式
# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# my_set = set(my_dict.keys())
my_set = {key for key, value in my_dict.items()}  # 灵活性更高
print(type(my_set))  # <class 'set'>
print(my_set)  # {'li2', 'li3', 'li'}
