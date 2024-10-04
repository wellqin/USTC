# -*- coding:utf-8 -*-


from function.streams import seq, pseq

from collections import namedtuple
from fn import _


l1 = seq([1, 2, 3, 4]) \
    .map(lambda x: x * 2) \
    .filter(lambda x: x > 4) \
    .reduce(lambda x, y: x + y)
# 14

# or if you don't like backslash continuation
l2 = (seq(1, 2, 3, 4)
      .map(lambda x: x * 2)
      .filter(lambda x: x > 4)
      .reduce(lambda x, y: x + y)
      )
# 14
print(l1, l2)


Transaction = namedtuple('Transaction', 'reason amount')
transactions = [
    Transaction('github', 7),
    Transaction('food', 10),
    Transaction('coffee', 5),
    Transaction('digitalocean', 5),
    Transaction('food', 5),
    Transaction('riotgames', 25),
    Transaction('food', 10),
    Transaction('amazon', 200),
    Transaction('paycheck', -1000)
]

# Using the Scala/Spark inspired APIs
food_cost = seq(transactions)\
    .filter(lambda x: x.reason == 'food')\
    .map(lambda x: x.amount)\
    .sum()
print(food_cost)

# Using the LINQ inspired APIs
food_cost = seq(transactions)\
    .where(lambda x: x.reason == 'food')\
    .select(lambda x: x.amount).sum()
print(food_cost)

# Using PyFunctional with fn
food_cost = seq(transactions).filter(_.reason == 'food').map(_.amount).sum()
print(food_cost)

