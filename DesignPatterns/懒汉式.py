# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        懒汉式
Description :   
Author :          wellqin
date:             2019/9/23
Change Activity:  2019/9/23
-------------------------------------------------
"""
# -*- coding: utf-8 -*-


# class Singleton(object):
#
#     # 定义静态变量实例
#     __singleton = None
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_instance():
#         if Singleton.__singleton is None:
#             Singleton.__singleton = Singleton()
#         return Singleton.__singleton
#
# if __name__ == "__main__":
#     instance1 = Singleton.get_instance()
#     instance2 = Singleton.get_instance()
#
#     print (id(instance1))
#     print (id(instance2))

# -*- coding: utf-8 -*-
# from MyThread import *
import threading

Lock = threading.Lock()


class Singleton(object):

    # 定义静态变量实例
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            try:
                Lock.acquire()
                # double check
                if not cls.__instance:
                    cls.__instance = super().__new__(cls)
            finally:
                Lock.release()
        return cls.__instance


def test_singleton_in_thread():
    print(id(Singleton()))


if __name__ == "__main__":
    idx = 0
    while 1:
        t = threading.Thread(target=test_singleton_in_thread)
        t.start()
        # MyThread(test_singleton_in_thread, []).start()
        idx += 1
        if idx > 10:
            break
