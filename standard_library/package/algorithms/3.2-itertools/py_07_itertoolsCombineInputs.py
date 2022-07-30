import itertools, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def itertools_accumulate():
    # ! by default, accumulate() combines two values adds them
    print(list(itertools.accumulate(range(5))))
    print(list(itertools.accumulate('abcde')))
    return

@addBreaker
def itertools_accumulate_custom():
    def f(a: str, b: str):
        return b + a + b
    print(list(itertools.accumulate('abcde', f)))
    return

FACE_CARDS = tuple('JQKA')
SUITS      = tuple('HDCS')
@addBreaker
def itertools_product():
    """Python calculates cartesian product like this"""
    import pprint
    DECK = list(
        itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    )
    # print(DECK)
    for card in DECK:
        print('{:>2}{}'.format(*card), end=' ')
        if card[1] == SUITS[-1]:    # ? wtf is this line?
            print()                 # A: print format, newline ..
    print()
    for card in DECK:
        pprint.pprint('{:>2}{}'.format(*card), depth=1)
    return

@addBreaker
def itertools_product_ordering():
    # customs product's behavior via changing the order of the arguments to product
    DECK = list(
        itertools.product(
            SUITS,
            itertools.chain(range(2, 11), FACE_CARDS),
        )
    )
    
    for card in DECK:
        print('{:>2}{}'.format(card[1], card[0]), end=' ')
        if card[1] == FACE_CARDS[-1]:
            print()
    return

@addBreaker
def itertools_product_repeat():
    def show(iterable):
        for i, item in enumerate(iterable, 1):
            print(item, end=' ')
            if (i % 3) == 0:
                print()
        return

    print('Repeat 2:\n')
    show(list(itertools.product(range(3), repeat=2)))
    print('\nRepeat 3:\n')
    show(list(itertools.product(range(3), repeat=3)))
    return

S = 'abcd'
def pcc_show(iterable):
    first = None
    for _, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()
    return
@addBreaker
def itertools_permutations():

    print('All permutations:\n')
    pcc_show(itertools.permutations(S))
    print('\nPairs:\n')
    pcc_show(itertools.permutations(S, r=2))
    return

@addBreaker
def itertools_combinations():
    print('All combinations:\n')
    pcc_show(itertools.combinations(S, r=2))
    print('\nUnique Pairs:\n')
    pcc_show(itertools.combinations(S, r=2))
    return  

@addBreaker
def itertools_combinations_vs_combinations_with_replacement():
    print('Original: ', S)
    print()
    print('combinatinos():')
    pcc_show(itertools.combinations(S, r=2))
    print('\ncombinations_with_replacement():')
    pcc_show(itertools.combinations_with_replacement(S, r=2))
    return


if __name__ == "__main__":
    # accumulate
    itertools_accumulate()
    # accumulate() customs it by passing *func*
    itertools_accumulate_custom()
    # product
    itertools_product()
    # change the order of arguments passing product()
    itertools_product_ordering()
    # to compute the product of a sequence with itself, 
    # specify how many times the input should be repeated
    itertools_product_repeat()
    # permutations
    itertools_permutations()
    # unique combinations, 
    # combinations() dosn't repeat individual input elements
    itertools_combinations()
    # ! sometimes it is useful to consider combinations that do include repeated elements.
    # using combinations_with_replacement()
    itertools_combinations_vs_combinations_with_replacement()