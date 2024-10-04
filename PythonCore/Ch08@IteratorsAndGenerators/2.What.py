# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        2.What
Description :   
Author :          wellqin
date:             2020/4/14
Change Activity:  2020/4/14
-------------------------------------------------

1.2、什么是迭代器和可迭代对象
"""

from collections.abc import Iterator


# 1. 首先用__getitem__实现迭代
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 没有__getitem__的话，TypeError: 'Company' object is not iterable
    def __getitem__(self, item):  # 能切片，但是迭代器是不能切片的
        return self.employee[item]


company = Company(["li", "lily", "john"])
for i in company:  # for循环会去调用__iter__，没有的话，for会用__getitem__创建一个默认的迭代器
    print(i, end=" ")  # li lily john
print()


# 2. 这里不用上面的，用__iter__来做
class MyIterator(Iterator):  # 继承Iterator，这里__iter__由父类完成，子类重写__next__
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0  # 用迭代器维护这个变量

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            res = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return res


class ComPany(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):  # __iter__方法必须要返回一个迭代器
        return MyIterator(self.employee)  # 返回的是迭代器，这样自定义迭代器复用性更强


company = ComPany(["li", "lily", "john"])
# 1）普通方式用for去迭代
# for i in company:   # 当调用for循环的时候，它会尝试去调用iter(company),首先找的是__iter__,如果没有的话，它就会找__getitem__。
#     print(i, end=" ")  # li lily john

# 2）用迭代器方式去迭代，相当于上面的for循环方式
myItor = iter(company)

while True:           # for循环的实现原理
    try:
        print(next(myItor))
    except StopIteration:
        break
    """
    li
    lily
    john
    """

