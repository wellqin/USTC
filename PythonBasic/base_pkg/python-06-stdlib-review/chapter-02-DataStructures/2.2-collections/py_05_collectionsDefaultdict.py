import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

def default_factory():
    return 'default value'

@addBreaker
def collections_defaultdict_create():
    d = collections.defaultdict(default_factory, foo='bar')
    print('d: ', d)
    print('foo =>', d['foo'])
    print('bar =>', d['bar'])

def main():
    collections_defaultdict_create()

if __name__ == "__main__":
    main()