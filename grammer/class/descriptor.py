# -*- coding:utf-8 -*-

class Des(object):
    def __init__(self, init_value):
        self.value = init_value

    def __get__(self, instance, typ):
        print('call __get__', instance, typ)
        return self.value

    def __set__(self, instance, value):
        print('call __set__', instance, value)
        self.value = value

    def __delete__(self, instance):
        print('call __delete__', instance)


class Widget(object):
    t = Des(1)


def main():
    w = Widget()
    print(type(w.t))
    w.t = 1
    print(w.t, Widget.t)
    del w.t


if __name__ == '__main__':
    main()
