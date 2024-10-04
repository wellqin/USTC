# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.HowGenerator
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

1.4、python是如何实现生成器的
"""

# 1.python中函数的工作原理
import dis
import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


# python.exe会用一个叫做 PyEval_EvalFramEx(c函数)去执行foo函数， 首先会创建一个栈帧(stack frame)
"""
python一切皆对象，栈帧对象，编译成字节码对象
当foo调用子函数 bar， 又会创建一个栈帧
所有的栈帧都是分配在堆内存(栈帧一直在堆内存之中)上，这就决定了栈帧可以独立于调用者存在

栈帧object中包含f_code和f_back
    f_code 就是编译的函数字节码 f_code会指向PycodeObject，即运行的字节码对象
    f_back 会指向调用者
"""

# print(dis.dis(foo))  # 查看运行的字节码过程
"""
 22           0 LOAD_GLOBAL              0 (bar)
              3 CALL_FUNCTION            0 (0 positional, 0 keyword pair)
              6 POP_TOP
              7 LOAD_CONST               0 (None)
             10 RETURN_VALUE
"""

foo()
print(frame.f_code.co_name)  # bar栈帧
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)  # foo栈帧  # 虽然这个函数已经运行完成，我们照样可以去堆内存中找到它的栈帧

# 生成器原理
"""
普通函数对象：
函数栈帧object中包含f_code和f_back
    f_code 就是编译的函数字节码 f_code会指向PycodeObject，即运行的字节码对象
    f_back 会指向调用者
    
生成器函数对象：
函数栈帧object中包含gi_frame和gi_code
    gi_code指向PycodeObject，即运行的字节码对象
    gi_frame指向PyFrameObject，里面包含f_lasti[最近执行的代码]和f_locals
不会一次运行完，而且由于具有f_lasti和f_locals，我们可以从“断点”处继续运行
"""


def gen_func():
    yield 1
    name = "lisha"
    yield 2
    age = 18
    return "HUT"


gen = gen_func()  # 返回生成器对象
print(dis.dis(gen))
"""
 70           0 LOAD_CONST               1 (1)
              3 YIELD_VALUE
              4 POP_TOP

 71           5 LOAD_CONST               2 ('lisha')
              8 STORE_FAST               0 (name)

 72          11 LOAD_CONST               3 (2)
             14 YIELD_VALUE
             15 POP_TOP

 73          16 LOAD_CONST               4 (18)
             19 STORE_FAST               1 (age)

 74          22 LOAD_CONST               5 ('HUT')
             25 RETURN_VALUE
"""
# 人为控制它的执行流程
# 现在还没有开始执行
print(gen)
print(gen.gi_frame.f_lasti)  # -1      f_lasti：可以知道进行到哪一个步骤了
print(gen.gi_frame.f_locals)  # {}

# 每次调用都会生成新的栈帧对象，都可以拿来用
# 开始执行1次调用
next(gen)  # 进行下一步流程
print(next(gen))  # 2
print(gen.gi_frame.f_lasti)  # 位置为3  [字节码中 3 YIELD_VALUE]
print(gen.gi_frame.f_locals)  # {}

# 开始执行2次调用
next(gen)
print(next(gen))  # StopIteration: HUT
print(gen.gi_frame.f_lasti)  # 位置为14  [字节码中 14 YIELD_VALUE]
print(gen.gi_frame.f_locals)  # {"name":"lisha"}
