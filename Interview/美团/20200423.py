"""
-------------------------------------------------
File Name:        20200423
Author :          wellqin
date:             2020/4/23
-------------------------------------------------
"""

# N = int(input())
# nums = list(map(int, input().split()))
#
# li = []
# for i in range(N):
#     aa = list(map(int, input().split()))
#     li.append(aa)


import sys


def translate(num):
    neg = False  # 负数
    string = str(num)  # Python默认在转换成字符串时忽略前面的0，因此可以通过格式转换的方法实现去0
    if string[0] == "-":
        neg = True
        string = string[1:]

    a, b, c = string.partition('.')
    c = (c + "0" * 2)[:2]
    strings = ".".join([a, c])

    count = 0
    sumstring = ''
    a, b, c = strings.partition('.')
    for i in a[::-1]:
        count += 1  # 计数
        if count % 3 == 0 and count != len(a):  # zero
            i = ',' + i
            sumstring = i + sumstring
        else:
            sumstring = i + sumstring
    end = "$" + "".join([sumstring, b, c])
    if neg: end = "(" + end + ")"
    return end


li = []
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        li.append(line)
except:
    pass
for i in li:
    print(translate(i))

"""
$203,323.00
$0.00
$0.00
$0.00
$3,434,343,434.32
($12,344.10)
($12,345,678.90)
"""


# num = -12345.675656
# print(translate(num))
#
# num2 = 112431423.414124
# print(translate(num2))
#
# num3 = 00010.000000
# print(translate(num3))

# Test File


def is_same(a, b):
    if (a & b) != 0:
        return -1
    else:
        return 1


def main():
    # n = int(input())
    # seq = list(map(int, input().split()))
    n = 4
    seq = [3, 5, 6, 1]
    flag = [0] * n
    print(seq)

    for i in range(n):
        for j in range(n):
            if (is_same(seq[i], seq[j])) == 1:
                flag[i] = flag[j] = 1
    print(flag)
    for i in range(n):
        print(-1 if flag[i] == 0 else 1)  # -1,-1,1,1  ok


main()
