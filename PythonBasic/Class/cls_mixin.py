# -*- coding:utf-8 -*-

# coding:utf-8
class Foo(object):
    X = 1
    Y = 14

    @staticmethod
    def average(*mixes):  # "父类中的静态方法"
        """
        @param mixes:
        @return:
        """
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():  # "父类中的静态方法"
        """
        @return:
        """
        print("父类中的静态方法")
        return Foo.average(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):  # 父类中的类方法
        """
        cls
        @return:
        """
        print("父类中的类方法")
        return cls.average(cls.X, cls.Y)


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def average(*mixes):  # "子类中重载了父类的静态方法"
        print("子类中重载了父类的静态方法")
        return sum(mixes) / 3


p = Son()
print("result of p.averag(1,5)")
print(p.average(1, 5))
print("result of p.static_method()")
print(p.static_method())
print("result of p.class_method()")
print(p.class_method())

