#coding=utf-8
"""
python的thread模块是⽐较底层的模块，python的threading
模块是对thread做了⼀些包装的，可以更加⽅便的被使⽤
"""

# 1. 使⽤threading模块

# 单线程执⾏ == 一条条显示

import time


# def saySorry():
#     print("亲爱的，我错了，我能吃饭了吗？")
#     time.sleep(1)
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         saySorry()


# 多线程执⾏ == 一起显示
import threading

def saySorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()  # 启动线程，即让线程开始执⾏

"""
1. 可以明显看出使⽤了多线程并发的操作，花费时间要短很多
2. 创建好的线程，需要调⽤ start()  ⽅法来启动
"""