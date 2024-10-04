# normal usage
names = ("ZL", "World")
a, b = names
print(a)
print(b)
a, b = divmod(10, 3)
print(a)
print(b)

# ignore some elements
local = [(1, "hello"),
        (2, "world"),
        (3, "bonjure")]
for _, word in local:
    print(word)

# ignore more
t = (3, 1, 1, 0, 10)
a, b, *rest = t
print(a)
print(b)
print(rest)

# more examples
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print("{:15} | {:^9} | {:^9}".format('', 'lat.', 'long.'))
fmt = "{:15} | {:9.4f} | {:9.4f}"
for name, cc, pip, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


# namedtuple again
import collections
City = collections.namedtuple('City', 'name country population coordinates')
# or 
# City = collections.namedtuple('City', ['name', 'country', 'population', 'coordinates'])
Tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# useful: _fields
print(City._fields) # just like headers in excel, variables in matrix in R
# useful: _make()
LatLong = collections.namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # accept iterable and generate a namedtupe class
# useful: _asdict()
delhi._asdict()
for k, v in delhi._asdict().items():
    print(k + ":", v)