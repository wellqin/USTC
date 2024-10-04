import pprint, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class Node:
    def __init__(self, name, contents=[]):
        self.name     = name
        self.contents = contents[:]
    def __repr__(self):
        return 'node({!r}, {!r})'.format(self.name, self.contents)

def pprint_arbitrary_obj():
    trees = [
        Node('node-1'),
        Node('node-2', [Node('node-2-1')]),
        Node('node-3', [Node('node-3-1')]),
    ]
    pprint.pprint(trees)

if __name__ == "__main__":
    pprint_arbitrary_obj()