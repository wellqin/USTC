# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        下划线
Description :   
Author :          wellqin
date:             2019/9/9
Change Activity:  2019/9/9
-------------------------------------------------
"""
# 1. 单前导下划线 _var
"""
下划线前缀的含义是告知其他程序员：以单个下划线开头的变量或方法仅供内部使用。 该约定在PEP 8中有定义。

单个下划线是一个Python命名约定，表示这个名称是供内部使用的。 它通常不由Python解释器强制执行，仅仅作为一种对程序员的提示。
单个下划线并没有阻止我们“进入”类并访问该变量的值。
通配符导入，前导下划线的确会影响从模块中导入名称的方式。 from my_module import *
与通配符导入不同，常规导入不受前导单个下划线命名约定的影响： import my_module
"""

# 2. 单末尾下划线 var_
"""
单个末尾下划线（后缀）是一个约定，用来避免与Python关键字产生命名冲突。 PEP 8解释了这个约定。

def make_object(name, class):      class是关键字报错      SyntaxError: "invalid syntax"
def make_object(name, class_):
"""

# 3. 双前导下划线 __var
# 双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。名称修饰是否也适用于方法名称？ 是的，也适用。
# 双下划线名称修饰对程序员是完全透明的。


class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


t = Test()
print(dir(t))  # 对象属性的列表

"""
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']

"""
# 'foo'  '_bar' 对于self.__baz而言，情况看起来有点不同。 当你在该列表中搜索__baz时，你会看不到有这个名字的变量。
# 如果你仔细观察，你会看到此对象上有一个名为_Test__baz的属性。 这就是Python解释器所做的名称修饰。 它这样做是为了防止变量在子类中被重写。


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'


t2 = ExtendedTest()
print(t2.foo)    # 'overridden'
print(t2._bar)   # 'overridden'
print(t2.__baz)  # AttributeError: 'ExtendedTest' object has no attribute '__baz'
# 名称修饰被再次触发了！ 事实证明，这个对象甚至没有__baz属性：
print(t2._ExtendedTest__baz)    # 'overridden' 原来的_Test__baz还在


# 4. 双前导和双末尾下划线 _var_
"""
如果一个名字同时以双下划线开始和结束，则不会应用名称修饰。 由双下划线前缀和后缀包围的变量不会被Python解释器修改：
"""

# 5.单下划线 _
# 来表示某个变量是临时的或无关紧要的。















