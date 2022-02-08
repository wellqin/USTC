# -*- coding:utf-8 -*-

class A(object):

    def __init__(self, name):
        self.name = name

    def out_object_method(cls):
        print("外部类的方法")

    def test_inner(self):
        print(self)
        print(self.B("B inner_name", self).inner_name)
        print(self.B("B inner_name", self).inner_method())

    class B(object):
        def __init__(self, inner_name, obj):
            self.inner_name = inner_name
            self.obj = obj

        def inner_method(self):
            print("内部类的方法")
            self.obj.out_object_method()


a = A("Join")
b = a.B("July", a)
b.inner_method()
a.test_inner()

