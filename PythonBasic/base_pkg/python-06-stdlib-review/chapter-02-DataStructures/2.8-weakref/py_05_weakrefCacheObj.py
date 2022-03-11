"""
weakref.ref and weakref.proxy are considered as "low level".

"""

import weakref, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_02_weakrefRef import ExpensiveObj

@addBreaker
def weakref_valuedict():
    import gc
    import pprint
    class MyExpensiveObj(ExpensiveObj):
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return 'ExpensiveObject({})'.format(self.name)
        def __del__(self):
            print('     (Deleting {})'.format(self))
    
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

    def demo(cache_factory):
        # hold objects so any weak references are not removed immediately
        all_refs = {}
        # create the cache using the factory
        print('CACHE TYPE:', cache_factory)
        cache = cache_factory()
        for name in ['one', 'three', 'two']:
            o              = MyExpensiveObj(name)
            cache[name]    = o
            all_refs[name] = o
            del o # decref
        print('  all_refs = ', end=' ')
        pprint.pprint(all_refs)
        print('\n   Before, cache contains:', list(cache.keys()))
        for name, value in cache.items():
            print('     {} = {}'.format(name, value))
            del value   # decref
        # removes all references to the objects except the cache.
        print('\n   Cleanup:')
        del all_refs
        gc.collect()
        # result
        print('\n   After, cache contains:', list(cache.keys()))
        for name, value in cache.items():
            print('     {} = {}'.format(name, value))
        print('   demo returning')
        return
    
    demo(dict)
    print()
    demo(weakref.WeakValueDictionary)


if __name__ == "__main__":
    weakref_valuedict()