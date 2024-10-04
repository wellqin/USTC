import functools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from standard_library.package.algorithms.breaker import addBreaker
def do_reduce(a: int, b: int):
    print('do_reduce({}, {})'.format(a, b))
    return a + b
data = range(1, 5)

@addBreaker
def functools_reduce():
    print('data:', data)
    result = functools.reduce(do_reduce, data)
    print('result: {}'.format(result))

@addBreaker
def functools_reduce_initializer():
    print('data:', data)
    # ! optional initial argument is placed at the front of the sequence
    # ! and processed along with the other items.
    # * means reduce's startpoint is 99 ..
    result = functools.reduce(do_reduce, data, 99)
    print('result: {}'.format(result))

@addBreaker
def functools_reduce_short_sequences():
    # signle element in a seq ..
    print('Single item in sequence:', functools.reduce(do_reduce, [1]))
    # single element in a seq with initializer ..
    print('Single item in sequence with initializer:', functools.reduce(do_reduce, [1], 99))
    # Empty sequence with initializer ..
    print('Empty sequence with initializer:', functools.reduce(do_reduce, [], 99))
    # Empty sequence w/o initializer ..
    try:
        print('Empty sequence:', functools.reduce(do_reduce, []))
    except TypeError as err:
        print('Error: {}'.format(err))


if __name__ == "__main__":
    # functools.reduce() normal usage
    functools_reduce()
    # functools.reduce(callable, seq, initial)
    functools_reduce_initializer()
    # some edge cases
    functools_reduce_short_sequences()