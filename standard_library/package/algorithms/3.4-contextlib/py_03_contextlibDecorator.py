"""
one difference that arises when using the context manager as a decorator
is that the value return by __enter__() is not available inside the function be decorated, 
unlike the case when `with` and `as` are used.

arguments passed to the decorated fucntion are available in the usual way.

"""


import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

# context manager supports class
class MyContext(contextlib.ContextDecorator):
    def __init__(self, how_used):
        self.how_used = how_used
        print('MyContext.__init__({})'.format(how_used))
    def __enter__(self):
        print('MyContext.__enter__({})'.format(self.how_used))
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('MyContext.__exit__({})'.format(self.how_used))

# context manager supprots function
@MyContext('as decorator')
def func(message):
    print(message)

@addBreaker
def contextlib_decorator():
    print()
    with MyContext('as context manager'):
        print('Doing work in the context')
    print()
    func('Doing work in the wrapped function')
    return

if __name__ == "__main__":
    contextlib_decorator()