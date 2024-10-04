import copy, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_copy_data import MyClass

class MyClassHook(MyClass):
    # wow, dunder methods
    def __copy__(self):
        print('__copy__()')
        return MyClass(self.name)
    # wow * 2, dunder methods.
    # *memo* is a memo dictionary
    def __deepcopy__(self, memo):
        print('__deepcopy__{}'.format(memo))
        return MyClass(copy.deepcopy(self.name, memo))

@addBreaker
def copy_hooks():
    a  = MyClassHook('a')
    sc = copy.copy(a)
    dc = copy.deepcopy(a)
    print("a  :", id(a))
    print("sc :", id(sc))
    print("dc :", id(dc))
    print("a  :", a)
    print("sc :", sc)
    print("dc :", dc)

if __name__ == "__main__":
    copy_hooks()