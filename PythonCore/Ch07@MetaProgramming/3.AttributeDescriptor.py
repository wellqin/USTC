# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        3.AttributeDescriptor
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.3、属性描述符和属性查找过程

属性描述符：
    应用：数据库多字段验证，通常给每一个字段在类中写验证逻辑，这很冗杂。此时可以用属性描述符进行操作。
    分类：数据属性描述符 | 非数据属性描述符

属性查找过程：
    1. 先查找类或基类，并且属性正好是【数据属性描述符】，则调用其__get__函数返回。没找到则下一步。
    2. 查找对象属性，找到直接返回，没找到则下一步。
    3. 查找在类或其基类的属性中，并且属性是【非数据属性描述符】，那么调用其__get__方法，属性不是描述符则直接返回类中的属性。
    4. 若果此时都找不到，但是类中有__getattr__方法，调用__getattr__方法，否则抛出AttributeError

    可见，如果没有属性描述符，其过程为：查找对象属性-->查找在类或其基类的属性-->类中有__getattr__方法
                                  最好找不到就抛出AttributeError
"""

import numbers


# 验证数据库字段的实现
class IntField:
    # 数据描述符：至少实现了__get__，__set__二个
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):  # 检查是否为整型的逻辑
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value  # 这里self.value自定义后，在__get__中返回

    def __delete__(self, instance):  # 实现这三个魔法方法中的任意一个魔法方法，类都会变成属性描述符
        pass


class NonDataIntField:
    # 非数据属性描述符：只实现了__get__
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()  # age是data descriptor  数据库模型类的age字段整型验证
    # age = NonDataIntField() # age是non-data descriptor


user = User()
# user.age = 18  # 调用age属性描述符的__set__方法, 优先级最高
# print(user.age)  # 18
# print(getattr(user, "age"))  # 18 与上面等价

# user.age = "abc"  # 调用age属性描述符的__set__方法
# print(user.age)  # ValueError: int value need

user.__dict__["age"] = "abc"
print(user.__dict__)  # {'age': 'abc'}
print(user.age)  # AttributeError: 'IntField' object has no attribute 'value'
# 原因就是会按照顺序：第一优先级: 类或基类的数据属性描述符，调用其__get__函数返回，此时return self.value出错


"""
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__找不到属性时抛出 AttributeError， 此时就会调用到__getattr__，

而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：

（1）如果“age”是出现在User或其基类的__dict__中， 且age是数据描述符， 那么调用其__get__方法, 否则

（2）如果“age”出现在user对象的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则

（3）如果“age”出现在User或其基类的__dict__中
    （3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
    （3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError
"""


# 验证查找过程
class Person:
    age = IntField()  # age是data descriptor  数据库模型类的age字段整型验证
    height = NonDataIntField()  # height是non-data descriptor
    sex = ""  # 类属性

    def __getattr__(self, item):
        return "not find"


person = Person()
person.age = 28  # 第一优先级: 类或基类的数据属性描述符，调用其__get__函数返回
print(person.age)
person.hand = "2"  # 第二优先级: 对象属性
print(person.hand)
person.height = 160  # 第三优先级: 类或基类的非数据属性描述符，调用其__get__函数返回
print(person.height)
person.sex = "nan"  # 第四优先级: 类自身属性
print(person.sex)
# person.attr  # 第五优先级: __getattr__
print(person.attr)
# 第六优先级: 没有__getattr__，抛出AttributeError




