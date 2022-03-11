import sys, fractions
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def fractions_create_integers():
    for n, d in [
            (1, 2), (2, 4), (3, 6)
        ]:
        f = fractions.Fraction(n, d)
        print('{}/{} = {}'.format(n, d, f))
    return

@addBreaker
def fractions_create_strings():
    for s in ['1/2', '2/4', '3/6']:
        f = fractions.Fraction(s)
        print('{} = {}'.format(s, f))
    return

@addBreaker
def fractions_create_stringFloats():
    for s in ['0.5', '1.5', '2.0', '5e-1']:
        f = fractions.Fraction(s)
        print('{:<4} = {}'.format(s, f))
    return

@addBreaker
def fractions_create_floats():
    for s in [0.5, 1.5, 2.0, 5e-1]:
        f = fractions.Fraction(s)
        print('{:<4} = {}'.format(s, f))
    return

@addBreaker
def fractions_create_decimals():
    import decimal
    list_decimals = [decimal.Decimal((0, (i, j), -1)) for (i, j) in enumerate(range(1, 5))]
    for d in list_decimals:
        f = fractions.Fraction(d)
        print('{!r:<4} = {}'.format(d, f))
    return

if __name__ == "__main__":
    # creates by passing integers
    fractions_create_integers()
    # creates by passing strings
    fractions_create_strings()
    # parses stringFloats
    fractions_create_stringFloats()
    # creates by passing float or decimals
    fractions_create_floats()
    fractions_create_decimals()