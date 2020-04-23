# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        Built-in type
Author :          wellqin
date:             2020/4/10
-------------------------------------------------
3.1、对象的三个特征：id type value
    身份：什么是身份呢？可以理解成对象在内存中的地址。（可以用id函数来查看对象的地址）
    类型：对象都是有类型的。（例如：int型，str型）
    值：value

3.2、类型：Python中有哪些类型

3.2.1、None类型（全局只有一个）：
    Python解释器运行的时候，Python会用None这个类型声明一个None的对象。
    （例如：变量a、b都被赋值一个None对象，然后会发现变量都指向一个None对象（ 地址可以看出 id(a) = id(b) ）


3.2.2、数值类型：
    int类型、float类型、complex(复数)类型、bool类型

3.2.3、迭代类型：
    迭代类型用for循环进行遍历。（在后边的迭代器和生成器学习会介绍）

3.2.4、序列类型：
    常见的有list、tuple、str、array、range、[bytes，bytearray，memoryview（二进制序列）] 等。

3.2.5、映射类型(dict)：
    常用的字典，是一个映射类型。映射类型就是有key和map的。

3.2.6、集合：
    set、frozenset（不可以修改的set）

3.2.7、上下文管理类型(with)：
    with语句

3.2.8其他类型：
    模块类型（from，import）、class和实例、函数类型、方法类型（方法和函数是有区别的。方法是类中的函数）、
    代码类型（代码本身也会被Python解释器变为一个对象类型）、object对象、type类型、ellipsis类型（省略号类型）、notimplemented类型
"""


a = None
b = None
print(id(a) == id(b))  # True






