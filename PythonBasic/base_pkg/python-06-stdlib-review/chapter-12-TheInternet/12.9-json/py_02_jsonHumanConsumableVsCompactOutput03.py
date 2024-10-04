"""
Such verbose output increases the number of bytes needed to transmit the same amount of data; 
thus, it is not intended for use in a production environment. 

In fact, the settings for separating data in the encoded output 
can be adjusted to make it even more compact than the default.

"""


import json
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

print('repr(data)               :', len(repr(data)))

plain_dump = json.dumps(data)
print('dumps(data)              :', len(plain_dump))

small_indent = json.dumps(data, indent=2)
print('dumps(data, indent=2)    :', len(small_indent))

# compacted
"""
The `separators` argument to dumps() should be a tuple containing the strings to separate
the items in a list and to separate the keys from the values in a dictionary. 

The default is(',',': '). 

! Removing the whitespace yields a more compact output.

"""
with_separators = json.dumps(data, separators=(',', ':'))
print('dumps(data, separators)  :', len(with_separators))