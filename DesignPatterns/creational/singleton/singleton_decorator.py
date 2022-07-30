# -*- coding:utf-8 -*-


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    """
    装饰器解析
    A = singleton(A) -> 此步骤返回了_singleton这个函数
    """
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    a1 = A(2)
    a2 = A(3)
    print(id(a1), id(a2))

