# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.isinstance
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------

isinstance和type的区别

判断类型：为什么更推荐用isinstance而不是type？
因为如果判断某个对象的类型的话，用isinstance会根据树的形状去搜索，从叶子搜索到跟就可以判断是否是相同类型，就算是不同对象可能是相同类型，
然而type是同种类型，但不同对象。
"""


class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True

print(type(b) is B)  # True   is与==的区别，==判断值是否相等，is判断是不是同一个对象（id（b）地址是否一样）
print(type(b) is A)  # False
print(type(b), A)  # <class '__main__.B'> <class '__main__.A'>

# type 判断是否是同一个对象
# isinstance 可进一步判断是否有继承关系的对象（对象间存在继承关系也算在内）
# isinstance 会去找继承链




