# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        爬楼梯
Description :   
Author :          wellqin
date:             2019/9/23
Change Activity:  2019/9/23
-------------------------------------------------
"""

"""
从一些测试案例开始总是好的做法。让我们从小的案例开始，看看能否找到某种规律。
N = 1，1种爬楼方式：[1]
N = 2，2种爬楼方式：[1,1]，[2]
N = 3，3种爬楼方式：[1,2]，[1,1,1]，[2,1]
N = 4，5种爬楼方式：[1,1,2]，[2,2]，[1,2,1]，[1,1,1,1]，[2,1,1]

你有没有注意到什么？请看N = 3时，爬完3阶楼梯的方法数量是3，基于N = 1和N = 2。存在什么关系？
爬完N = 3的两种方法是首先达到N = 1，然后再往上爬2步，或达到N = 2再向上爬1步。所以 f(3) = f(2) + f(1)。
这对N = 4是否成立呢？是的，这也是成立的。因为我们只能在达到第三个台阶然后再爬一步，
或者在到了第二个台阶之后再爬两步这两种方式爬完4个台阶。所以f(4) = f(3) + f(2)。
所以关系如下： f(n) = f(n – 1) + f(n – 2)，且f(1) = 1和f(2) = 2。这就是斐波那契数列。

当然，这很慢（O(2^N)）——我们要做很多重复的计算！通过迭代计算，我们可以更快：
def fibonacci(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b    return a
"""

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))


def fibonacci1(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
        return a
print(fibonacci1(4))











"""
现在，让我们尝试概括我们学到的东西，看看是否可以应用到从集合X中取步数这个要求下的爬楼梯。类似的推理告诉我们，
如果X = {1,3,5}，那么我们的算法应该是f(n) = f(n – 1) + f(n – 3) + f(n – 5)。如果n <0，那么我们应该返回0，因为我们不能爬负数。
"""


def staircase(n, X):
    if n <= 0:
        return 0
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)


X = {1, 3, 5}
print(staircase(8, X))


def fibonacci3(n):
    if n <= 1:
        return 1
    return fibonacci3(n - 1) + fibonacci3(n-3) + fibonacci3(n-5)
print(fibonacci3(8))


def staircase1(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    return cache[-1]