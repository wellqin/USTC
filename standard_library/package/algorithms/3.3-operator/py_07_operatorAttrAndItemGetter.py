import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class MyObj:
    def __init__(self, arg):
        # super().__init()
        self.arg = arg
    def __repr__(self):
        return 'MyObj({})'.format(self.arg)

@addBreaker
def operator_attrGetter():
    """
    attrgetter()
    itemgetter()

    getitem()
    setitem()
    """
    l = [MyObj(i) for i in range(5)]
    print('objects   :', l)
    
    # extract the 'arg' value from each obj
    g    = operator.attrgetter('arg')
    vals = [g(i) for i in l] 
    print('arg values:', vals)
    # sort using arg.
    l.reverse()
    print('reversed  :', l)
    print('sorted    :', sorted(l, key=g))
    return

if __name__ == "__main__":
    operator_attrGetter()