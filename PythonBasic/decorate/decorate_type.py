# -*- coding:utf-8 -*-


def decorateFunction(fun):
    class wrapClass:
        def __init__(self, *a, **k):
            self.wrappedClass = fun(*a, **k)

        def fun1(self, *a, **k):
            print("准备调用被装饰类的方法fun1")
            self.wrappedClass.fun1(*a, **k)
            print("调用被装饰类的方法fun1完成")

    return wrapClass


@decorateFunction
class wrappedClass:

    def __init__(self, *a, **k):
        print("我是被装饰类的构造方法")
        if a:
            print("构造方法存在位置参数：", a)
        if k:
            print("构造方法存在关键字参数：", k)
        print("被装饰类构造方法执行完毕")

    def fun1(self, *a, **k):
        print("我是被装饰类的fun1方法")
        if a:
            print("fun1存在位置参数：", a)
        if k:
            print("fun1存在关键字参数：", k)
        print("被装饰类fun1方法执行完毕")

    def fun2(self, *a, **k):
        print("我是被装饰类的fun2方法")


c1 = wrappedClass('testPara', a=1, b=2)
c1.fun1()
# c1.fun2()  # AttributeError: 'wrapClass' object has no attribute 'fun2'
# 可以看到被装饰类的相关方法必须在装饰类中调用才能执行，装饰后的类如果装饰函数定义类时未定义被装饰类的同名函数，
# 在装饰后返回的类对象无法执行被装饰类的相关方法。

