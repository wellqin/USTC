# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        工厂方法
Description :   
Author :          wellqin
date:             2019/9/13
Change Activity:  2019/9/13
-------------------------------------------------
"""
from pprint import pprint

"""
意图：
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。

无抽象工厂类，只有一个具体工厂实现类
"""


class Mercedes(object):
    """梅赛德斯
    """

    def __repr__(self):
        return "Mercedes-Benz"


class BMW(object):
    """宝马
    """

    def __repr__(self):
        return "BMW"


# 假设我们有两个“产品”分别是Mercedes和BMW的汽车，如果没有“工厂”来生产它们，我们就要在代码中自己进行实例化，如：
# mercedes = Mercedes()
# bmw = BMW()
# 但现实中，你可能会面对很多汽车产品，而且每个产品的构造参数还不一样，这样在创建实例时会遇到麻烦。这时就可以构造一个“简单工厂”把所有汽车实例化的过程封装在里面。

class SimpleCarFactory(object):
    """
    简单工厂
    """
    @staticmethod
    def product_car(name):
        if name == 'mb':
            return Mercedes()
        elif name == 'bmw':
            return BMW()


# 有了SimpleCarFactory类后，就可以通过向固定的接口传入参数获得想要的对象实例，如下：
c1 = SimpleCarFactory.product_car('mb')
pprint(c1)
c2 = SimpleCarFactory.product_car('bmw')
pprint(c2)


"""
优点：客户端不需要修改代码。
缺点：当需要增加新的运算类的时候，不仅需新加运算类，还要修改工厂类，违反了开闭原则。

实际使用工厂的过程中，我们会发现新问题：如果我们要新增一个“产品”，例如Audi的汽车，
我们除了新增一个Audi类外还要修改SimpleCarFactory内的product_car方法。这样就违背了软件设计中的开闭原则[1]，
即在扩展新的类时，尽量不要修改原有代码。所以我们在简单工厂的基础上把SimpleCarFactory抽象成不同的工厂，
每个工厂对应生成自己的产品，这就是工厂方法。
"""
