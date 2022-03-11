import weakref, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_02_weakrefRef import ExpensiveObj

@addBreaker
def weakref_proxy():
    class MyExpensiveObj(ExpensiveObj):
        def __init__(self, name):
            self.name = name
    obj = MyExpensiveObj('My Obj')
    r   = weakref.ref(obj)
    p   = weakref.proxy(obj)

    print('Before delete obj')
    print('via obj  :', obj.name)
    print('via ref  :', r().name)
    print('via proxy:', p.name)
    del obj
    print('\nAfter delete obj')
    print('via ref  :', r().name) # r() is linking nothing. r is None
    print('via proxy:', p.name) # proxy

if __name__ == "__main__":
    weakref_proxy()