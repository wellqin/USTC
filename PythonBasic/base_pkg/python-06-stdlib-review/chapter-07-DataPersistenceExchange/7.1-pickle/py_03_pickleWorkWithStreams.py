import sys, pickle, pprint, io
sys.path.append('.')
from pkg.breaker import addBreaker

class SimpleObj:
    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


@addBreaker
def pickle_stream():
    data = []
    data.append(SimpleObj('pickle'))
    data.append(SimpleObj('preserve'))
    data.append(SimpleObj('last'))

    # simulate a file
    out = io.BytesIO()
    for o in data:
        print('WRITING : {} ({})'.format(o.name, o.name_backwards))
        pickle.dump(o, out)
        out.flush()
    inp = io.BytesIO(out.getvalue())
    while True:
        try:
            o = pickle.load(inp)
        except EOFError:
            break
        else:
            print('READ    : {} ({})'.format(o.name, o.name_backwards))
    pass


if __name__ == "__main__":
    # in addition to dumps() and loads(),
    # pickle provides convenience functions for working with file-liek streams
    pickle_stream()