import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_shuffle():
    import itertools
    FACE_CARDS = tuple('JQKA')
    SUITS      = tuple('HDCS')

    def new_deck():
        return [
            '{:>2}{}'.format(*c)
            for c in itertools.product(
                itertools.chain(range(2, 11), FACE_CARDS),
                SUITS,
            )
        ]

    def show_deck(deck: list):
        p_deck = deck[:]
        while p_deck:
            row    = p_deck[:13]
            p_deck = p_deck[13:]
            for j in row:
                print(j, end=' ')
            print()
    
    # make a new deck, with the cards in order
    deck = new_deck()
    print('Initial deck:')
    show_deck(deck)
    # shuffle the deck to random order
    # xi pai 
    random.shuffle(deck)
    print('\nShuffled deck:')
    show_deck(deck)
    # deal 4 hands of 5 cards each
    hands = [[], [], [], []]
    for _ in range(5):
        for h in hands:
            h.append(deck.pop())
    # show the hands
    print('\nhands:')
    for n, h in enumerate(hands):
        print('{}:'.format(n + 1), end=' ')
        for c in h:
            print(c, end=' ')
        print()
    # show the remaining deck
    print('\nRemaining deck:')
    show_deck(deck)

@addBreaker
def random_sample():
    with open('./words', 'rt') as f:
        words = f.readlines()
    words = [w.strip() for w in words]
    for w in random.sample(words, 5):
        print(w)
        

if __name__ == "__main__":
    # xi pai
    random_shuffle()
    # sampling
    random_sample()