import itertools
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from standard_library.package.algorithms.breaker import addBreaker


@addBreaker
def itertools_count():
    for i in zip(itertools.count(1), list('abc')):
        print(i)


@addBreaker
def itertools_count_step():
    import fractions
    start = fractions.Fraction(1, 3)
    step = fractions.Fraction(1, 3)
    for i in zip(itertools.count(start, step), list('abcde')):
        print('{}: {}'.format(*i))


@addBreaker
def itertools_cycle():
    for i in zip(range(7), itertools.cycle(list('abc'))):
        print(i)


@addBreaker
def itertools_repeat():
    for i in itertools.repeat('over-and-over', 5):
        print(i)


@addBreaker
def itertools_repeat_with_zip():
    """it is useful to combine repeat() with zip() or map() 
    when **invariant** values should be included with the values from the other iterators
    """
    for i, s in zip(itertools.count(), itertools.repeat('over-and-over', 5)):
        print(i, s)


@addBreaker
def itertools_repeat_with_map():
    # ehh, isn't this numpy.product?
    for i in map(lambda x, y: (x, y, x * y), itertools.repeat(2), range(5)):
        print('{:d} * {:d} = {:d}'.format(*i))


if __name__ == "__main__":
    # auto generate new values by using itertools.count() by default arguments
    itertools_count()
    # user-defined arguments, start, step
    itertools_count_step()
    # cycle()
    itertools_cycle()
    # repeat()
    itertools_repeat()
    # practical usage of count() + repeat() + zip()
    itertools_repeat_with_zip()
    # practial usage of map() + repeat()
    itertools_repeat_with_map()
