import sys, linecache, os
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def linecache_path_search():
    # look for the linecache module using
    # the built-in sys.path search
    module_line = linecache.getline('linecache.py', 3)
    print('MODULE:')
    print(repr(module_line))
    # look at the linecache module source directly
    file_src = linecache.__file__
    if file_src.endswith('.pyc'):
        file_src = file_src[:-1]
    print('\nFILE:')
    with open(file_src, 'r') as f:
        file_line = f.readlines()[2]
    print(repr(file_line))
    
    pass

if __name__ == "__main__":
    linecache_path_search()