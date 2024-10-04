# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        4.SliceObject
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------

1.4、实现可切片的对象
切片操作不会对原来列表有改动，而是新建一个列表。
#   模式[start:end:step]

    其中，第一个数字start表示切片开始位置，默认为0；
    第二个数字end表示切片截止（但不包含）位置（默认为列表长度）；
    第三个数字step表示切片的步长（默认为1）。
    当start为0时可以省略，当end为列表长度时可以省略，
    当step为1时可以省略，并且省略步长时可以同时省略最后一个冒号。
    另外，当step为负整数时，表示反向切片，这时start应该比end的值要大才行。

拓展应用：以后相对其他对象实现像数组般的操作，就可以实现这个协议。

"""

aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(aList[::])    # 返回包含原列表中所有元素的新列表
print(aList[::-1])  # 返回包含原列表中所有元素的逆序列表
print(aList[::2])   # 隔一个取一个，获取偶数位置的元素
print(aList[1::2])  # 隔一个取一个，获取奇数位置的元素
print(aList[3:6])   # 指定切片的开始和结束位置
aList[0:100]        # 切片结束位置大于列表长度时，从列表尾部截断
aList[100:]         # 切片开始位置大于列表长度时，返回空列表             ******这前面都是取值操作******

# 这里可以修改列表
aList[len(aList):] = [9]        # 在列表尾部增加元素              [3, 4, 5, 6, 7, 9, 11, 13, 15, 17, 9]
aList[:0] = [1, 2]              # 在列表头部插入元素        [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 15, 17, 9]
aList[3:3] = [4]                # 在列表中间位置插入元素  [1, 2, 3, 4, 4, 5, 6, 7, 9, 11, 13, 15, 17, 9]
aList[:3] = [1, 2]              # 替换列表元素，等号两边的列表长度相等 [1, 2, 4, 4, 5, 6, 7, 9, 11, 13, 15, 17, 9]
aList[3:] = [4, 5, 6]           # 等号两边的列表长度也可以不相等 [1, 2, 4, 4, 5, 6]
aList[::2] = [0] * 3            # 隔一个修改一个 [0, 2, 0, 4, 0, 6]

print(aList)
aList[::2] = ['a', 'b', 'c']    # 隔一个修改一个 ['a', 2, 'b', 4, 'c', 6]
# aList[::2] = [1, 2]             # 左侧切片不连续，等号两边列表长度必须相等   *****会出现异常******
aList[::2] = [1, 2, 3]             # 左侧切片不连续，等号两边列表长度必须相等  [1, 2, 2, 4, 3, 6]
aList[:3] = []                  # 删除列表中前3个元素 [4, 3, 6]

aList[len(aList):] = [9, 10, 11, 12]  # [4, 3, 6, 9, 10, 11, 12]
del aList[:3]                   # 切片元素连续  [9, 10, 11, 12]
del aList[::2]                  # 切片元素不连续，隔一个删一个  [10, 12]

import numbers


# 自己实现可切片的对象，看Sequence抽象基类源码，可知要实现__reversed__，__getitem__，__contains__等魔法函数
class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):  # 实现这个可以用reverse（group进行反转）
        self.staffs.reverse()
        # 自己实现reverse()函数
        # n = len(self.staffs)
        # for i in range(n >> 1):
        #     self.staffs[i], self.staffs[n - i - 1] = self.staffs[n - i - 1], self.staffs[i]

    def __getitem__(self, item):  # 切片操作传入的是slice对象  # 索引取值传入的是int类型（因此需要实现这两种方法）
        # 实现切片功能的关键，如果注释掉，会出现报错
        # return self.staffs[item] 即可切片，但是希望切片后返回新的依然可以切片的对象，就需要下面方法

        # item理解：若传入的是[m:n],则其为切片对象，若传入n，则为整数下标

        cls = type(self)  # django中的queryset实现了这个魔法方法，可以进行切片
        # cls为<class '__main__.Group'>，即Group类
        if isinstance(item, slice):
            # 当item为切片类型操作时，self.staffs[item]中item为切片类型
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            # 注意staffs=[self.staffs[item]]的[],不加的话有巨大影响
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):  # 实现它可以知道员工的人数len(group)
        return len(self.staffs)

    def __iter__(self):  # 实现它可以遍历出具体员工 否则只是遍历出<__main__.Group object at 0x000002843AD3EF48>
        return iter(self.staffs)  # 遍历出对象与__getitem__有关

    def __contains__(self, item):  # 实现它就可以利用if语句判断(if "li" in group: 返回bool)
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["li1", "li2", "li3", "li4"]
group = Group(company_name="university", group_name="user", staffs=staffs)

item1 = group[1:3]
item2 = group[2]
print(list(item1))  # ['li2', 'li3']
print(list(item2))  # ['li3']  改成staffs=self.staffs[item]时结果为['l', 'i', '3']

reversed(group)  # 反转需要实现__reversed__魔法方法

print(len(group))  # 4

if "li1" in group:
    print("YES")  # YES

for user in group:
    print(user)
    """
    查看打印结果，说明数据反转
    li4
    li3
    li2
    li1
    """

    """这就是不可改变序列类型（Sequence）的协议的实现，以后需要实现某个协议，根据协议类型实现协议各自的魔法方法，
    这样就可以完成协议类型的开发（框架开发等）"""
