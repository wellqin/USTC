from collections import abc
import keyword

class FrozenJSON:
    """a read-only interface, using property expression to access JSON object
    """
    def __init__(self, mapping):
        self.__data = dict()
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.__data[k] = v
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
    x = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    print(x.name)
    print(x.class_)