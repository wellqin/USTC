import collections
# create double ended queue. it's always return a list-like object
dq = collections.deque(range(10), maxlen=10)
print(dq)

# rotate a queue, the most right n elements are moved to left when n > 0
dq.rotate(3)
print(dq)
# [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
dq.rotate(-4)
print(dq)
# [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]

# append elements to left. 
# because maxlen = 10, forever 10 elements inside the queue.
# when one new element is added into the queue on left side, then right end element will be removed
# then add the new element to left end
dq.appendleft(-1)
print(dq)
dq.append("strange")
print(dq)

# extend a queue like a list or an array!
dq.extend("hello world".split())
print(dq)

# likewise, you may also determine which end you gonna extend
# note: extendleft(iter) will add element reversedly.
dq.extendleft(set([3, 1, 2, 1, 2]))
print(dq)