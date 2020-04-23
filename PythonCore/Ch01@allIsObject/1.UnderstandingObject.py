"""
-------------------------------------------------
File Name:        UnderstandingObject
Author :          wellqin
date:             2020/4/10
-------------------------------------------------

函数和类也是对象，属于python的一等公民
"""


""" 1. 函数和类可以赋值给一个变量 """


def ask(name="bobby"):  # 先以函数为例
    print(name)


# my_func = ask() TypeError: 'NoneType' object is not callable  不能加括号
my_func = ask
my_func("bobby")  # bobby
my_func("alan")  # alan


class Person:  # 再以类为例
    def __init__(self):
        print("bobby")


my_class = Person
my_class()  # bobby

""" 2. 可以添加到集合对象中 """
obj_list = [ask, Person]
for obj in obj_list:
    print(obj())

# bobby  # ask()
# None   # ask()的返回值为None，为什么之前没有，因为print缘故
# bobby  # Person()
# <__main__.Person object at 0x00000260A1DD8780>  # Person()返回的类对象


""" 3. 可以作为参数传递给函数 """


def print_type(item):
    print(type(item))  # <class 'function'>
    print(item)  # <function ask at 0x00000216DF269AE8>


print(print_type(ask))  # None

""" 4. 可以当做函数的返回值 【装饰器原理】 """


def decorator():
    print("dec start")
    return ask


my_ask = decorator()
my_ask("tom")  # dec start  tom
