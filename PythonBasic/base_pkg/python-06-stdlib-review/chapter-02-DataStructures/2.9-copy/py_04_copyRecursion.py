import copy, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class Graph:
    def __init__(self, name, connections):
        self.name        = name
        self.connections = connections
    def add_connectiton(self, other):
        self.connections.append(other)
    def __repr__(self):
        return 'Graph(name={}, id={})'.format(self.name, id(self))
    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Already copied to {!r}'.format(existing))
            return existing
        print('  Memo dictionary:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('     (empty)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print(' Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connectiton(copy.deepcopy(c, memo))
        return dup

@addBreaker
def copy_recursion():
    root = Graph('root', [])
    a    = Graph('a', [root])
    b    = Graph('b', [a, root])
    root.add_connectiton(a)
    root.add_connectiton(b)

    dup = copy.deepcopy(root)

    print(root)
    print(dup)

if __name__ == "__main__":
    copy_recursion()