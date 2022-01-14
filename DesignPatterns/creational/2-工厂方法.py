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
import abc
from pprint import pprint

"""
这个和简单工厂有区别，简单工厂模式只有一个工厂，工厂方法模式对每一个产品都有相应的工厂
    好处：增加一个运算类（例如N次方类），只需要增加运算类和相对应的工厂，两个类，不需要修改工厂类。
    缺点：增加运算类，会修改客户端代码，工厂方法只是把简单工厂的内部逻辑判断移到了客户端进行。
    
工厂方法：一个抽象工厂接口，里面实现一个创建方法，一或多个工厂实现类
"""


class AbstractCar(object):
    """
    抽象车
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def car(self):
        pass


class Mercedes(AbstractCar):
    """梅赛德斯
    """

    def __repr__(self):
        return "Mercedes-Benz"

    def car(self):
        return "BenzCAR"


class BMW(AbstractCar):
    """宝马
    """

    def __repr__(self):
        return "BMW"

    def car(self):
        return "BMWCAR"


class AbstractFactory(object):
    """抽象工厂
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass


class MercedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """

    def product_car(self):
        return Mercedes()


class BMWFactory(AbstractFactory):
    """宝马工厂
    """

    def product_car(self):
        return BMW()


c1 = MercedesFactory().product_car()
pprint(c1)

c2 = BMWFactory().product_car()
pprint(c2)

if __name__ == '__main__':
    """
    （1）首先获取A的所有子类对象
    （2）利用反射机制实例化子类对象
    （3）调用子类对象的print_name方法
    """
    # 获取A的所有子类
    sub_class_list = AbstractCar.__subclasses__()
    print(sub_class_list)
    for i in range(len(sub_class_list)):
        # 获取子类的类名
        class_name = sub_class_list[i].__name__
        print(class_name)
        # 导入model模块
        model_module = __import__('creational')
        """
        如果模块导入成功，该模块下的所有py文件会作为模块的属性，因此使用getattr(模块，文件名)获取即可
        文件名不需要加.py后缀
        """
        m_py = getattr(model_module, 'm')
        # 根据子类名称从m.py中获取该类
        obj_class_name = getattr(m_py, class_name)
        # 实例化对象
        obj = obj_class_name()
        # 调用print_name方法
        getattr(obj, 'print_name')()
