"""
most context managers operate on one object at a time, 
such as a single file or database handle.
In these cases, the object is known in advance and the code using the context manager can be built around that one object.

In other cases, a program may need to create an unknown number of objects within a context,
with all of these objects expected to be cleaned up when control flow exits the context.
`ExitStack` was created to handle those more dynamic cases.

`ExitStack` maintains a stack data structure of cleanup callbacks.
the callbacks are populated explicitly within the context, 
and any registered callbacks are called in the reverse order when control flow exits the context.

The result is similar to having multiple nested `with` statements,
except they are established dynamically.

"""


import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

### ExitStack is treated as though they appear within a series of nested `with` statements.
@contextlib.contextmanager
def make_context(i):
    print('{} entering'.format(i))
    yield {}
    print('{} exiting'.format(i))

def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            # ExistStack.enter_context(f) first calls __enter__ on the context manager.
            # It then registers its __exit__() as a callback to be invoked as the stack is undone.
            stack.enter_context(make_context(i))
        print(msg)

@addBreaker
def contextlib_exitstack_enter_context():
    variable_stack(2, 'inside context')

### Errors propagate through the normal error handling of the context managers
class Tracker:
    "Base class for noisy context managers."
    def __init__(self, i):
        self.i = i
    def msg(self, s):
        print('  {}({}): {}'.format(self.__class__.__name__, self.i, s))
    def __enter__(self):
        self.msg('entering')

class HandleError(Tracker):
    "If an exception is received, treate it as handled"
    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(exc_details[1]))
        self.msg('exiting {}'.format(received_exc))
        # return a boolean value indicating whether the exception was handled
        return received_exc

class PassError(Tracker):
    "if an exception is received, propagate it"
    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passing exception {!r}'.format(exc_details[1]))
        self.msg('exiting')
        # return False, indicating any exception was not handled
        return False

class ErrorOnExit(Tracker):
    "casue an exception"
    def __exit__(self, *exc_details):
        self.msg('throw error')
        raise RuntimeError('from {}'.format(self.i))

class ErrorOnEnter(Tracker):
    "cause an exception"
    def __enter__(self):
        self.msg('throw error on enter')
        raise RuntimeError('from {}'.format(self.i))
    def __exit__(self, *exc_details):
        self.msg('exiting')

"""

isn't this ExitStack compliated too much?
normal usage of context manager is really necessary in real life?
i have no idea.

P242-P248

"""

if __name__ == "__main__":
    contextlib_exitstack_enter_context()