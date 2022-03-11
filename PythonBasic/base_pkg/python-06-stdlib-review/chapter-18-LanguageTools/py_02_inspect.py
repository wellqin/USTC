import inspect
from example import example

class C(example.B):
    pass

class D(C, example.A):
    pass


if __name__ == '__main__':
    for name, data in inspect.getmembers(example):
        if name.startswith('__'):
            continue
        else:
            print('{} : {!r}'.format(name, data))
    print()
    print(inspect.getmembers(example.B, inspect.isfunction))
    print()
    print(inspect.getmembers(example.B, inspect.ismethod))
    print()
    print(inspect.getdoc(example.B))
    print()
    print(inspect.getcomments(example.B.do_something))
    print()
    print(inspect.getsource(example.A))
    print()
    print(inspect.getsourcelines(example.A.get_name))
    print()
    print(inspect.getclasstree([example.A, example.B, C, D], unique=True))
    print()
    for c in inspect.getmro(D):
        print(' {}'.format(c.__name__))