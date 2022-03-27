import inspect

from open_source.eventbus.eventbus_souce import subscribe
from open_source.eventbus.eventbus_souce.subscriber_method import SubscriberMethod

"""
getmembers(object, predicate=None) 方法 在 inspect 模块中，第二个参数就是过滤的条件
getmembers(object, predicate=None) 方法可以提取 object 对象中的所有成员，重新组织成((成员1名, 成员1值), (成员2名, 成员2值), …) 
的形式返回，predicate 参数是一个判断方法，如果 predicate 不为 None，那么只返回通过 predicate 判断的成员。

"""


class Finder:

    def find(self, subscriber):
        return self._find_by_reflect(subscriber)

    @staticmethod
    def _find_by_reflect(subscriber):
        subscriber_methods = []

        methods = inspect.getmembers(subscriber, predicate=inspect.ismethod)
        for name, method in methods:
            annotation = getattr(method, subscribe.subscribe_annotation_property, None)
            if annotation is None:
                continue
            assert len(method.__annotations__) == 1, '订阅方法参数不合法'
            event_type = list(method.__annotations__.values())[0]
            subscriber_method = SubscriberMethod(method.__func__, event_type,
                                                 priority=annotation.priority, sticky=annotation.sticky)
            subscriber_methods.append(subscriber_method)

        return subscriber_methods
