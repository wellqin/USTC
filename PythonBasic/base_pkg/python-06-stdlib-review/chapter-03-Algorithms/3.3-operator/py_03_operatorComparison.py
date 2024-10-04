import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def operator_comparison():
    a = 1
    b = 5.0
    print('a =', a)
    print('b =', b)
    print()
    comp_funcs = 'eq ne lt le gt ge'.split(' ')
    for func in comp_funcs:
        print('operator.{}(a, b): {}'.format(eval('operator.' + func).__name__, eval('operator.' + func)(a, b)))

if __name__ == "__main__":
    operator_comparison()