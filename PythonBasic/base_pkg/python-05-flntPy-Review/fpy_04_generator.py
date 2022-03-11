symbols = '$¢£¥€¤'
t = (ord(symbol) for symbol in symbols)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))

import array
t = array.array('I', (ord(symbol) for symbol in symbols))
print(t)

# using generator to produce Cartesian Product
colors = ['black', 'white']
sizes  = ['S', 'M', 'L']
for item in ('%s %s' % (color, size) for color in colors
                            for size in sizes):
    print(item)