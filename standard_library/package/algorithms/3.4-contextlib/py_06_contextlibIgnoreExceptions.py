"""
it is frequently useful to ignore exceptions raised by libraries.
because the error indicates that desired state has already been achieved or can otherwise be ignored.

- the most common way to ignore exceptions is with `try:except` statement that includes only a `pass` statement in the except block
- replace `try:except` with `contextlib.suppress()` 
  to more explictly suppress a class of exceptions happening anywhere within `with` block

"""

import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class NotFatalError(Exception):
    pass

def non_idempotent_operation():
    raise NotFatalError(
        'The operation failed because of existing state'
)

@addBreaker
def contextlib_ignore_error():
    try:
        print('trying non-idempotent operation')
        non_idempotent_operation()
        print('succeed!')
    except NotFatalError:
        pass
    print('Done')

@addBreaker
def contextlib_suppress():
    with contextlib.suppress(NotFatalError):
        print('trying non-idempotent oepration')
        non_idempotent_operation()
        print('succeeded!')
    print('Done')

if __name__ == "__main__":
    # try:except
    contextlib_ignore_error()
    # contextlib.suppress
    contextlib_suppress()