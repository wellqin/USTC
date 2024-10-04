# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        DictAndSetTheory
Description :   
Author :          wellqin
date:             2020/4/13
Change Activity:  2020/4/13
-------------------------------------------------

1.5、dict和set的实现原理
    dict和list查找元素，dict查找的性能远远大于list，在list中随着list数据的增大查找时间增大，
    在dict中查找元素不会随着数据的增大而增大，dict的实现原理叫做哈希表。
    哈希表的存储逻辑，哈希表的右边是数值的存储结构，是连续的数组，这个数组里存了指向key和value的指针。

哈希表的查找：首先计算dict的键的hash值，然后利用hash值定位数组中的一个表元，此时判断表元是否为空，如果表元为空，直接抛出KeyError，
            如果表元不为空，则判断键是否相等，
                如果相等的话返回表元里的值，
                如果不相等的话，则使用hash值的另一部分来定位hash表的另一行，然后又判断表元是否为空进入下一次判断循环。（哈希冲突的存在）
特性：
    1、dict的key或者set的值都必须是可以hash的(不可变对象，都是可以hash的，str，frozenset，tuple，自己实现的类__hash__都是可以hash的)
    2、dict的内存花销大（表元），但是查询速度快，自定义的对象或者python内部的对象都是用dict包装的
    3、dict的存储顺序和元素添加顺序有关，元素添加过程中的哈希冲突，先来先占位，后来的会按照策略放到另一个位置
    4、添加数据有可能改变已有的数据的顺序，哈希表空间不足时，会重新申请空间并重新分配，rehash造成数据顺序产生变化
"""

from random import randint


def load_list_data(total_nums, target_nums):
    """
    从文件中读取数据，以list的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = []
    target_data = []
    file_name = "fbobject_idnew.txt"
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data.append(line)
            else:
                break

    for x in range(target_nums):
        random_index = randint(0, total_nums)
        if all_data[random_index] not in target_data:
            target_data.append(all_data[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data


def load_dict_data(total_nums, target_nums):
    """
    从文件中读取数据，以dict的方式返回
    :param total_nums: 读取的数量
    :param target_nums: 需要查询的数据的数量
    """
    all_data = {}
    target_data = []
    file_name = "fbobject_idnew.txt"
    with open(file_name, encoding="utf8", mode="r") as f_open:
        for count, line in enumerate(f_open):
            if count < total_nums:
                all_data[line] = 0
            else:
                break
    all_data_list = list(all_data)
    for x in range(target_nums):
        random_index = randint(0, total_nums - 1)
        if all_data_list[random_index] not in target_data:
            target_data.append(all_data_list[random_index])
            if len(target_data) == target_nums:
                break

    return all_data, target_data


def find_test(all_data, target_data):
    # 测试运行时间
    test_times = 100
    total_times = 0
    import time
    for i in range(test_times):
        find = 0
        start_time = time.time()
        for data in target_data:
            if data in all_data:
                find += 1
        last_time = time.time() - start_time
        total_times += last_time
    return total_times / test_times


if __name__ == "__main__":
    all_data, target_data = load_list_data(10000, 1000)
    # all_data, target_data = load_list_data(100000, 1000)
    # all_data, target_data = load_list_data(1000000, 1000)

    # all_data, target_data = load_dict_data(10000, 1000)
    # all_data, target_data = load_dict_data(100000, 1000)
    # all_data, target_data = load_dict_data(1000000, 1000)
    last_time = find_test(all_data, target_data)
    print(last_time)
