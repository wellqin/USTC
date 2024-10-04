# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        1.DuckType
Description :   
Author :          wellqin
date:             2020/4/10
Change Activity:  2020/4/10
-------------------------------------------------
1.1、鸭子类型和多态
维基百科中的解释为：
鸭子类型（英语：duck typing）在程序设计中是动态类型的一种风格。
在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，
而是由"当前方法和属性的集合"决定。这个概念的名字来源于由詹姆斯·惠特科姆·莱利提出的鸭子测试。

“鸭子测试”可以这样表述：
“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
”在鸭子类型中，关注点在于对象的行为，能作什么；而不是关注对象所属的类型。

python：定义多个类实现同一个方法，在方法里面说什么，那么它就是什么

"""


# JAVA实现多态思想:需要继承父类在覆盖父类的方法实现多态
# 例如：一般情况先定义一个父类Animal，然后这个Animal有一个say()方法。
# 然后在写其他类例如上面的Cats类，Cats类继承Animal类，然后重写say()方法。
# 然后指定类型实例化这个Cats对象，在python中不需要指定类型，在JAVA中(静态语言)必须指定类型，
# 这是动态语言和静态语言最大的区别: 就是可以指向任何一个类型
class Animal:
    def say(self):
        print("I am a Animal")


class Cats(Animal):
    def say(self):
        print("I am a Cats")


animal = Cats()  # JAVA中实例化要指明类型
animal.say()  # I am a Cats
print("===============================================================")


# Python中实现多态：没有继承任何一个父类
# 在python中都要做的一件事就是每个对象下都要写这个say()方法
class Cat:
    def say(self):
        print("I am a cat")


class Dog:
    def say(self):
        print("I am a dog")


class Duck:
    def say(self):
        print("I am a duck")


# 实例化对象，在调用say方法  三个类实现同一个方法名，这就是多态。然后可以将这些类归为一种类型（鸭子类型）
# python中的魔法函数充分也利用了鸭子类型的特性，可以在任一类中定义
animalList = [Cat, Dog, Duck]
for animals in animalList:
    # 三个类实现了同一个say方法，在调用的时候就可以不同类对象调用同一个方法
    animals().say()  # I am a cat    I am a dog     I am a duck

print("===============================================================")

name_list = ["list1", "list2"]
name_list1 = ["love", "python"]
name_tuple = (3, 4)
name_set = set()
name_set.add(5)
name_set.add(6)
name_list.extend(name_set)  # 参数name_set：['list1', 'list2', 5, 6] 参数name_tuple：['list1', 'list2', 3, 4]
print(name_list)  # 参数：name_list1：['list1', 'list2', 'love', 'python']

"""
extend源码

这里说的是只要传入的参数是一个可迭代的类型就可以，
就连我们自定义的类将类的魔法函数__getitem__(返回 )、__iter__就可以变成可迭代的，都可以传入
def extend(self, *args, **kwargs): # real signature unknown
    Extend list by appending elements from the iterable. 
    pass
"""
print("===============================================================")


# 所以我们要转变观念，比如以前认为extend只能传递列表，现在知道可迭代的类型都可以
# 甚至自己实现的可迭代的类型也可以，在类中加上魔法函数__getitem__(返回 )、__iter__即可
class Students(object):
    def __init__(self, student_list):
        self.student = student_list

    def __getitem__(self, item):  # 给类增加了可迭代的属性
        return self.student[item]

    def __len__(self):
        return len(self.student)  # 这里一定要返回的是正整数


students = Students(["lisha", "wang", "li"])
name_list.extend(students)  # extend类实例对象
print(name_list)  # ['list1', 'list2', 5, 6, 'lisha', 'wang', 'li']

