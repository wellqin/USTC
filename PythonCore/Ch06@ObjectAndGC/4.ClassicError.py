# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.ClassicError
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.4、一个经典的参数错误

+ : 产生一个新的list,加号的两边必须同一类型才能相加
+=: 原地加,加号的两边不是同一类型也能相加，可以为任意（序列类型）序列的特性就是可以利用for循环进行遍历，即可迭代

为什么二个不同对象，产生了纠葛？com2，com3二者都采用了默认的staffs=[]参数，而[]list是可变对象
"""


def add(a, b):
    a += b  # 就地修改
    return a


# a = 1
# b = 2
# c = add(a,b)
# print(a,b) # 1 2
# print(c) # 3
#
# a = [1,2]
# b = [3,4]
# c = add(a, b)
# print(a, b)  # [1, 2, 3, 4] [3, 4]  ？？？原因是list为可变对象
# print(c)  # [1, 2, 3, 4]
#
# a = (1,2)
# b = (3,4)
# c = add(a, b)
# print(a, b)  # (1, 2) (3, 4)
# print(c)  # (1, 2, 3, 4)


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    com1 = Company("com1", ["lishuntao1", "lishuntao2"])
    com1.add("lishuntao3")
    com1.remove("lishuntao1")
    print(com1.staffs)  # ['lishuntao2', 'lishuntao3']   OK

    com2 = Company("com2")
    com2.add("lishuntao")
    print(com2.staffs)  # ['lishuntao']

    print(Company.__init__.__defaults__)  # (['lishuntao'],)
    # 如果自己传递staffs参数，就不会出现__defaults__
    # 结合下面注释的可以总结出，当传递一个列表的时候，可能会影响值的改变，在这里，com3与com2
    # 都没有传入值，则对象都采用默认值，因此值的改动会影响默认值的改变，因此以后出现这样的问题
    # 需要警惕这样的结果，才不会一头雾水。

    com3 = Company("com3")
    com3.add("lishuntao5")
    # 为什么二个不同对象，产生了纠葛？com2，com3二者都采用了默认的staffs=[]参数，而[]list是可变对象
    print(com2.staffs)  # ['lishuntao', 'lishuntao5']  ？
    print(com3.staffs)  # ['lishuntao', 'lishuntao5']  ？

    print(com2.staffs is com3.staffs)  # True
