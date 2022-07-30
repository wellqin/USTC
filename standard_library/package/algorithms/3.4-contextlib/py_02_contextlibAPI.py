import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class MyContext:
    def __init__(self):
        print('__init__()')
    # contextlib interface
    def __enter__(self):
        print('__enter__()')
        return self
    # contextlib interface
    def __exit__(self, exec_type, exec_val, exc_tb):
        print('__exit__()')

class WithinContext:
    def __init__(self, context):
        print('WithinContext.__ini__({})'.format(context))
    def do_something(self):
        print('WithinContext.do_something()')
    def __del__(self):
        print('WithinContext.__del__')
class YourContext:
    def __init__(self):
        print('YourContext.__init__()')
    def __enter__(self):
        print('YourContext.__enter__()')
        return WithinContext(self)
    def __exit__(self, *args):
        print('YourContext.__exit__()')

class HerContext:
    def __init__(self, handle_error):
        print('HerContext.__init__({})'.format(handle_error))
        self.handle_error = handle_error
    def __enter__(self):
        print('HerContext.__enter__()')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('HerContext.__exit__()')
        print('     exc_type = ', exc_type)
        print('     exc_val  = ', exc_val)
        print('     exc_tb   = ', exc_tb)
        return self.handle_error


@addBreaker
def contextlib_api():
    with MyContext():
        print('Doing work in the context')
    return

@addBreaker
def contextlib_api_other_object():
    with YourContext() as c:
        c.do_something()

@addBreaker
def contextlib_api_error():
    with HerContext(True):
        raise RuntimeError('error message handled')
    print()
    with HerContext(False):
        raise RuntimeError('error message propagated')

if __name__ == "__main__":
    # interface is easy to impement using data-model methods __enter__(), __exit()
    contextlib_api()
    # __enter__() method can return ANY object to be associated with a name specified 
    # in the **as** clause of the **with** statement.
    contextlib_api_other_object()
    # __exit()__ handles errors
    contextlib_api_error()