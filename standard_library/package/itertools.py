# -*- coding:utf-8 -*-
# itertools - 为高效循环而创建迭代器的函数

"""一、无穷迭代器：count、cycle、repeat"""

# 1、itertools.count(start=0, step=1)
# 创建一个迭代器，它从 start 值开始，返回均匀间隔的值。常用于 map() 中的实参来生成连续的数据点。此外，还用于 zip() 来添加序列号

# count()会创建一个无限的迭代器，停不下来
natuals = itertools.count(1)
for n in natuals:
    print(n)

# cycle()会把传入的一个序列无限地循环下去，同样停不下来
# cs = itertools.cycle('ABC')
# for c in cs:
#     print c

# repeat()可以把一个元素无限重复下去，不过如果指定第二个参数就可以限定重复的次数
# ns = itertools.repeat('A', 10)
# for n in ns:
#     print n

# 可以通过takewhile()等函数根据条件判断来截取出一个有限的序列
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# for n in ns:
#     print n

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain('ABC', 'XYZ'):
#     print c

# groupby()把迭代器中相邻的重复元素挑出来放在一起
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print key, list(group)
# 可以忽略大小写
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print key, list(group)

# imap()可以作用于无穷序列，如果两个序列的长度不一致，以短的为准
# for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
#     print x
# map()返回list，调用map()时，已经计算完毕
# r = map(lambda x: x * x, [1, 2, 3])
# print r
# imap()返回一个迭代对象，当调用imap()时，并没有进行计算
# r2 = itertools.imap(lambda x : x * x, [1, 2, 3])
# print r2
# for x in r2:
#     print x
# imap()实现了“惰性计算”，在需要获得结果的时候才计算
# r = itertools.imap(lambda x: x * x, itertools.count(1))
# for n in itertools.takewhile(lambda x: x < 100, r):
#     print n
# 换成map()呢？停不下来
# r = map(lambda x: x * x, itertools.count(1))
# print r

