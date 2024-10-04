import types

# MappingProxyType: a dynamic mapping view, just a view
# you can't change source data via the view

d = {1: "A"}
d_proxy = types.MappingProxyType(d)
print(d_proxy)

# read element
print(d_proxy[1])

# but can't write elements into the view
# d_proxy[2] = 'x' # TypeError

# changing source data will also lead the view change dynamically
# yeah, it behaves like a mask in photoshop
d[2] = 'x'
print(d_proxy)