import sys, fractions
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def fractions_limit_denominator():
    import math
    print('PI       =', math.pi)
    f_pi = fractions.Fraction(str(math.pi))
    print('No limit =', f_pi)

    for i in [1, 6, 11, 60, 70, 90, 100]:
        limited = f_pi.limit_denominator(i)
        print('{0:>8} = {1}'.format(i, limited))
    return

if __name__ == "__main__":
    fractions_limit_denominator()