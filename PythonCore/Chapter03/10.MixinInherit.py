# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        10.MixinInherit
Description :   
Author :          wellqin
date:             2020/4/11
Change Activity:  2020/4/11
-------------------------------------------------
Python支持多继承，但是一般用的少，不然容易混乱，最好用mixin继承方式

2.0、mixin掺杂继承案例----django-rest-framework
mixin模式特点：
    1、Mixin类功能单一
    2、不和基类关联（mixin只是定义一个方法（接口）），可以和任一基类组合、基类可以不和mixin组合就能初始化成功
    3、在mixin中不要使用super的用法
    4、设置mixin的时候尽量以Mixin结尾，这样别人就可以读懂代码（规范）
接下来展示的代码就是Django-REST-Framework的Mixins的设计模式(Mixin源代码)：
"""
# from rest_framework import status, mixins, viewsets
# from rest_framework.response import Response
# from rest_framework.settings import api_settings

"""
Basic building blocks for generic class based views.

We don't bind behaviour to http method handlers yet,
which allows mixin classes to be composed in interesting ways.
"""

"""
class CreateModelMixin:
    # Create a model instance.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ListModelMixin:
    # List a queryset.
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveModelMixin:
    # Retrieve a model instance.
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UpdateModelMixin:

    # Update a model instance.


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin:

    #Destroy a model instance.


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
"""

# class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     # 商品列表页 分页 搜索 过滤 排序
#
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsSetPagination
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     # 这是精确搜索过滤，我们需要的是模糊搜索
#     # filterset_fields = ['name', 'shop_price']
#     filter_class = GoodsFilter
#     search_fields = ("name", "goods_brief", "goods_desc")
#     ordering_fields = ("shop_price", "sold_num", "add_time")

'''
python 对于 mixin 命名方式一般以 MixIn, able, ible 为后缀。

由于 mixin 是组合，因而是做加法，为已有的类添加新功能，而不像继承一样,下一级会覆盖上一级相同的属性或方法。
但在某些方面仍然表现得与继承一样， 例如类的实例也是每个 mixin 的实例。
mixin 使用不当会导致类的命名空间污 染，所以要尽量避免 mixin 中定义相同方法。
对于相同的方法，有时很难区分 实例到底使用的是哪个方法。
'''


class Mixin1(object):
    def test(self):
        print("mixin 1")

    def which_test(self):
        self.test()


class Mixin2(object):
    def test(self):
        print("mixin 2")


class MyClass1(Mixin1, Mixin2):
    pass  # 按从左到右顺序从 mixin 中获取功能并添加到 MyClass


class Myclass2(Mixin1, Mixin2):
    def test(self):  # 已有 test 方法，因而不会再添加 Mixin1, Mixin2 的 test 方法
        print("my class 2")  # c2.which_test()中self.test()调用的也是这里，而不是父类Mixin1中的test()


c1 = MyClass1()
c1.test()  # "mixin 1"
c2 = Myclass2()
c2.test()  # "my class 2"

c2.which_test()  # "my class 2"
isinstance(c1, Mixin1)  # True
issubclass(MyClass1, Mixin2)  # True
