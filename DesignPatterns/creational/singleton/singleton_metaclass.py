# -*- coding:utf-8 -*-
import threading
import time

"""
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""


class FooExample:
    def __init__(self):
        print("FooExample.__init__")

    def __call__(self, *args, **kwargs):
        print("FooExample.__call__")


# 如果想把一个类设计成 MetaClass 元类，其必须符合以下条件：
# 必须显式继承自 type 类；
# 类中需要定义并实现 __new__() 方法，该方法一定要返回该类的一个实例对象，因为在使用元类创建类时，该 __new__() 方法会自动被执行，用来修改新建的类。
class SingletonType(type):
    """
    类变量在所有实例化对象中是作为公用资源存在的，所以通过类名修改类变量的值，会影响所有的实例化对象。
    在调用方式上：既可以使用类名直接调用，也可以使用类的实例化对象调用。
    注意，通过类对象是无法修改类变量的。通过类对象对类变量赋值，其本质将不再是修改类变量的值，而是在给该对象定义新的实例变量
    """
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):  # 可以使得类实例对象可以像调用普通函数那样，以 “对象名()” 的形式使用
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    # 动态为该类添加一个_instance属性
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    """
    # 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建Foo时，要通过Foo.__new__()来创建，
    # 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
    """
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    obj = FooExample()
    obj()

    obj1 = Foo('name')
    obj2 = Foo('name')
    print(obj1, obj2)
