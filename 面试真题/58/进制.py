# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        进制
Description :   
Author :          wellqin
date:             2019/9/21
Change Activity:  2019/9/21
-------------------------------------------------
"""

# n = int(input())

# dicts = {
#     "1":"0",
#     "2":"0",
#     "3":"0",
#     "4":"0",
#     "5":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
#     "1":"0",
# }

# def decimalToNBaseByNormal(decimalVar, base):
#     tempList = []
#     temp = decimalVar
#     i = 0
#     while (temp > 0):
#         ord = temp % base
#         if (ord > 9):  # 如果余数大于9，则以字母的形式表示
#             ord = chr(65 + (ord - 10))   # 把数字转换成字符
#         tempList.append(ord)
#         temp = int(temp / base)
#         i = i + 1
#     tempList.reverse()
#     # print(tempList)
#     binary = ""
#     for j in range(len(tempList)):
#         binary = binary + str(tempList[j])
#     print("the decimal is: %d and after convering by %d base is %s"%(decimalVar, base, binary))
#
# import sys
# def main():
#     decimal = eval(input("please input the decimal for converting binary: "))
#     base = eval(input("please input base: "))
#     decimalToNBaseByNormal(decimal, base)
#     # decToNBaseByRecursion(decimal, base)
# main()

# def func(n,x):
#     # n为待转换的十进制数，x为机制，取值为2-16
#     ls = [0,1,2,3,4,5,6,7,8,9,'`','!','@','#','$','%','^','&','*','(',')','{','}','\\','<','>','?']
#     num = []
#     while True:
#         sp = n // x   # 商
#         div = n % x    # 余数
#         num = num+[div]
#         if sp == 0:
#             break
#         n = sp
#     num.reverse()
#     for i in num:
#         print(ls[i], end='')
#
# func(53,27)


def func(n,x):
    ls = [0,1,2,3,4,5,6,7,8,9,'`','!','@','#','$','%','^','&','*','(',')','{','}','\\','<','>','?']
    num = []
    while True:
        sp = n // x
        div = n % x
        num = num+[div]
        if sp == 0:
            break
        n = sp
    num.reverse()
    for i in num:
        print(ls[i], end='')

func(53,27)

