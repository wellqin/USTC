import sys, decimal
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def decimal_arithmetic():
    # ! it should be same as normal integer/float
    a = decimal.Decimal('5.1')
    b = decimal.Decimal((0, (3, 1, 4), -2))
    c = 4
    d = 3.14 
    print('a     =', repr(a))
    print('b     =', repr(b))
    print('c     =', repr(c))
    print('d     =', repr(d))
    print('a + b =', a + b)
    print('a - b =', a - b)
    print('a * b =', a * b)
    print('a / b =', a / b)
    print()
    print('a + c =', a + c)
    print('a - c =', a - c)
    print('a * c =', a * c)
    print('a / c =', a / c)
    print()
    # ! decimal arithmetic does NOT support decimal.Decimal() operator float
    print('a + d', end=' ')
    try:
        print(a + d)
    except TypeError as err:
        print(err)
    return

if __name__ == "__main__":
    # arithmetics
    decimal_arithmetic()