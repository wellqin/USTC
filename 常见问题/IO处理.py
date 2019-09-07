# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        Newcoder
Description :   
Author :          wellqin
date:             2019/8/1
Change Activity:  2019/8/1
-------------------------------------------------
"""
import sys
"""
在牛客网上做编程题，真的是崩溃，才发现连输入都不太会处理，作为一个整理狂，干啥都想要整理起来。
以下是我在做题过程中遇见的几种输入情况以及处理方式，另外，本人超级喜欢用list，对于各种输入都想处理成list格式（持续更新）。
输入的处理
1. 对于一行输入多个的情况
例如：[[1,2],[2,3]],4:

eval() 函数本来是用来执行一个字符串表达式，并返回表达式的值。
"""

# 1. 对于一行输入多个的情况
# 方法一：
# L = list(eval(input()))  # eval() 函数也可以直接用来提取用户输入的多个值。
L = [[1, 2], [2, 3]], 4

array = L[0]
target = L[1]
print(array, target)  # [[1, 2], [2, 3]] 4
print(array)  # [[1, 2], [2, 3]]
print(target)  # 4

# 方法二：
# target1, array1 = input().split(',', 1)
# target1 = int(target1)
# array1 = list(eval(array1))


# 方法三：输入什么就输出什么
# a = sys.stdin.readline().strip()  # readline()逐行读取
# b = sys.stdin.readline().strip()
# print(a, b)
# print(a)
# print(b)
"""
strip()方法只能用于移除字符串 开头和结尾 指定的字符（默认为空格或换行符）或字符序列。
例如：
str = ’ abcd0e ’
print(str.strip())
输出：abcd0e
print(str.strip(‘0’))
输出： abcde
"""

"""
这里补充下split()的用法：
默认以空格切分，split(’’,1)表示分成两块，例如：
str = “Line1-abcdef \nLine2-abc \nLine4-abcd”;
print str.split( ); # 以空格为分隔符，包含 \n
print str.split(’ ', 1 ); # 以空格为分隔符，分隔成两个
结果：
[‘Line1-abcdef’, ‘Line2-abc’, ‘Line4-abcd’]
[‘Line1-abcdef’, ‘\nLine2-abc \nLine4-abcd’]
"""


# 2. 对于先输入个数n ，后输入n个数的情况（用循环）
"""
2. 对于先输入个数n ，后输入n个数的情况（用循环）
例如：
输入个数4，接着输入4个数2 2 1 3 

4
2
2
1
3

代码：
"""
# n = int(input())
# li = []
# for i in range(n):
#     b = int(input())
#     li.append(b)
# print(li)  # [2, 2, 1, 3]

"""
另外一种情况：
输入个数4，接着输入4组数
"""


# 3.对于含有空格的一行数的输入
"""
3.对于含有空格的一行数的输入
例如：
输入2 4 5 8 9这样的
代码：
如果仅仅只是input().split()
得到：[‘2’,‘4’,‘5’,‘8’,‘9’]
"""
li = map(int, input().split())
# li = list(map(int, input().split()))
# # print(li)  # [2,4,5,8,9]


# 4.保证list里面的数全为整数
"""
4.保证list里面的数全为整数
代码：
"""
b = [1, 2, 2]
b = [int(i) for i in b]
print(b)  # [1,2,2]


# 输出的处理
"""
1.对于[‘1’,‘2’,‘3’,‘4’]这样的格式要求变成1 2 3 4 5
代码：
"""
a = ['1', '2', '3', '4']
print(''.join(a))  # 1234
print(' '.join(a))  # 1 2 3 4

# 若要求输出格式为1,2,3,4
print(','.join(a))  # 1,2,3,4

"""
2.对于循环输出多个数，两个数之间用空格隔开
代码:
"""
for i in range(5):
    print(i, end=' ')
