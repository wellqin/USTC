import sys, pickle
sys.path.append('.')
from pkg.breaker import addBreaker

class Node:
    """A simple digraph
    """
    def __init__(self, name):
        self.name = name
        self.connections = []
    def add_edge(self, node):
        "Create an edge between this node and the other."
        self.connections.append(node)
    def __iter__(self):
        return iter(self.connections)

def preorder_traversal(root, seen=None, parent=None):
    """Generator function to yield the edges in a graph.
    """
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)

def show_edges(root):
    "Print all the edges in the graph."
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} -> {:>2} ({})'.format(
            parent.name, child.name, id(child)))



@addBreaker
def pickle_cycle():
    # set ip the nodes
    root = Node('root')
    a = Node('a')
    b = Node('b')
    c = Node('c')
    # add edges
    root.add_edge(a)
    root.add_edge(b)
    a.add_edge(b)
    b.add_edge(a)
    b.add_edge(c)
    a.add_edge(a)
    print('ORIGINAL GRAPH:')
    show_edges(root)

    # pickle and unpickle the graph to create
    # a new set of nodes
    dumped = pickle.dumps(root)
    reloaded = pickle.loads(dumped)
    print('\nRELOADED GRAPH:')
    show_edges(reloaded)
    pass


if __name__ == "__main__":
    # ! pickle auto handles complex, circular references between objects
    # * does not need any special handling
    pickle_cycle()