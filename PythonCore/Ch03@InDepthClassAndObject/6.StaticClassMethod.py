# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        StaticClassMethod
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------

1.6、类方法classmethod、静态方法staticmethod和实例方法

实例方法(self)：类中定义的一般方法，仅仅对于类的实例对象进行操作。
类方法classmethod():硬编码，如果换类名又要重新改返回的类名
静态方法staticmethod(cls):

一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。
而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。


编写类时需要采用很多不同的方式来创建实例，而我们只有一个__init__函数，此时静态方法就派上用场了
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


if __name__ == '__main__':
    days = Date(2019, 12, 1)
    print(days)  # 2019/12/1。 __str__使得类对象可以直接打印
    # 方法中传入self这个参数叫实例方法。

    date_str = "2019-12-01"
    # # 此时传递"2019-12-01"输出日期，由于Date类中没有处理方法，我们就在外部处理
    # year, month, day = tuple(date_str.split("-"))
    # new_day = Date(int(year), int(month), int(day))
    # print(new_day)  # 2019/12/1
    # # 外部处理有个弊端就是，每次都需要外部额外处理

    # 用staticmethod在类内部完成初始化，直接使用"类名.方法名"的形式调用
    new_day = Date.parse_from_string(date_str)
    print(new_day)  # 2019/12/1

    # 用classmethod完成初始化
    new_day = Date.from_string(date_str)
    print(new_day)  # 2019/12/1

    # 可见用classmethod比用staticmethod更好用，那么用staticmethod没什么好处了吗？
    # 在valid_str中如果不需要return Date，并且不需要在classmethod中传递cls。那么用staticmethod

    print(Date.valid_str("2019-12-01"))  # True
