# li = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
#
#
# def func(nums):
#     if not nums:
#         return 0
#     lookup = {}
#     for i in range(len(nums)):
#         lookup[nums[i]] = lookup.get(nums[i], 0) + 1
#     # return sorted(lookup, key=lambda x: lookup[x])[-1]
#     res = sorted(lookup.items(), key=lambda x: x[1])[-1]
#     return list(res)[0]
#
#
# print(func(li))


# def g():
#     print("1 is")
#     yield 1
#     print("2 is")
#     yield 2
#     print("3 is")
#     yield 3
#
#
# z = g()
# print(z)
# print(next(z))
# print(next(z))
# print(next(z))
#
# print(next(z))  # 异常


import datetime as dt
from time import sleep


def log_time(msg, time=dt.datetime.now()):
    sleep(1)  # 线程暂停一秒
    print("%s: %s" % (time.isoformat(), msg))


log_time('msg 1')
log_time('msg 2')
log_time('msg 3')
