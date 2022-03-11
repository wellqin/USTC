import weakref, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

# assume we have an expensive class
class ExpensiveObj:
    def __del__(self):
        print('(Deleting {}'.format(self))

@addBreaker
def weakref_ref(): 
    obj = ExpensiveObj()
    r   = weakref.ref(obj)

    print('obj:', obj)
    print('ref:', r)
    print('r():', r())
    print('deleting obj')
    del obj
    print('r():', r())

    # I need comparison between a normal reference vs weakref.reference to see:
    # - reference count on the obj
    # - prevent garbage collecting
    # TODO: P160
@addBreaker
def weakref_ref_callback(): 
    def callback(reference):
        print('callback({!r})'.format(reference))
    obj = ExpensiveObj
    r = weakref.ref(obj, callback)
    print('obj:', obj)
    print('ref:', r)
    print('r():', r())
    print('deleting obj')
    del obj
    print('r():', r())

@addBreaker
def weakref_finalize():
    def on_finalize(*args):
        print('on_finalize({!r})'.format(args))
    
    obj = ExpensiveObj()
    # arguments to finalize are the obj to track, a callable to invoke 
    # when the obj is garbage collected, and any positional or named arguments to pass to the callable.
    weakref.finalize(obj, on_finalize, 'extra argument')
    del obj

if __name__ == "__main__":
    # first impression
    weakref_ref()
    # callback when referenced obj is deleted or 'dead' and no long refers to the original obj.
    weakref_ref_callback()
    # more robust management of resources when weak references are cleaned up, 
    # use finalize to associate callbacks with objects.
    # finalize() instance is retained until the attached obj is deleted, 
    # even if the application does not retrain a reference to the finalizer
    weakref_finalize()