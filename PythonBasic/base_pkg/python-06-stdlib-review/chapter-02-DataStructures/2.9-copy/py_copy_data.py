import functools
@functools.total_ordering
class MyClass:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            raise NotImplementedError
    def __gt__(self, other):
        try:
            return self.name > other.name
        except AttributeError:
            raise NotImplementedError