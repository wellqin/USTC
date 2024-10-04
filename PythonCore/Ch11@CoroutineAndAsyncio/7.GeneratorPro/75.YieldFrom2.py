# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        75.YieldFrom2
Description :   
Author :          wellqin
date:             2020/4/19
Change Activity:  2020/4/19
-------------------------------------------------
最重要的用法：双向通道

main调用方
g1:委托生成器  作用：省去了子生成器yield的异常处理
gen:子生成器
"""


def g1(gener):  # g1:委托生成器
    yield from gener


gen = range(10)  # gen:子生成器


def main():  # main调用方
    g = g1(gen)
    # 直接发送给子生成器
    print(g.send(None))


# yield from会在调用方与子生成器之间建立一个双向通道
# main调用方 <-->     委托生成器    <--> 子生成器
# main()    <--> yield from gen  <--> range(10)
main()  # 0
print("======================================================================")

# 看一个例子
final_result = {}


# 子生成器
def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量: ", x)
        if not x:  # 如果传入的x为None，则break
            break
        total += x
        nums.append(x)
    # 直接返回到yield from sales_sum(key)
    return total, nums


# 委托生成器
def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！！.")


# 调用方
def main():
    data_sets = {
        "面膜": [1200, 1500, 3000],
        "手机": [28, 55, 98, 108],
        "大衣": [280, 560, 778, 70],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        # 直接send到子生成器里面（x = yield）
        m.send(None)  # 预激middle协程，则运行到yield from sales_sum(key)

        for value in data_set:
            m.send(value)  # 给协程传递每一组的值[1200, 1500, 3000]...通过委托生成器发给子生成器
        m.send(None)  # 数据传完后，send(None)会使得子生成器while循环结束，return total, nums给yield from sales_sum(key)
    print("final_result:", final_result)


# 看一下无yield from，需要自己处理异常。
def sales_sum1(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    # 直接返回到yield from sales_sum(key)
    return total, nums


# 直接与子生成器通信（没用yield from就需要捕获异常）
my_gen = sales_sum1("手机")
my_gen.send(None)
my_gen.send(1200)
my_gen.send(1500)
my_gen.send(3000)
try:
    my_gen.send(None)  # 不加异常处理会报错StopIteration
# 获取返回值
except StopIteration as e:
    result = e.value
    print(result)
print("======================================================================")


if __name__ == '__main__':
    main()
    """
    start key: 手机
    手机销量:  28
    手机销量:  55
    手机销量:  98
    手机销量:  108
    手机销量:  None   # 子生成器break
    手机销量统计完成！！.
    start key: 面膜
    面膜销量:  1200
    面膜销量:  1500
    面膜销量:  3000
    面膜销量:  None
    面膜销量统计完成！！.
    start key: 大衣
    大衣销量:  280
    大衣销量:  560
    大衣销量:  778
    大衣销量:  70
    大衣销量:  None
    大衣销量统计完成！！.
    final_result: {'手机': (289, [28, 55, 98, 108]), '面膜': (5700, [1200, 1500, 3000]), 
                    '大衣': (1688, [280, 560, 778, 70])}

    """
