# -*- coding:utf-8 -*-
from pprint import pprint

from fn import _
from fn.op import zipwith
from itertools import repeat

""" 1、Scala-style lambdas definition """
pprint(list(map(_ * 2, range(5))))  # [0, 2, 4, 6, 8]
pprint(list(filter(_ < 10, [9, 10, 11])))  # [9]
pprint(list(zipwith(_ + _)([0, 1, 2], repeat(10))))  # [10, 11, 12]
# Attention "_"
pprint(_ + 2)  # "(x1) => (x1 + 2)"
pprint(_ + _ * _)  # "(x1, x2, x3) => (x1 + (x2 * x3))"


""" 2、Persistent data structures """

