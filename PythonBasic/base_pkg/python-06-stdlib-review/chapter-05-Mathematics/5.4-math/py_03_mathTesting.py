import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_testing_exceptions():
    # some concepts: `math.inf` appears when floaing-point value 'overflows'
    # ! Not all floating-point overflows result in `math.inf` values, however.
    # raise `OverflowError` instead
    print('{:^3} {:6} {:6} {:6}'.format('e', 'x', 'x**2', 'isinf'))
    print('{:-^3} {:-^6} {:-^6} {:-^6}'.format('', '', '', ''))
    for e in range(0, 201, 20):
        x = 10.0 ** e
        y = x * x
        # using math.isinf() to test
        print('{:3d} {:<6g} {:<6g} {!s:6}'.format(e, x, y, math.isinf(y)))
    pass

@addBreaker
def math_OverflowError():
    x = 10.0 ** 200
    print('x    =', x)
    print('x*x  =', x * x)
    print('x**2 =', end=' ')
    try:
        print(x ** 2)
    except OverflowError as err:
        print(err)

@addBreaker
def math_isnan():
    x = (10.0 ** 200) * (10.0 ** 200)
    y = x / x
    print('        x =', x)
    print(' isnan(x) =', math.isnan(x))
    print('y = x / x =', x / x)
    print(' x == nan =', y == float('nan'))
    # ! nan does not compare as equal to any value, even itself
    # thus, using math.isnan() to check for nan
    print(' isnan(y) =', math.isnan(y))

@addBreaker
def math_isfinite():
    for f in [0.0, 1.0, math.pi, math.e, math.inf, math.nan]:
        print('{:5.2f} {!s}'.format(f, math.isfinite(f)))



if __name__ == "__main__":
    # math.isinf()
    math_testing_exceptions()
    # OverflowError
    math_OverflowError()
    # math.isnan()
    math_isnan()
    # using math.isfinte() to check regular numbers or either of the special value `inf` or `nan`
    math_isfinite()