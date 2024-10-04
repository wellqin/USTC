#假设有这么一个类： 
#
# class ZeroEvenOdd {
#  public ZeroEvenOdd(int n) { ... }      // 构造函数
#  public void zero(printNumber) { ... }  // 仅打印出 0
#  public void even(printNumber) { ... }  // 仅打印出 偶数
#  public void odd(printNumber) { ... }   // 仅打印出 奇数
#}
# 
#
# 相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程： 
#
# 
# 线程 A 将调用 zero()，它只输出 0 。 
# 线程 B 将调用 even()，它只输出偶数。 
# 线程 C 将调用 odd()，它只输出奇数。 
# 
#
# 每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。 
#
# 
#
# 示例 1： 
#
# 输入：n = 2
#输出："0102"
#说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
# 
#
# 示例 2： 
#
# 输入：n = 5
#输出："0102030405"
# 
#python + 条件变量 + 一把锁 + notify_all()
"""

最后结果2n个数，其中n个0.

多少个奇数呢？自己写写就能推理出来 (self.n+1)//2
然后剩下的是偶数: self.n - (self.n+1)//2
最后的问题：什么时候输出偶数，什么时候输出奇数： 输出数字01020304 index 01234567
对比你会发现 被4除余数为3的位置输出偶数，余数为1的位置输出奇数


"""

from threading import Lock, Condition


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.num = 0
        self.cv = Condition()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        for i in range(self.n):
            with self.cv:
                while self.num % 2 != 0:
                    self.cv.wait()
                printNumber(0)
                self.num += 1
                self.cv.notify_all()

    def even(self, printNumber):
        for i in range(self.n - (self.n + 1) // 2):
            with self.cv:
                while self.num % 4 != 3:
                    self.cv.wait()
                printNumber((self.num + 1) // 2)
                self.num += 1
                self.cv.notify_all()

    def odd(self, printNumber):
        for i in range((self.n + 1) // 2):
            with self.cv:
                while self.num % 4 != 1:
                    self.cv.wait()
                printNumber((self.num + 1) // 2)
                self.num += 1
                self.cv.notify_all()

ss = ZeroEvenOdd(5)
ss.zero()
ss.even()
ss.odd()
