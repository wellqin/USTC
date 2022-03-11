import sys, pickle
sys.path.append('.')
from pkg.breaker import addBreaker

class State:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'State({!r})'.format(self.__dict__)

class MyClass:
    def __init__(self, name):
        print('MyClass.__init__({})',format(name))
        self._set_name(name)
    def _set_name(self, name):
        self.name = name
        self.computed = name[::-1]
    def __repr(self):
        return 'MyClass({!r}) (computed={!r})'.format(self.name, self.computed)
    def __getstate__(self):
        state = State(self.name)
        print('__getstate__ -> {!r}'.format(state))
        return state
    def __setstate__(self, state):
        print('__setstate__({!r})'.format(state))
        self._set_name(state.name)

@addBreaker
def pickle_state():
    inst = MyClass('name here')
    print('BEFORE   :', inst)
    dumped = pickle.dumps(inst)
    reloaded = pickle.loads(dumped)
    print('AFTER    :', reloaded)
    pass

if __name__ == "__main__":
    # ! NOT all objects are picklable
    # ! sockets, file handles, database connections, 
    # ! and other objects with `runtime` state that depends on the operating system 
    # ! or another process may not be able to be saved in a meaningful way
    # * objects that have non-picklable attributes can define __getstate__() and __setstate__()
    # * to return a subset of the state of the instance to be pickled.
    pickle_state()