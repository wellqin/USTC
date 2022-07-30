#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
该例子来展示如何实现 __getitme__ 和__len__ 这两个特殊方法，也能见识到特殊方法的强大。

虽然 FrenchDeck 隐式地继承了 object 类， 但功能却不是继承而来的。我们通过数据模型和一些合成来实现这些功能。通过实现 __len__
和 __getitem__ 这两个特殊方法，FrenchDeck 就跟一个 Python 自有的序列数据类型一样，可以体现出 Python 的核心语言特性（例如迭代和
切片）。同时这个类还可以用于标准库中诸如random.choice、reversed 和 sorted 这些函数。
另外，对合成的运用使得 __len__ 和 __getitem__ 的具体实现可以代理给 self._cards这个 Python 列表（即 list 对象）。

@Time    : 2022/4/3 16:53
@Author  : qinwei05
"""

import collections

# collections模块中是各种容器，这里用namedtuple定义了一个Card类，
# namedtuple定义得到的是不能改变的字典，即兼具字典和元组的特性。这里我们的Card类有两个属性，rank和suit，
# 其中rank有13中取值可能，代表大小，suit有四种可能，代表花色
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    一摞Python风格的纸牌
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """
        __len__方法保证我们可以直接用标准库len函数作用于一个FrenchDeck对象，当我们用len函数作用于FrenchDeck对象时，
        实际上解释器会调用FrenchDeck对象中的魔术方法__len__，因此我们实际计算的时其私有属性self._cards列表的长度。
        """
        return len(self._cards)

    def __getitem__(self, position):
        """
        __getitem__方法让我们可以对FrenchDeck对象进行索引操作。
        解释器实际上会调用魔术方法__getitem__，由我们类内__getitem__方法的实现可以看出，实际上返回的是self._cards[position]，
        deck[0] 或 deck[-1]。这都是由 __getitem__ 方法提供的，因此对deck做索引操作实际上是对self._cards列表做索引操作。

        一个类实现了__getitem__方法，那么这个类就变成可迭代的了
        对于可迭代对象，就可以用for进行遍历，用choice随机选取一个元素，支持切片（slicing）操作，in查询，以及排序
        """
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(one_card):
    """
    一张牌的不同花色，用suit_values[card.suit]就可以判断权重
    不同牌的相同花色，用rank_value * len(suit_values)判断权重
    全局判断的话，需要二者结合。
    @param one_card:
    @return:
    """
    rank_value = FrenchDeck.ranks.index(one_card.rank)
    return rank_value * len(suit_values) + suit_values[one_card.suit]


if __name__ == "__main__":
    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
        print(card)
