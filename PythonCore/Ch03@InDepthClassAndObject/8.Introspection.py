# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        8.Introspection
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------

1.8、python对象的自省机制
自省：就是通过一定的机制查询到对象的内部结构。

通过实例.__dict__只是查询实例属性，不能查询到对象父类属性
     类.__dict__比对象也就是实例更加丰富

dir会列出我们对象的所有属性，但是没有属性值
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 静态方法的缺点就是: 硬编码，如果换类名又要重新改返回的类名
    @staticmethod
    def parse_from_string(dateStr):  # 注意这里没有self和cls，其调用必须通过Date，即Date.parse_from_string
        year, month, day = tuple(dateStr.split("-"))
        return Date(int(year), int(month), int(day))  # 如果换类名Date又要重新改成新类名

    # 为啥不用classmethod替换staticmethod呢？
    # 检查时间格式是否正确,不需要对象返回回来，因此这个时候它就有用了，而其余都是要将对象返回回来
    @staticmethod
    def valid_str(dateStr):
        year, month, day = tuple(dateStr.split("-"))
        if int(year) > 0 and (0 < int(month) <= 12) and int(day) <= 31:
            return True
        else:
            return False

    # 类方法就解决掉刚才的硬编码问题
    @classmethod
    def from_string(cls, dateStr):  # cls就是类本身.cls只是一个标识，换成其他字符也可以
        year, month, day = tuple(dateStr.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


class Person:
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name
        self.school = school_name


if __name__ == '__main__':
    student = Student("USTC")  # 实例
    # 通过__dict__查询属性

    print(student.__dict__)  # {'school': 'USTC', 'school_name': 'USTC'}

    # 上面打印的是实例的属性,为啥name属性没有进入__dict__呢？因为name属于Person类，
    # 实例查询到name的值，但并不是说name属性属于实例
    print(student.name)  # user
    print(Person.__dict__)
    # 结果如下：类的__dict__比对象也就是实例更加丰富
    # {'__module__': '__main__', 'name': 'user', '__dict__': <attribute '__dict__' of 'Person' objects>,
    # '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None} 给实例添加属性

    student.__dict__["school_addr"] = "合肥市"
    print(student.school_addr)  # 合肥市
    print(student.__dict__)  # {'school_name': 'USTC', 'school': 'USTC', 'school_addr': '合肥市'}

    # 会列出我们对象的所有属性，但是没有属性值
    print(dir(student))

    """
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '
    __le__
    ', '
    __lt__
    ', '
    __module__
    ', '
    __ne__
    ', '
    __new__
    ', '
    __reduce__
    ', '
    __reduce_ex__
    ',
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    'name', 'school_addr', 'school_name']
    """

    list1 = [1, 2, 3, 4]
    print(dir(list1))

    """
    # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
    '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
    '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
    '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
    '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
    '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    """

    print(list1.__dict__)  # AttributeError: 'list' object has no attribute '__dict__'
    # 列表不可以用__dict__，列表没有这个属性
