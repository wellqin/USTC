# -*- coding:utf-8 -*-

"""
数据库连接池的设计一般是采用单例模式，因为数据库连接是一种数据库资源。
数据库软件系统中使用数据库连接池，主要是节省打开或者关闭数据库连接所引起的效率损耗，这种效率上的损耗还是非常昂贵的。
使用单例模式来维护连接池，就可以大大降低这种损耗，当需要频繁创建和销毁的对象时单例模式无疑可以提高系统的性能。
"""


def connection_pool(n):
    assert n < 20  # 限制连接池实例数量

    def singleton(cls):
        # 创建一个列表用来保存类的实例对象
        _instance_list = list()

        def _singleton(*args, **kwargs):
            # 先判断这个实例列表有没有实例，即是不是类第一次init
            while len(_instance_list) < n:
                _instance_list.append(cls(*args, **kwargs))
            # 循环返回实例
            _instance_list.insert(0, _instance_list[-1])
            return _instance_list.pop()

        return _singleton

    return singleton


MONGODB_URL = ""
MONGODB_DATABASE = ""


# 将三个连接实例加入连接池中
@connection_pool(3)
class MongodbModule(object):
    def __init__(self, url=MONGODB_URL, db=MONGODB_DATABASE):
        self.my_client = {MONGODB_DATABASE: "hello@example"}
        self.my_db = self.myclient[db]


# 循环返回mongodb的实例
mongo = MongodbModule()
