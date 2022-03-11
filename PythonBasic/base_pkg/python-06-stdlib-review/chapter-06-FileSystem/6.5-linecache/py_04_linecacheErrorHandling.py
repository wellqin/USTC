import sys, linecache, linecache_data
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def linecache_out_of_range():
    fn = linecache_data.make_tempfile()
    # the cache always return a string, 
    # and uses an empty string 
    # to indicate a line that does not exist.
    not_there = linecache.getline(fn, 500)
    print('NOT THERE: {!r} includes {} characters'.format(
        not_there, len(not_there)
    ))
    
    linecache_data.cleanup(fn)
    pass

@addBreaker
def linecache_missing_file():
    no_such_file = linecache.getline('this_file_not_exist.txt', 1)
    print('NO FILE: {!r}'.format(no_such_file))

if __name__ == "__main__":
    # handles lines that are out of range
    # return an empty string
    linecache_out_of_range()
    # handles files not exist
    # return an empty string
    linecache_missing_file()