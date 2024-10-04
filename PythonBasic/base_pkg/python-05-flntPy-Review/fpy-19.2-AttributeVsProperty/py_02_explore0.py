from collections import abc

class FrozenJSON:
    """a read-only interface, using property expression to access JSON object
    """
    def __init__(self, mapping):
        self.__data = dict(mapping)
    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

if __name__ == "__main__":
    from py_01_osconfeed import load
    feed = FrozenJSON(load())
    print(len(feed.Schedule.speakers))
    print(sorted(feed.Schedule.keys()))
    for k, v in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(v), k))
    