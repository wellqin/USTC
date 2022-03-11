import sys, pickle
sys.path.append('.')
from pkg.breaker import addBreaker


@addBreaker
def pickle_stream():
    class SimpleObj:
        def __init__(self, name):
            self.name = name
            l = list(name)
            l.reverse()
            self.name_backwards = ''.join(l)
            return
    # or correct way is the following. either way works
    # from py_03_pickleWorkWithStreams import SimpleObj

    data = []
    data.append(SimpleObj('pickle'))
    data.append(SimpleObj('preserve'))
    data.append(SimpleObj('last'))
    filename = 'test.dat'
    # simulate a file
    with open(filename, 'wb') as out:
        for o in data:
            print('WRITING  : {} ({})'.format(o.name, o.name_backwards))
            pickle.dump(o, out)

@addBreaker
def pickle_load_from_file1():
    filename = 'test.dat'
    with open(filename, 'rb') as inp:
        while True:
            try:
                o = pickle.load(inp)
            except EOFError:
                break
            else:
                print('READ     : {} ({})'.format(o.name, o.name_backwards))

if __name__ == "__main__":
    # dump data into harddisk
    pickle_stream()
    # load data from harddisk. problem occures
    # ? why?
    # ! pickle can serialzie instances of user defined class, but NOT user defined calss definition. 
    # ! and the class must be in the same namespace during pickling and unpickling
    pickle_load_from_file1()
