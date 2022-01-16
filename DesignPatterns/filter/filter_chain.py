# -*- coding:utf-8 -*-

import abc
from typing import List

"""
拦截过滤器模式（Intercepting Filter Pattern）用于对应用程序的请求或响应做一些预处理/后处理。
定义过滤器，并在把请求传给实际目标应用程序之前应用在请求上。过滤器可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序。
以下是这种设计模式的实体。
"""


class AbstractFilter(abc.ABC):
    @abc.abstractmethod
    def execute(self, request: List[str]): ...


class AuthenticationFilter(AbstractFilter):
    def execute(self, request: List[str]):
        print(f"Authenticating request: {request}")
        return [r for r in request if r == "Authentication"]


class DebugFilter(AbstractFilter):
    def execute(self, request: List[str]):
        print(f"DebugFilter request: {request}")
        return [r for r in request if r == "Debug"]


class Target:
    """Target 对象是请求处理程序"""
    @staticmethod
    def execute(request: List[str]):
        print(f"Target Executing request: {request}")
        return request + ["Target"]


class FilterChain:
    """过滤器链带有多个过滤器，并在 Target 上按照定义的顺序执行这些过滤器。"""
    def __init__(self, builder=None):
        self.filters = []
        self.filter_chain_builder = getattr(builder, "chain", [])
        self.target = None

    class FilterChainBuilder:
        def __init__(self):
            self.chain = []

        def add_filter(self, fi: AbstractFilter):
            self.chain.append(fi)
            return self

        def build(self):
            return FilterChain(self)

    def add_filter(self, fi: AbstractFilter):
        self.filters.append(fi)

    def extend_filter(self, fi_chain: List[AbstractFilter]):
        self.filters.extend(fi_chain)

    def build_filter(self, fi: AbstractFilter):
        self.filters = self.FilterChainBuilder().add_filter(fi).build().filter_chain_builder

    def execute(self, request: str):
        # 1、处理前，过滤器可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序
        # test2有而test1没有的元素: list(set(test2).difference(set(test1)))
        for fi in self.filters:
            request = list(set(request).difference(set(fi.execute(request))))
        # 2、真正去处理逻辑
        return self.target.execute(request)

    def set_target(self, target: Target):
        self.target = target


class FilterManager:

    def __init__(self, target: Target):
        self.filter_chain = FilterChain()
        self.filter_chain.set_target(target)

    def set_filter(self, fi: AbstractFilter):
        self.filter_chain.add_filter(fi)

    def set_filter_chain(self, fi_chain: List[AbstractFilter]):
        self.filter_chain.extend_filter(fi_chain)

    def set_build_filter(self, fi: AbstractFilter):
        self.filter_chain.build_filter(fi)

    def filter_request(self, request: str):
        return self.filter_chain.execute(request)


class Client:

    def __init__(self):
        self.filter_manager = None

    def set_filter_manager(self, fi_manager: FilterManager):
        self.filter_manager = fi_manager

    def send_request(self, request: List[str]):
        return self.filter_manager.filter_request(request)


if __name__ == "__main__":
    filter_manager = FilterManager(Target())
    # 1、过滤器链： 也可以使用建造者模式创建
    filter_manager.set_build_filter(AuthenticationFilter())

    # 2、一口气加载全部过滤器接口子类, __subclasses__这个方法返回的是这个类的子类的集合
    # sub_class_list = AbstractFilter.__subclasses__()
    # filter_manager.set_filter_chain([sub() for sub in sub_class_list])

    # 3、依次加入每个过滤器接口子类
    # filter_manager.set_filter(AuthenticationFilter())
    # filter_manager.set_filter(DebugFilter())

    client = Client()
    client.set_filter_manager(filter_manager)
    res = client.send_request(["HOME", "hello", "Authentication", "Debug"])
    print(res)
