import doctest
import collections, random

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """A simple and concise class holds all french cards

    :return: a sequence of cards
    :rtype: list

    Examples
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')
    >>> Card('Q', 'diamonds') in deck
    True
    >>> Card('7', 'beast') in deck
    False
    >>> deck[:3]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def choice(self):
        return random.choice(self)


deck = FrenchDeck()
print(deck.choice())
print(deck.choice())
print(deck.choice())

# ordinal conversion
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# sorting
for card in sorted(deck, key=spades_high):
    print(card)

if __name__ == "__main__":
    doctest.testmod()
