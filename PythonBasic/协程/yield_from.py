#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/5/4 19:34
@Author  : qinwei05
"""


def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next


def gather_tallies(tallies):
    while 1:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []
acc = gather_tallies(tallies)
next(acc)  # Ensure the accumulator is ready to accept values

for i in range(4):
    acc.send(i)
acc.send(None)  # Finish the first tally

for i in range(5):
    acc.send(i)
acc.send(None)  # Finish the second tally
print(tallies)
