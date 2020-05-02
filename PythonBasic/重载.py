"""
-------------------------------------------------
File Name:        重载
Author :          wellqin
date:             2020/5/2
-------------------------------------------------

函数重载？简单的理解，支持多个同名函数的定义，只是参数的个数或者类型不同，在调用的时候，解释器会根据参数的个数或者类型，调用相应的函数。

二种情况： 参数个数不同的情形 | 参数类型不同的情形
"""

# 1. 参数个数不同的情形
"""
C++ 是怎么实现重载的

#include <iostream>
using namespace std;

int func(int a)
{
    cout << 'One parameter' << endl;
}

int func(int a, int b)
{
    cout << 'Two parameters' << endl;
}

int func(int a, int b, int c)
{
    cout << 'Three parameters' << endl;
}
"""


# 如果 Python 按类似的方式定义函数的话，不会报错，只是后面的函数定义会覆盖前面的，达不到重载的效果。
# 但是我们知道，Python 函数的形参十分灵活，我们可以只定义一个函数来实现相同的功能，就像这样
def func1(*args):
    if len(args) == 1:
        print('One parameter')
    elif len(args) == 2:
        print('Two parameters')
    elif len(args) == 3:
        print('Three parameters')
    else:
        print('Error')


# 2. 参数类型不同的情形
"""
先看下当前情况下 C++ 的重载是怎么实现的
代码中，func 支持两种类型的参数：整形和浮点型。调用时，解释器会根据参数类型去寻找合适的函数。

#include <iostream>
using namespace std;

int func(int a)
{
    cout << 'Int: ' << a << endl;
}

int func(float a)
{
    cout << 'Float: ' << a << endl;
}
"""


# Python 要实现类似的功能，需要借助 functools.singledispatch 装饰器
# func 函数被 functools.singledispatch 装饰后，又根据不同的参数类型绑定了另外两个函数。
# 当参数类型为整形或者浮点型时，调用绑定的对应的某个函数，否则，调用自身

from functools import singledispatch


@singledispatch
def func(a):  # 需要注意的是，这种方式只能够根据第一个参数的类型去确定最后调用的函数
    print('Other: {a}'.format(a=a))


@func.register(int)
def _(a):
    print('Int: {a}'.format(a=a))


@func.register(float)
def _(a):
    print('Float: {a}'.format(a=a))


if __name__ == '__main__':
    func('zzz')
    func(1)
    func(1.2)
