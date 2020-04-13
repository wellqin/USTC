# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.FrozenSet
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.4、set和frozenset

set源码
set() -> new empty set object
set("a", "b") -> new not empty set object
set(iterable) -> new set object  注意这里的可迭代对象，所以str也可以，会被迭代拆开
"""

# set 集合  frozenset 不可变集合  【无序、不重复】
s = set("abcde")
s.add("u")
print(s)  # {'b', 'a', 'e', 'd', 'c', 'u'}
s.add("a")
print(s)  # {'b', 'a', 'e', 'd', 'c', 'u'}

s2 = frozenset("abcdef")  # frozenset 应用: 可以作为dict的key
print(s2)  # frozenset({'b', 'f', 'a', 'e', 'd', 'c'}) # 不能修改

# difference
anoth_set = set("cdefgh")
res = s.difference(anoth_set)
print(res)  # {'a', 'b', 'u'}

# 集合运算 交 并 差集
res = s - anoth_set  # {'a', 'b', 'u'}
res1 = s & anoth_set  # 交  {'d', 'e', 'c'}
res2 = s | anoth_set  # 并  {'a', 'g', 'f', 'd', 'u', 'c', 'b', 'e', 'h'}

# set性能高(hash)s
# 实现__contains__魔法函数就可以做if判断
if "a" in res:
    print(True)  # True

print(res.issubset(res2))  # 判断子集 True
