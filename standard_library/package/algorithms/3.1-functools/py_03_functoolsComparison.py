import functools
import inspect
import os
import pprint
import sys

from standard_library.package.algorithms.breaker import addBreaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print(' testing __eq__({}, {})'.format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print(' testing __gt__({}, {})'.format(self.val, other.val))
        return self.val > other.val


### functool.cmp_to_key()
class CompObj:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'MyObj({})'.format(self.val)


def compare_obj(a: CompObj, b: CompObj):
    """old-style comparison function
    """
    print('comparing {} and {}'.format(a, b))
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    else:
        return 0


@addBreaker
def functools_total_ordering():
    print('Method:\n')
    # inspect.getmembers(), inspect.isfunction() checks if object is a function
    pprint.pprint(inspect.getmembers(MyObject, inspect.isfunction))
    a = MyObject(1)
    b = MyObject(2)
    print('\nComparison:')
    for expr in ['a < b', 'a <= b', 'a == b', 'a >= b', 'a > b']:
        print('\n{:<6}:'.format(expr))
        result = eval(expr)
        print(' result of {}: {}'.format(expr, result))


@addBreaker
def functools_cmp_to_key():
    """cmp is deprecated, 
    cm_to_key() converts comparison functions to a function that returns a **collation key**
    """
    # make a key function using cmp_to_keY(). 
    # It means convert cmp function to key literally
    get_key = functools.cmp_to_key(compare_obj)

    def get_key_wrapper(o):
        """wrapper function for get_key to allow for print statements
        """
        new_key = get_key(o)
        print('key_wrapper({} -> {!r})'.format(o, new_key))
        return new_key

    objs = [CompObj(n) for n in range(5, 0, -1)]
    for o in sorted(objs, key=get_key_wrapper):
        print(o)


if __name__ == "__main__":
    # total_ordering
    functools_total_ordering()
    # cmp_to_key
    functools_cmp_to_key()
