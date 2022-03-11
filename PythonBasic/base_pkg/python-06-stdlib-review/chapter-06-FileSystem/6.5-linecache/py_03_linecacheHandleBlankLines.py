import sys, linecache
sys.path.append('.')
from pkg.breaker import addBreaker
import linecache_data

@addBreaker
def linecache_empty_line():
    fn = linecache_data.make_tempfile()
    # Blank lines include the newline
    print('BLANK    : {!r}'.format(linecache.getline(fn, 8)))
    linecache_data.cleanup(fn)


if __name__ == "__main__":
    linecache_empty_line()