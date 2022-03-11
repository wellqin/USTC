import decimal, sys, pathlib, os
sys.path.append('.')
# sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
# sys.path.append(str(pathlib.Path.cwd()))
# sys.path.append(os.getcwd())
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def decimal_formatting():
    # ! same as str obj formatting by implementing Python ___format__() protocol
    # ahh, i see what tuple argument notation is good at. **fidelity**
    d1 = decimal.Decimal(1.1)
    d2 = decimal.Decimal((1, (2, 3), -2))

    def display(d: decimal):
        print('Precision')
        print('{:.1}'.format(d))
        print('{:.2}'.format(d))
        print('{:.3}'.format(d))
        print('{:.18}'.format(d))

        print('\nwidth and precision combined:')
        print('{:5.1f} {:5.1g}'.format(d, d))
        print('{:5.2f} {:5.2g}'.format(d, d))
        print('{:5.1f} {:5.1g}'.format(d, d))

        print('\nzero padding:')
        print('{:05.1}'.format(d))
        print('{:05.2}'.format(d))
        print('{:05.3}'.format(d))
        print()
        return
    for d in [d1, d2]:
        display(d)
    return











if __name__ == "__main__":
    decimal_formatting()