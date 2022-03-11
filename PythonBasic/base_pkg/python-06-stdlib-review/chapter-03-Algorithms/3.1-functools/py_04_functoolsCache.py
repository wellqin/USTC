import functools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@functools.lru_cache(maxsize=2)
def expensive(a: int, b: int):
    print('expensive({}, {})'.format(a, b))
    return a * b
MAX = 2

def make_call(a: int, b: int):
    print('({}, {})'.format(a, b), end=' ')
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print('cache hit')

@addBreaker
def functools_lru_cache():
    print('First set of calls:')
    for i in range(MAX):
        for j in range(MAX):
            expensive(i, j)
    print(expensive.cache_info())
    
    print('\nSecond set of calls:')
    for i in range(MAX + 1):
        for j in range(MAX + 1):
            expensive(i, j)
    print(expensive.cache_info())
    
    print('\nClearing cache:')
    expensive.cache_clear()

    print('\nThird set of calls:')
    for i in range(MAX):
        for j in range(MAX):
            expensive(i, j)
    print(expensive.cache_info())

@addBreaker
def functools_lru_cache_expire():
    print('Establish the cache')
    make_call(1, 2)
    make_call(2, 3)

    print('\nUse cached items')
    make_call(1, 2)
    make_call(2, 3)

    print('\nCompute a new value, triggering cache expiration')
    make_call(3, 4)

    print('\nCache still contains one old item')
    make_call(2, 3)

    print('\nOldest item needs to be computed')
    make_call(1, 2)
    pass

@addBreaker
def functools_lrc_cache_arguments():
    make_call(1, 2)
    # try NOT hashable arguments ..
    try:
        # list object [1] is NOT hashable
        # it raise TypeError, 
        # ! because the keys for the cache managed by lru_cache() must be hashable, 
        # ! so ALL of the **arguments** to the function wrapped with the cache lookup MUST be hashable
        make_call([1], 2)
    except TypeError as err:
        print('Error: {}'.format(err))
    # try hashable arguments ..
    try:
        make_call(1, {'2': 'two'})
    except TypeError as err:
        print('Error: {}'.format(err))

if __name__ == "__main__":
    # 'least recently used', memorization
    functools_lru_cache()
    # maxsize = 2
    functools_lru_cache_expire()
    # lru_cache_arguments MUST be hashable