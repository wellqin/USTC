import functools
import os
import sys
from standard_library.package.algorithms.breaker import addBreaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def myfunc(a, b=2):
    """Docstring for myfunc()"""
    print(' called my function with:', (a, b))


def show_details(name: str, f: callable, is_partial=False):
    """show details of a callable object"""
    print('{}:'.format(name))
    print(' object:', f)
    if not is_partial:
        print(' __name__:', f.__name__)
    if is_partial:
        print(' func:', f.func)
        print(' args:', f.args)
        print(' keywords:', f.keywords)
    return


def show_details2(name: str, f: callable):
    """show details of a callable object"""
    print('{}:'.format(name))
    print(' object:', f)
    print(' __name__:', end='')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print(' __doc__', repr(f.__doc__))
    print()


@addBreaker
def functools_partial():
    # set default value for b only
    show_details('myfunc', myfunc)
    myfunc('a', 3)
    print()
    # currying 
    p1 = functools.partial(myfunc, b=4)
    show_details('partial with named default', p1, True)
    p1('passing a')
    p1('override b', b=5)
    print()
    # set default values for both a and b
    p2 = functools.partial(myfunc, 'default a', b=99)
    show_details('partial with defaults', p2, True)
    p2()
    p2(b='override b')
    print()
    print('Insuffient argumetns:')
    p1()


@addBreaker
def functools_update_wrapper():
    show_details2('myfunc', myfunc)
    p1 = functools.partial(myfunc, b=4)
    show_details2('raw wrapper', p1)

    print('Updating wrapper:')
    # myfunc is base, p1 is a wrapped myfunc. 
    # so, using update(p1, myfunc) means to check any difference from the base
    # also, attributes added to the wrapper are defined in **WRAPPER_ASSIGNMENTS**
    # **WRAPPER_UPDATES** lists values to be modified
    print('assign:', functools.update_wrapper(p1, myfunc))
    show_details2('updated wrapper', p1)


@addBreaker
def functools_callable():
    class MyClass:
        """Demonstration class for functools"""

        def __call__(self, e, f=6):
            """Docstring for MyClass.__call__"""
            print(' called object with:', (self, e, f))

    o = MyClass()
    show_details2('instance', o)
    o('e goes here')
    print()
    # functools.partial(f,)
    p = functools.partial(o, e='default for e', f=8)
    functools.update_wrapper(p, o)
    show_details2('instance wrapper', p)
    p()


@addBreaker
def functools_partialmethod_vs_partial():
    def standalone(self, a=1, b=2):
        """standalone function"""
        print(' called standalone with:', (self, a, b))
        if self is not None:
            print(' self.attr=', self.attr)

    class MyClass:
        def __init__(self):
            self.attr = 'instance attribute'

        # partialmethod is binding a standalone function with MyClass..
        method1 = functools.partialmethod(standalone)
        # partial can't do it
        method2 = functools.partial(standalone)

    o = MyClass()
    print('standalone')
    standalone(None)
    print()
    print('method1 as functools.partialmethod')
    o.method1()
    print()
    print('method2 as functools.partial')
    try:
        o.method2()
    except TypeError as err:
        print('Error: {}'.format(err))


@addBreaker
def functools_wraps():
    def simple_decorator(f):
        # wraps(f) is to apply update_wrapper() to the decorated function
        @functools.wraps(f)
        def decorated(a='decorated defaults', b=1):
            print(' decorated:', (a, b))
            print(' ', end=' ')
            return f(a, b=b)

        return decorated

    # raw function
    show_details2('myfunc', myfunc)
    myfunc('unwrapped, default b')
    myfunc('unwrapped, passing b', 3)
    print()
    # wrapped explicitly
    wrapped_myfunc = simple_decorator(myfunc)
    show_details2('wrapped_myfunc', wrapped_myfunc)
    wrapped_myfunc()
    wrapped_myfunc('args to wrapped', 4)
    print()

    # wrapped with decorator syntax
    @simple_decorator
    def decorated_myfunc(a, b):
        myfunc(a, b)
        return

    show_details2('decorated_myfunc', decorated_myfunc)
    decorated_myfunc()
    decorated_myfunc('args to decorated', 4)


if __name__ == "__main__":
    # functools_partial()
    # using functools.update_wrapper() to do update ..
    # functools_update_wrapper()
    # Python is protocol lang so class could be callable too via implementing __call__ dunder method
    # functools_callable()
    # functools.partialmethod() vs functools.partial()
    # functools_partialmethod_vs_partial()
    # decorator
    functools_wraps()
