import itertools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from typing import Tuple

def times_two(x: int) -> int:
    return 2 * x
def multiply(x: int, y: int) -> Tuple[int, int, int]:
    return (x, y, x * y)

@addBreaker
def itertools_map_vs_starmap():
    """
    map(): return an iterator that calls a function on the values in the input iterators 
           and return the results(Tuple).

    itertools.starmap():
    """
    print('\n{:-^30}'.format('built-in map function'))
    print('Doubles:')
    for i in map(times_two, range(5)):
        print(i)
    print('\nMultiples:')
    r1 = range(5)
    r2 = range(5, 10)
    for i in map(multiply, r1, r2):
        print('{:d} * {:d} = {:d}'.format(*i))
    print('\nStopping:')
    r1 = range(5)
    r2 = range(2)
    # ! input data structure is different
    for i in map(multiply, r1, r2): # an iterator contains tuples
        print(i)

    print('\n{:-^30}'.format('itertools.starmap function'))
    # ! input data structure is different
    values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    for i in itertools.starmap(lambda x, y: (x, y, x * y), values):
        print('{} * {} = {}'.format(*i))
        print(i)


if __name__ == "__main__":
    # map vs itertools.starmap
    itertools_map_vs_starmap()