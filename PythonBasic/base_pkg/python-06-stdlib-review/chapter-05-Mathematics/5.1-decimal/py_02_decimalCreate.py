"""
A decimal instance can represent any number exactly, be rounded up or down,
and apply a limit to the number of significant digits

"""
import decimal, sys
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def decimal_create():
    fmt = '{0:<25}  {1:<25}'
    # headers
    print(fmt.format('Input', 'Output'))
    print(fmt.format('-' * 25, '-' * 25))
    # integer
    print(fmt.format(5, decimal.Decimal(5)))
    # string
    print(fmt.format('3.14', decimal.Decimal('3.14')))
    # float
    f = .1
    print(fmt.format(repr(f), decimal.Decimal(str(f))))
    print('{:0.23g} {:<25}'.format(
        f,
        str(decimal.Decimal.from_float(f))[:25])
    )
    # tuple as argument, its notation (±, (\d, \d, \d, ...), exp)
    # aha, it is basically treat a number combining from 4 parts
    t = (1, (1, 2), -2)
    print(fmt.format(repr(t), decimal.Decimal(t)))
    return

if __name__ == "__main__":
    # create decimal obj by passing inter, string, float
    decimal_create()