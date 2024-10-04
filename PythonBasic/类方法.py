# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        类方法
Description :   
Author :          wellqin
date:             2019/12/3
Change Activity:  2019/12/3
-------------------------------------------------
"""


class A(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        pass


a = A()
# a.m1(1)  # self: <__main__.A object at 0x000001E596E41A90>
# A.m2(1)  # cls: <class '__main__.A'>
# A.m3(1)

# 实例方法
print(A.m1)  # <function A.m1 at 0x000002BF7FF9A488>
print(a.m1)  # <bound method A.m1 of <__main__.A object at 0x000002BF7FFA2BE0>>


"""
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
可以来调用类的属性，类的方法，实例化对象等。

class AA(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


AA.func2()  # 不需要实例化, 比如aa = AA()  aa.func2()




class A(object):
    # 属性默认为类属性（可以给直接被类本身调用）
    num = "类属性"

    # 实例化方法（必须实例化类之后才能被调用）
    def func1(self):  # self : 表示实例化类后的地址id
        print("func1")
        print(self)

    # 类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def func2(cls):  # cls : 表示没用被实例化的类本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1()

    # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
    def func3(self):
        print("func3")
        print(A.num)  # 属性是可以直接用类本身调用的


# A.func1()  # 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
A.func2()
# A.func3()
"""