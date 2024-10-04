# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        190911
Description :   
Author :          wellqin
date:             2019/9/11
Change Activity:  2019/9/11
-------------------------------------------------
"""
import sys
import copy
import re  #  python内建的split()函数只能使用单个分隔符
           # re模块的split()函数可以使用多个分隔符对句子进行分割，其中不同的分隔符要用 “|” 隔开。

# line = sys.stdin.readline()
# line = line.strip().split()
# print(line)

# line = "IamaAstudent"
# print(re.split('A|B|R|=|{|,|}', line))






# import re
# phone = "I am a student"
# g = re.compile(r'([a-z]+)')  # 生成用来提取字母正则表达式对象 re.I忽略大小写
# g1 = re.compile(r'([A-Z]+)')
# g2 = re.compile(r'([0-9])+')
#
# temp = g.findall(phone)      # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# temp.reverse()  # 倒序排列
# string = ''
# for i in range(len(temp)):
#     string = string + ' ' + temp[i]
# print(string)

a, b, res = [], [], []
result = ''
# line = sys.stdin.readline().strip()  # A={1,3,5}B={2,4,6}R=4
line = "A={1,3,5},B={2,4,6},R=2"

tempr = line.split(",")[-1]
r = int(tempr.split('=')[-1])

temp = line.split("},")

tempa = temp[0]
tempb = temp[1]

tempa1 = tempa.split(',')
for i in range(len(tempa1)):
    if i == 0:
        a.append(int(tempa1[i].split('{')[-1]))
    else:
        a.append(int(tempa1[i]))

tempb1 = tempb.split(',')
for i in range(len(tempb1)):
    if i == 0:
        b.append(int(tempb1[i].split('{')[-1]))
    else:
        b.append(int(tempb1[i]))

for i in a:
    for j in b:
        if i>j:
            continue
        else:
            if i + r >= j:
                s = "(" + str(i) + ',' + str(j) + ")"
                res.append(s)

for i in res:
    result = result + i
print(result)

# line = "453452354323411"
# valid = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
# for idx in range(len(line)):
#     i = 0
#     while (i < len(line[idx])):
#         if ((line[idx][i] not in valid)):
#             line[idx] = line[idx][:i] + line[idx][(i + 1):]
#             print(line[idx])
#             continue
#         if (line[idx][i] == '-') and (((i - 1) <= 0) or ((i + 1) >= len(line[idx])) or ((line[idx][(i - 1)] not in valid) and (line[idx][(i + 1) not in valid]))):
#             print(line[idx])
#             line[idx] = line[idx][:i] + line[idx][(i + 1):]
#             continue
#         i += 1
#
# line = list(map(lambda x : x.strip(), line))
# while '' in line:
#     line.remove('')
# print(' '.join(line[::-1]))




