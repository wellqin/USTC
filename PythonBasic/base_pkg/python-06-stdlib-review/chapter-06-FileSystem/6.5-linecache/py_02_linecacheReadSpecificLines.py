import sys, linecache
sys.path.append('.')
from pkg.breaker import addBreaker
import linecache_data

@addBreaker
def linecache_getline():
    filename = linecache_data.make_tempfile()
    # pick out the sanme line from source and cache
    # ! (Notice that linecache counts from 1). Differs from normal lists indexing the array from 0 
    print('SOURCE:')
    print('{!r}'.format(linecache_data.lorem.split('\n')[4]))
    print()
    print('CACHE:')
    print('{!r}'.format(linecache.getline(filename, 5)))
    linecache_data.cleanup(filename)
    
    
    
    pass

if __name__ == "__main__":
    # simple usage
    linecache_getline()