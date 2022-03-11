import operator, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

class MyObj:
    def __init__(self, val):
        super().__init__()
        self.val = val
    def __str__(self):
        return 'MyObj({})'.format(self.val)
    def __lt__(self, other):
        """compare for less-than"""
        print('Testing {} < {}'.format(self, other))
        return self.val < other.val
    def __add__(self, other):
        """add values"""
        print('Adding {} + {}'.format(self, other))
        return MyObj(self.val + other.val)


@addBreaker
def operator_to_custom_classes():
    a = MyObj(1)
    b = MyObj(2)
    print('Comparison:')
    print(operator.lt(a, b))
    print('\nArithmetic:')
    print(operator.add(a, b))
    return

if __name__ == "__main__":
    # combines operators and custom classes
    # functions in operator module work via the standard Python interfaces, yeah, aka data-model methods ..
    operator_to_custom_classes()
