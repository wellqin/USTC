import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_isclose():
    # yeah. i had written similar function in VBA to find out the cloest view angles
    # concept is simple: put values into one containner, find min-value, other values subtract the min-value
    # find the max-value
    INPUTS = [
        (1000, 900, 0.1),
        (100, 90, 0.1),
        (10, 9, 0.1),
        (1, 0.9, 0.1),
        (0.1, 0.09, 0.1),
    ]
    print('math.isclose(rel_tol):\n')
    print('{:^8} {:^8} {:^8} {:^8} {:^8} {:^8}'.format('a', 'b', 'rel_tol', 'abs(a-b)', 'tolerance', 'close'))
    print('{:-^8} {:-^8} {:-^8} {:-^8} {:-^8} {:-^8}'.format('-', '-', '-', '-', '-', '-'))
    fmt = '{:8.2f} {:8.2f} {:8.2f} {:8.2f} {:8.2f} {!s:>8}'

    for a, b, rel_tol in INPUTS:
        # ! by default, rel_tolerance == 1e-9.
        # ! this behavior could be overrided by passing user-defined tolerance to `rel_tol` argument
        # aha, rel_tol is percentage tolerance
        close = math.isclose(a, b, rel_tol=rel_tol)
        tolerance = rel_tol * max(abs(a), abs(b))
        abs_diff = abs(a - b)
        print(fmt.format(a, b, rel_tol, abs_diff, tolerance, close))
        
    # ofc, pairs, abs_tol is absolute tolerance
    INPUTS = [
        (1.0, 1.0 + 1e-07, 1e-08),
        (1.0, 1.0 + 1e-08, 1e-08),
        (1.0, 1.0 + 1e-09, 1e-08),
    ]
    print('math.isclose(abs_tol):\n')
    print('{:^8} {:^11} {:^8} {:^10} {:^8}'.format('a', 'b', 'abs_tol', 'abs(a-b)', 'close'))
    print('{:-^8} {:-^11} {:-^8} {:-^10} {:-^8}'.format('-', '-', '-', '-', '-'))
    for a, b, abs_tol in INPUTS:
        close = math.isclose(a, b, abs_tol=abs_tol)
        abs_diff = abs(a - b)
        print('{:8.2f} {:11} {:8} {:0.9f} {!s:>8}'.format(a, b, abs_tol, abs_diff, close))
    pass

@addBreaker
def math_compare_special_cases():
    # ? what is special in `math` module?
    # A: inf, nan, finite
    print('nan, nan:', math.isclose(math.nan, math.nan))
    print('nan, 1.0:', math.isclose(math.nan, 1.0))
    print('inf, inf:', math.isclose(math.inf, math.inf))
    print('inf, 1.0:', math.isclose(math.inf, 1.0))

@addBreaker
def math_convert_floatingPoint_to_integer():
    # trunc(), ceil(), floor()
    # ? isn't it familiar with decimal.getcontext().rounding?
    HEADINGS = ('i', 'int', 'trunk', 'floor', 'ceil')
    print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
    print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format(*(' ',) * 5))
    fmt = '{:5.1f} {:5.1f} {:5.1f} {:5.1f} {:5.1f}'
    TEST_VALUES = [
        -1.5,
        -0.8,
        -0.5,
        -0.2,
        0,
        0.2,
        0.5,
        0.8,
        1,
    ]
    for i in TEST_VALUES:
        print(fmt.format(
                        i,
                        int(i),
                        math.trunc(i),
                        math.floor(i),
                        math.ceil(i))
        )

@addBreaker
def math_alternative_representations_of_floatingPoint():
    for i in range(6):
        print('{}/2 = {}'.format(i, math.modf(i / 2.0)))

@addBreaker
def math_frexp():
    print('{:^7} {:^7} {:^7}'.format('x', 'm', 'e'))
    print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))
    for x in [0.1, 0.5, 4.0]:
        m, e = math.frexp(x)
        print('{:7.2f} {:7.2f} {:7d}'.format(x, m, e))
    pass

@addBreaker
def math_ldexp():
    print('{:^7} {:^7} {:^7}'.format('m', 'e', 'x'))
    print('{:-^7} {:-^7} {:-^7}'.format('', '', ''))
    INPUTS = [
    (0.8, -3),
    (0.5, 0),
    (0.5, 3),
    ]
    for m, e in INPUTS:
        x = math.ldexp(m, e)
        print('{:7.2f} {:7d} {:7.2f}'.format(m, e, x))

if __name__ == "__main__":
    # math.isclose(rel_tol) vs math.isclose(abs_tol)
    math_isclose()
    # compare
    math_compare_special_cases()
    # convert floatingPoint value to integer
    math_convert_floatingPoint_to_integer()
    # alternative to represent floatingPoint value using math.modf()
    math_alternative_representations_of_floatingPoint()
    # math.frexp() vs math.ldexp()
    # ! x = m * 2**e
    # aha, ln algorithm
    math_frexp()
    math_ldexp()