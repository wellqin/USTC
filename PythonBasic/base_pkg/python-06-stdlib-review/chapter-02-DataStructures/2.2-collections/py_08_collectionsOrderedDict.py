import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def collections_ordereddict_vs_dict():
    ### no difference when using the following construction method
    d  = dict(zip(list('abc'), list('ABC')))
    od = collections.OrderedDict(zip(list('abc'), list('ABC')))
    ### ? difference pop out?
    # no. wtf
    # d = dict()
    # d['a'] = 'A'
    # d['b'] = 'B'
    # d['c'] = 'C'
    # od = collections.OrderedDict()
    # od['a'] = 'A'
    # od['b'] = 'B'
    # od['c'] = 'C'
    print('dict:')
    for k, v in d.items():
        print(k, v)
    print('\nOrderedDict:')
    for k, v in od.items():
        print(k, v)

@addBreaker
def collections_ordereddict_euqality():
    # order doest matter in dict()
    d1 = dict(zip(list('abc'), list('ABC')))
    d2 = dict(zip(list('cba'), list('CBA')))
    print('dict equality        :', end=' ')
    print(d1 == d2)
    # order does matter in OrderedDict() ofc..
    d1 = collections.OrderedDict(zip(list('abc'), list('ABC')))
    d2 = collections.OrderedDict(zip(list('cba'), list('CBA')))
    print('OrderedDict equality :', end=' ')
    print(d1 == d2)

@addBreaker
def collections_ordereddict_move_to_end():
    d1 = collections.OrderedDict(zip(list('abc'), list('ABC')))
    print('Before:')
    for k, v in d1.items():
        print(k, v)
    # reorder, -> end
    d1.move_to_end('b')
    print('\nOrderedDict.move_to_end():')
    for k, v in d1.items():
        print(k, v)
    # reorder, -> 'end'
    # deja vu? we see the shit in deque
    d1.move_to_end('b', last=False)
    print('\nOrderedDict.move_to_end(last=False):')
    for k, v in d1.items():
        print(k, v)   

def main():
    # dict vs OrderedDict, creating
    collections_ordereddict_vs_dict()
    # dict vs OrderedDict, equality
    collections_ordereddict_euqality()
    # OrderedDict, reordering
    collections_ordereddict_move_to_end()

if __name__ == "__main__":
    main()