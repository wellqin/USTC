# -*- coding:utf-8 -*-

"""
在上述例子中，foo只是个函数，但当调用ik.foo的时候我们得到的是一个已经跟实例ik绑定的函数。
调用foo时需要两个参数，但调用ik.foo时只需要一个参数。foo跟ik进行了绑定，因此，当我们打印ik.foo时，会看到以下输出:
<bound method Kls.foo of <__main__.Kls object at 0x0551E190>>

当调用ik.class_foo时，由于class_foo是类方法，因此，class_foo跟Kls进行了绑定（而不是跟ik绑定）。当我们打印ik.class_foo时，输出：
<bound method type.class_foo of <class '__main__.Kls'>>

当调用ik.static_foo时，静态方法并不会与类或者实例绑定，因此，打印ik.static_foo（或者Kls.static_foo）时输出：
<function static_foo at 0x055238B0>

概括来说，是否与类或者实例进行绑定，这就是实例方法，类方法，静态方法的区别。
"""


class Kls(object):
    def foo(self, x):  # 对于实例方法，调用时会把实例ik作为第一个参数传递给self参数。因此，调用ik.foo(1)时输出了实例ik的地址。
        print('executing foo(%s,%s)' % (self, x))

    @classmethod
    def class_foo(cls, x):  # 对于类方法，调用时会把类Kls作为第一个参数传递给cls参数。因此，调用ik.class_foo(1)时输出了Kls类型信息。
        # 前面提到，可以通过类也可以通过实例来调用类方法，在上述代码中，我们再一次进行了验证。
        print('executing class_foo(%s,%s)' % (cls, x))

    @staticmethod
    def static_foo(x):  # 对于静态方法，调用时并不需要传递类或者实例。其实，静态方法很像我们在类外定义的函数，
        # 只不过静态方法可以通过类或者实例来调用而已。
        print('executing static_foo(%s)' % x)


if __name__ == '__main__':
    ik = Kls()

    # 实例方法
    ik.foo(1)
    print(ik.foo)
    print('==========================================')

    # 类方法
    ik.class_foo(1)
    Kls.class_foo(1)
    print(ik.class_foo)
    print('==========================================')

    # 静态方法
    ik.static_foo(1)
    Kls.static_foo('hi')
    print(ik.static_foo)
