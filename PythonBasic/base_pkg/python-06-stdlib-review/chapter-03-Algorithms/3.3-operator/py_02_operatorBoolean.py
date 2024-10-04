import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def operator_Boolean():
    a = -1
    b = 5

    print('a = ', a)
    print('b = ', b)
    print()
    print('not_(a)      :', operator.not_(a))
    print('truth(a)     :', operator.truth(a))
    print('is_(a, b)    :', operator.is_(a, b))
    print('is_not(a, b) :', operator.is_not(a, b))

if __name__ == "__main__":
    # boolean API
    operator_Boolean()