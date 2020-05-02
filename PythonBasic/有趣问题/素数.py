"""
-------------------------------------------------
File Name:        素数
Author :          wellqin
date:             2020/5/2
-------------------------------------------------
"""


# Test File
# 用filter求素数

# 生成器，生成一个无限序列


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数：这个函数接受一个参数 x, 返回 x % n > 0。
def _not_divisible(n):  # 调用 _not_divisible(n) 后返回的是一个能过滤掉能被 n 整除的数，留下不能被 n 整除的数的函数
    ll = lambda x: x % n > 0  # it是一个生成器对象，而filter每次会得到一个由它生成的值。所以x指的不是it，只是it产生的一个值。
    return ll  # x为每次最新的生成器pop数，n为it迭代器中的所有素数结果


# 生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数,此时next后，会生成最新的_odd_iter值，接着立马调用真正的filter逻辑
        yield n
        it = filter(_not_divisible(n), it)  # 在没有最新的next n值时，这里只是获取了lambda返回函数，逻辑还未执行
        # it每次都在变化，里面是符合素数标准的3 5 7 11 13 17 19 23


# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件
# 打印1000以内的素数
for n in primes():
    if n < 40:
        # print(n)
        pass
    else:
        break
