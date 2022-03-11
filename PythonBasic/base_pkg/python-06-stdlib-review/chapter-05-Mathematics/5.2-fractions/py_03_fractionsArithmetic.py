import sys, fractions
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def fractions_arithmetic():
    # ! just like decimal, fractions implement Python arithmetic protocol
    f1 = fractions.Fraction(1, 2)
    f2 = fractions.Fraction(3, 4)
    print('{} + {} = {}'.format(f1, f2, f1 + f2))
    print('{} - {} = {}'.format(f1, f2, f1 - f2))
    print('{} * {} = {}'.format(f1, f2, f1 * f2))
    print('{} / {} = {}'.format(f1, f2, f1 / f2))
    return

if __name__ == "__main__":
    fractions_arithmetic()