"""

traditional way -- that is, by writing a class with __enter__() and __exit__() methods -- is not difficult

Nevertheless, writing everything out fully creates extra overhead 
when only a trivial bit of context is being mananged.

In those sorts of situations, the best approach is to use the contextmanager() decorator to
convert a generator function into a context manager

aha, there are two approaches to use contextmanager as decorator.

:: approach 01
@contextlib.contextmanager
def f(*args, **kwargs):
    try:
        yield {} # ! actually yield somethign
    except RuntimeError as err:
        # do sth
    finally:
        # exit

+++

with f() as value:
    # do sth

with f() as value:
    # do sth

with f() as value:
    # do sth

:: approach 02
@contextlib.contextmanager
def f(*args, **kwargs):
    try:
        yield   # ! just yield only, it returns control to who call this generator. "interleave" concept, remember?
    except RuntimeError as err:
        # do sth
    finally:
        # exit

+++

@f()
def usage1():
    # do sth
@f()
def usage2():
    # do sth
@f()
def usage3():
    # do sth


"""
import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@contextlib.contextmanager # is derived from ContextDecorator
def make_context():
    print('  entering')
    try:
        # initializes the context, and invokes `yield` exactly one time
        yield {}    # the value yielded, if any, is bound to the variable in the `as` clause of the `with` statement
    except RuntimeError as err:
        # exceptions from the `with` block are raised again inside the generator, 
        # so they can be handled here
        print('  ERROR:', err)
    finally:
        print('  exiting')  # clean up the context

@addBreaker
def contextlib_contextmanager_mechnism():
    print('Normal:')
    with make_context() as value:
        print('  inside with statement:', value)

    print('\nHandled error:')
    with make_context() as value:
        raise RuntimeError('showing example of handling an error')

    print('\nUnhandled error:')
    with make_context() as value:
        raise ValueError('this exception is not handle')

@contextlib.contextmanager
def dec_make_context():
    print('  entering')
    try:
        # Yield control, but not a value, because any value
        # yielded is not available when the contextmanager 
        # is used as a decorator.  
        yield
    except RuntimeError as err:
        print('  Error:', err)
    finally:
        print('  exiting')

@dec_make_context()
def normal():
    print('  inside with statement')
@dec_make_context()
def throw_error(err):
    raise err

@addBreaker
def contextlib_contextmanager_decorator():
    print('Normal:')
    normal()
    print('\nHandled error:')
    throw_error(RuntimeError('showing example of handling an error'))
    print('\nUnhandled error:')
    throw_error(ValueError('this exception is not handled'))



if __name__ == "__main__":
    contextlib_contextmanager_mechnism()