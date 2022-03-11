"""
naturally, objects that implement __enter__() and __exit__() support context manager directly.

some other objects that may implement __enter__(), close() method but not __exit__()
In this situations, using contextlib.closing() to complement close() functionality => __exit__()
the handle is always closed whether there is an error in the `with` statement or not

"""


import contextlib, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class Door:
    def __init__(self):
        print('  __init__()')
        self.status = 'open'
    def close(self):
        print('  close()')
        self.status = 'closed'

@addBreaker
def contextlib_closing():
    print('Normal Example:')
    with contextlib.closing(Door()) as door:
        print('  inside with statement: {}'.format(door.status))
    print('  outside with statement: {}'.format(door.status))

    print('\nError handling example:')
    try:
        with contextlib.closing(Door()) as door:
            print('  raising from inside with statement')
            raise RuntimeError('error massage')
    except Exception as err:
        print('  Had an error:', err)
    return


if __name__ == "__main__":
    contextlib_closing()