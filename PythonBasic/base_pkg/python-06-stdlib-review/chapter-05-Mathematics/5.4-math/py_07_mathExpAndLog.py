import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_pow():
    INPUTS = [
        # Typical uses
        (2, 3),
        (2.1, 3.2),
        # Always 1
        (1.0, 5),
        (2.0, 0),
        # Not a number
        (2, float('nan')),
        # Roots
        (9.0, 0.5),
        (27.0, 1.0 / 3),
    ]
    for x, y in INPUTS:
        print('{:5.1f} ** {:5.3f} = {:6.3f}'.format(x, y, math.pow(x, y)))

### TODOS: P316
@addBreaker
def math_sqrt():
    print(math.sqrt(9.0))
    print(math.sqrt(3))
    try:
        # ! `complex numbers`, which are NOT handled by `math`
        print(math.sqrt(-1))
    except ValueError as err:
        print('Cannot compute sqrt(-1):', err)

@addBreaker
def math_log():
    print(math.log(8))
    print(math.log(8, 2))
    print(math.log(0.5, 2))

@addBreaker
def math_log10_vs_log():
    print('{:2} {:^12} {:^10} {:^20} {:8}'.format('i', 'x', 'accurate', 'inaccurate', 'mismatch'))
    print('{:-^2} {:-^12} {:-^10} {:-^20} {:-^8}'.format(*('',) * 5))
    print('log10')
    for i in range(0, 10):
        x = math.pow(10, i)
        accurate = math.log10(x)
        inaccurate = math.log(x, 10)
        match = '' if int(inaccurate) == i else '*'
        print('{:2d} {:12.1f} {:10.8f} {:20.18f} {:^5}'.format(i, x, accurate, inaccurate, match))    

@addBreaker
def math_log2():
    print('{:>2} {:^5} {:^5}'.format('i', 'x', 'log2'))
    print('{:-^2} {:-^5} {:-^5}'.format(*('',) * 3))
    for i in range(0, 10):
        x = math.pow(2, i)
        result = math.log2(x)
        print('{:2d} {:5.1f} {:5.1f}'.format(i, x, result))

@addBreaker
def math_loglp():
    x = 0.0000000000000000000000001
    print('x        :', x)
    print('1 + x    :', 1 + x)
    print('log(1+x) :', math.log(1 + x))
    print('log1p(x) :', math.log1p(x))

@addBreaker
def math_exp():
    x   = 2
    fmt = '{:.20f}'
    print(fmt.format(math.e ** x))
    print(fmt.format(math.pow(math.e, x)))
    print(fmt.format(math.exp(x)))
    
@addBreaker
def math_expml():
    x = 0.0000000000000000000000001
    print(x)
    print(math.exp(x) - 1)
    print(math.expm1(x))

if __name__ == "__main__":
    # power
    math_pow()
    # sqrt()
    math_sqrt()
    # log
    math_log()
    # log10 vs log, accuracy is different
    # ! log10
    math_log10_vs_log()
    # log2
    math_log2()
    # loglp() calculates the Newton-Mercator series
    # the natural logarithm of 1 + x
    math_loglp()
    # exponetial
    # ! just like other special-case functions,
    # ! it uses an algorithm that produces more accurate results than general-purpose equivalent math.pow(math.e, x)
    math_exp()
    #expml? wth is it? calc index .. oh well
    math_expml()