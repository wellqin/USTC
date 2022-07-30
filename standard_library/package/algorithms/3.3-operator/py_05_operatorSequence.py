import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def operator_sequence_operation():
    """
    we do some sequence operation like following.
    ---CRUD---
    container :: in, append, extend, clear, remove, __new__, __eq__
    sized     :: len, index
    iterable  :: set, get
    """
    a = [1, 2, 3]
    b = list('abc')
    print('a =', a)
    print('b =', b)
    
    # concatenate
    print('\nConstructive:')
    print('  concat(a, b):', operator.concat(a, b))
    
    # search
    print('\nSearch:')
    print('  contains(a, 1)  :', operator.contains(a, 1))
    print('  contains(b, "d"):', operator.contains(b, "d"))
    print('  countOf(a, 1)   :', operator.countOf(a, 1))
    print('  countOf(b, "d") :', operator.countOf(b, "d"))
    print('  indexOf(a, 1)   :', operator.indexOf(a, 1))
    # access items
    print('\nAccess:')
    print('  getitem(b, 1)                   :', operator.getitem(b, 1))
    print('  getitem(b, slice(1, 3))         :', operator.getitem(b, slice(1, 3)))
    print('  setitem(b, 1, "d")              :', end=' ')
    operator.setitem(b, 1, "d")
    print(b)
    print('  setitem(a, slice(1, 3), [4, 5]) :', end=' ')
    operator.setitem(a, slice(1, 3), [4, 5])
    print(a)
    # remove items
    print('\nDestructive:')
    print('  delitem(b, 1)                   :', end=' ')
    operator.delitem(b, 1)
    print(b)
    print('  delitem(a, slice(1, 3))         :', end=' ')
    operator.delitem(a, slice(1, 3))
    print(a)

if __name__ == "__main__":
    operator_sequence_operation()