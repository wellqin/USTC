# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        数字
Description :   
Author :          wellqin
date:             2019/8/1
Change Activity:  2019/8/1
-------------------------------------------------
"""
import math
# // 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
print(7.5//2)  # 3.0
print(math.modf(7.5))  # (0.5, 7.0)
print(math.modf(7))  # (0.0, 7.0)
print(round(3.14159, 4))  # 3.1416
print(round(10.5))  # 10



"""
fractions 模块提供了分数类型的支持。

构造函数：
class fractions.Fraction(numerator=0, denominator=1) 
class fractions.Fraction(int|float|str|Decimal|Fraction)
可以同时提供分子（numerator）和分母（denominator）给构造函数用于实例化Fraction类，但两者必须同时是int类型或者numbers.Rational类型，否则会抛出类型错误。当分母为0，初始化的时候会导致抛出异常ZeroDivisionError。

分数类型：

from fractions import Fraction

>>> x=Fraction(1,3)
>>> y=Fraction(4,6)
>>> x+y
Fraction(1, 1)

>>> Fraction('.25') 
Fraction(1, 4)
"""
from fractions import Fraction
x = Fraction(1,3)
y = Fraction(4,6)
print(x+y)  # 1

print(Fraction('.25'))  # 1/4


print(Fraction('3.1415'), type(Fraction('3.1415')))  # 6283/2000

listres = str(Fraction('3.1415')).split("/")
print(listres[0], listres[1])


f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)  # 5/2


xx=Fraction(1,3)
print(float(xx))  # 0.3333333333333333


# decimal 模块提供了一个 Decimal 数据类型用于浮点数计算，拥有更高的精度。
import decimal
decimal.getcontext().prec=4  # 指定精度（4位小数）
yy = decimal.Decimal(1) / decimal.Decimal(7)
print(yy)  # 0.1429
print(yy)  # 0.14286  decimal.getcontext().prec=5


# fractions.gcd(a, b)
# 用于计算最大公约数。这个函数在Python3.5之后就废弃了，官方建议使用math.gcd()。
print(math.gcd(21, 3))


import math



