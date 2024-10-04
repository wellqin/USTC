import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def operator_inplace():
    """
    we have inplace operators on operants.
    i += 1
    i -= 1
    i *= 1
    i /= 2
    i //= 2
    i %= 2
    i **= 2
    """
    a, b, c, d = -1, 5.0, [1, 2, 3], list('abc')
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)
    # simple exampls
    print('a += b =>', operator.iadd(a, b))
    print('c += d =>', operator.iconcat(c, d))
    
    return

if __name__ == "__main__":
    operator_inplace()