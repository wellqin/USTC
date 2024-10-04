import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def operator_arithmetic():
    """
    arithmetic, math
    +, -, |a|
    +, -, *, //, /, %, pow
    &, |, ^, ~, <<, >>
    """
    a, b, c, d = -1, 5.0, 2, 6
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)

    print('\nPositive/Negative:')
    print('abs(a):', operator.abs(a))
    print('neg(a):', operator.neg(a))
    print('neg(b):', operator.neg(b))
    print('pos(a):', operator.pos(a))
    print('pos(b):', operator.pos(b))

    print('\nArithmetic:')
    print('add(a, b)        :', operator.add(a, b))
    print('sub(b, a)        :', operator.sub(b, a))
    print('mul(a, b)        :', operator.mul(a, b))
    print('truediv(a, b)    :', operator.truediv(a, b))
    print('truediv(d, c)    :', operator.truediv(d, c))
    print('floordiv(a, b)   :', operator.floordiv(a, b))
    print('pow(c, d)        :', operator.pow(c, d))
    print('mod(a, b)        :', operator.mod(a, b))

    print('\nBitwise:')
    print('and_(c, d)       :', operator.and_(c, d))    # c & d
    print('or_(c, d)        :', operator.or_(c, d))     # c | d
    print('invert(c)        :', operator.invert(c))     # two's complement. ~c = -c - 1
    print('xor(c, d)        :', operator.xor(c, d))     # a ^ b
    print('lshift(c, d)     :', operator.lshift(c, d))  # d << c
    print('rshift(d, c)     :', operator.rshift(d, c))  # d >> c

if __name__ == "__main__":
    operator_arithmetic()