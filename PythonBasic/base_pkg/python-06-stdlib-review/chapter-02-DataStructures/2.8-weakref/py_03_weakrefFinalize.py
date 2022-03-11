
import weakref, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_02_weakrefRef import ExpensiveObj

# @addBreaker
def weakref_finalize():
    def on_finalize(*args):
        print('on_finalize({!r})'.format(args))
    
    obj = ExpensiveObj()
    # arguments to finalize are the obj to track, a callable to invoke 
    # when the obj is garbage collected, and any positional or named arguments to pass to the callable.
    weakref.finalize(obj, on_finalize, 'extra argument')
    del obj

@addBreaker
def weakref_finalize_atexit():
    def on_finalize(*args):
        print('on_finalize({!r})'.format(args))
    obj = ExpensiveObj()
    f   = weakref.finalize(obj, on_finalize, 'extra argument')
    # atexit is writable property to control whether the callback is invoked as a program is exiting, if it hasn't been called.
    # ohh, just like an alarm
    # f.atexit = bool(sys.argv[1])
    f.atexit = False

@addBreaker
def weakref_finalize_reference():
    import gc
    def on_finalize(*args):
        print('on_finalize({!r})'.format(args))
    obj      = ExpensiveObj()
    obj_id   = id(obj)
    f        = weakref.finalize(obj, on_finalize, obj)
    f.atexit = False
    # deletes obj
    del obj
    # Returns a list of all objects tracked by the collector, excluding the list returned.
    for o in gc.get_objects():
        if id(o) == obj_id:
            print('found uncollected obj in gc')

@addBreaker
def weakref_finalize_reference_method():
    import gc
    # derives from MyExpensiveObj
    class MyExpensiveObj(ExpensiveObj):
        def do_finalize(self):
            print('do_finalize')
    # creates an expensive obj
    obj = MyExpensiveObj()
    obj_id = id(obj)
    # sets up weakref. bounds an obj method with finalize. 
    # linking obj, and aslo liking obj.method on finalize.. this is so-called
    # 'to be caught in one's own trap'.. in this case, gc won't track it ofc
    f = weakref.finalize(obj, obj.do_finalize)
    f.atexit = False
    # deletes obj
    del obj
    for o in gc.get_objects():
        if id(o) == obj_id:
            print('found uncollected object in gc')

if __name__ == "__main__":
    # more robust management of resources when weak references are cleaned up, 
    # use finalize to associate callbacks with objects.
    # finalize() instance is retained until the attached obj is deleted, 
    # even if the application does not retrain a reference to the finalizer
    weakref_finalize()
    # weakref.finalize().atexit(True)
    weakref_finalize_atexit()
    # giving the finalize instance a reference to the obj it tracks causes a reference to be retained, 
    # so the obj is never garbage collected
    weakref_finalize_reference()