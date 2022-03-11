"""
Hyperbolic functions appear in linear differential equations and are used when working
with `electromagnetic fields`, `fluid dynamics`, `special relativity`, and other `advanced physics
and mathematics`.

"""

import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_hyperbolic():
    print('{:^6} {:^6} {:^6} {:^6}'.format(
    'X', 'sinh', 'cosh', 'tanh',
    ))
    print('{:-^6} {:-^6} {:-^6} {:-^6}'.format('', '', '', ''))
    fmt = '{:6.4f} {:6.4f} {:6.4f} {:6.4f}'
    for i in range(0, 11, 2):
        x = i / 10.0
        print(fmt.format(
        x,
        math.sinh(x),
        math.cosh(x),
        math.tanh(x),
        ))

@addBreaker
def math_invert_hyperbolic():
    print('{:^6} {:^6} {:^6} {:^6}'.format(
    'X', 'asinh', 'acosh', 'atanh',
    ))
    print('{:-^6} {:-^6} {:-^6} {:-^6}'.format('', '', '', ''))
    fmt = '{:6.4f} {:6.4f} {:6.4f} {:6.4f}'
    for i in range(0, 11, 2):
        x = i / 10.0
        print(fmt.format(
        x,
        math.sinh(x),
        math.cosh(x),
        math.tanh(x),
        ))

@addBreaker
def math_erf():
    print('{:^5} {:7}'.format('x', 'erf(x)'))
    print('{:-^5} {:-^7}'.format('', ''))
    for x in [-3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3]:
        print('{:5.2f} {:7.4f}'.format(x, math.erf(x)))

if __name__ == "__main__":
    # nice
    math_hyperbolic()
    # always pairs
    # The inverse hyperbolic functions acosh(), asinh(), and atanh() are also available.
    math_invert_hyperbolic()
    # ! special functions: The Gauss error function is used in statistics.
    math_erf()

