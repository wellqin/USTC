import functools
import os
import sys
from typing import Any

from standard_library.package.algorithms.breaker import addBreaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


### function overload
@functools.singledispatch
def myfunc(arg: Any):
    print('default myfunc({!r})'.format(arg))


@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    print('myrfunc_list()')
    for item in arg:
        print(' {}'.format(item))


### class mro
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


@functools.singledispatch
def clsMyFunc(arg: Any):
    print('default clsMyFunc({})'.format(arg.__class__.__name__))


@clsMyFunc.register(A)
def clsMyFunc_A(arg):
    print('clsMyFunc_A({})'.format(arg.__class__.__name__))


@clsMyFunc.register(B)
def clsMyFunc_B(arg):
    print('clsMyFunc_B({})'.format(arg.__class__.__name__))


@clsMyFunc.register(C)
def clsMyFunc_C(arg):
    print('clsMyFunc_C({})'.format(arg.__class__.__name__))


@addBreaker
def functools_singledispatch():
    myfunc('string argument')
    myfunc(1)
    myfunc(2.3)
    myfunc(list('abc'))


@addBreaker
def functools_singledispatch_mro():
    # ! when NO extact match is found for the type, 
    # ! the inheritance order is evaluted and the closest matching type is used
    clsMyFunc(A())
    clsMyFunc(B())
    clsMyFunc(C())
    clsMyFunc(D())
    clsMyFunc(E())


if __name__ == "__main__":
    # using signledispatch to perform function overload
    functools_singledispatch()
    # proximity, Python>=3.x
    functools_singledispatch_mro()
