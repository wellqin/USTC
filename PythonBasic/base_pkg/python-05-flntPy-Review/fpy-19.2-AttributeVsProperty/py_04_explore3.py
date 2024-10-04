from collections import abc
import keyword

class FrozenJSON:
    """a read-only interface, using property expression to access JSON object
    """
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
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
            return FrozenJSON(self.__data[name])

if __name__ == "__main__":
    x = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    print(x.name)
    print(x.class_)
    # print(keyword.kwlist)