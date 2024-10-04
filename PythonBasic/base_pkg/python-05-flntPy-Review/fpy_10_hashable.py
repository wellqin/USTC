# is tuple hashable? 
# example 01
tt = (1, 2, (30, 40))
print(hash(tt))

# example 03
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

# example 02
tl = (1, 2, [30, 40])
print(hash(tl))

