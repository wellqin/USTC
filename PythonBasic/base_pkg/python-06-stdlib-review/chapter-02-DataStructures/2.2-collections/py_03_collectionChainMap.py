import collections, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

@addBreaker
def collections_chainmap_read(a: dict, b: dict):
    # ! look into the behavior of 'c' ..
    m = collections.ChainMap(a, b)
    # ? 'c' value has been overwritten?
    # A: No
    # ? why not? for example, normal dict value will be overwritten if key(hashable) are same, and its value got updated from latter paris with the same key.
    # A: it's not case in collections.ChainMap(). collections.ChainMap is a class which constructs its dict in sequence of arguments(dict obj) passing into it by default.
    # that's the reason that 'c' in dict obj(b) is omitted.
    print('Individual Values')
    print('a = {}'.format(m['a']))
    print('b = {}'.format(m['b']))
    print('c = {}'.format(m['c']))
    print()
    print('Keys   = {}'.format(list(m.keys())))
    print('Values = {}'.format(list(m.values())))
    print()
    print('Items:')
    for k, v in m.items():
        print('{} = {}'.format(k, v))
        print()
        print('"d" in m: {}'.format(('d' in m)))

@addBreaker
def collections_chainmap_reorder(a: dict, b: dict):
    m = collections.ChainMap(a, b)
    print(m.maps)
    print('c = {}\n'.format(m['c']))
    # Reverse the list.
    m.maps = list(reversed(m.maps))
    print(m.maps)
    print('c = {}'.format(m['c']))

@addBreaker
def memo_view(a: dict):
    mv = memoryview(a)
    print(mv)

@addBreaker
def enum_chainmap_update_behind(a: dict, b: dict):
    m = collections.ChainMap(a, b)
    print('Before: {}'.format(m['c']))
    a['c'] = 'E'
    print('After : {}'.format(m['c']))

@addBreaker
def enum_chainmap_update_directly(a: dict, b: dict):
    m = collections.ChainMap(a, b)
    print('Before:', m)
    m['c'] = 'E'
    print('After :', m)
    print('a     :', a)

@addBreaker
def enum_chainmap_new_child(a: dict, b: dict):
    m = collections.ChainMap(a, b)
    # an instance of *m*, changes it won't affect underlying map list. it will add extra mapping to the map list by default
    c = m.new_child()
    print('Before:', m)
    c['c'] = 'E'
    print('After :', m)
    print('a     :', a)
    print('child :', c)

@addBreaker
def enum_chainmap_new_child_explicit(a: dict, b: dict):
    # why i repeated it here? cuz it behaves unexpectedly if a, b are passing global static variables.
    a = {'a': 'A', 'c': 'C'}
    b = {'b': 'B', 'c': 'D'}
    c  = {'c': 'E'}
    m1 = collections.ChainMap(a, b)
    m2 = m1.new_child(c) # this is equivalent to `m2 = collections.ChainMap(c, *m1.maps)`
    print('m1 :', m1)
    print('m2 :', m2)
    print()
    print('m1["c"] = {}'.format(m1['c']))
    print('m2["c"] = {}'.format(m2['c']))





def main():
    # normal usage of collections.ChainMap()
    collections_chainmap_read(a, b)
    # reorder
    collections_chainmap_reorder(a, b)
    # collections.ChainMap vs memoryview. nope. memoryview() works on bytes only. wtf
    # memo_view(a)
    # update values in ChainMap, approach 01: from source mapping
    enum_chainmap_update_behind(a, b)
    # approach 02: directly change ChainMap. it's limited to change the first mapping tho...
    enum_chainmap_update_directly(a, b)
    # approach 03: collections.ChainMap().new_child()
    enum_chainmap_new_child(a, b)
    # approach 03: explicitly new_child()
    enum_chainmap_new_child_explicit(a, b)

if __name__ == "__main__":
    main()