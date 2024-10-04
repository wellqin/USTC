import pprint, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker
from py_pprint_data import data

@addBreaker
def pprint_depth():
    # for very deep data structures, it may not be desirable for the output to include all of the details.
    # using *depth* argument to control how far down into the nested data structure the pretty printer recurses.
    pprint.pprint(data, depth=1)
    pprint.pprint(data, depth=2)

@addBreaker
def pprint_width():
    # default output width for the formatted text is 80 columns.
    # when the width is too small to accommodate the formatted data structure, 
    # the lines are not truncated or wrapped if doing so would introduce invalid syntax
    for width in [80, 5]:
        print('WIDTH = ', width)
        pprint.pprint(data, width=width)
        print()

@addBreaker
def pprint_compact():
    # compact flag tells pprint to try to fit more data on each individual line,
    # rather than spreading complex data structures accross lines.
    print('DEFAULT:') 
    pprint.pprint(data, compact=False)
    print('\nCOMPACT:')
    pprint.pprint(data, compact=True)


if __name__ == "__main__":
    # control display depth ..
    pprint_depth()
    # coutrol display width ..
    pprint_width()
    # makes output compact using compact=True flag
    pprint_compact()
