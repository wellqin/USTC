import sys, decimal
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def decimal_special_values():
    list_spVals = [
        'Infinity',
        'NaN',
        '0'
    ]
    for val in list_spVals:
        print(decimal.Decimal(val), decimal.Decimal('-' + val))
    print()
    # Match with infinity. hoho
    print('Infinity + 1 :', decimal.Decimal('Infinity') + 1)
    print('-Infinity + 1:', decimal.Decimal('-Infinity') + 1)
    # print comparing NaN
    print(decimal.Decimal('NaN') == decimal.Decimal('Infinity'))
    print(decimal.Decimal('NaN') != decimal.Decimal('Infinity'))
    return

if __name__ == "__main__":
    decimal_special_values()