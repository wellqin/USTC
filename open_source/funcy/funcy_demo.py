# -*- coding:utf-8 -*-
"""
https://github.com/Suor/funcy
"""
from itertools import count
from pprint import pprint

import funcy as fc

"""Sequences"""
item = [1, 2, 3]


def sequences_generate():
    pprint([item] * 3)
    pprint(item * 3)
    # pprint(list(map(lambda x: x ** 2, count(1))))


if __name__ == "__main__":
    sequences_generate()
