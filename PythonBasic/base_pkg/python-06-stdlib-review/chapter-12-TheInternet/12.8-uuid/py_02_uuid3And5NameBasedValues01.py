"""
In some contexts, it is desirable to create UUID values from names instead of random
or time-based values.

Versions 3 and 5 of the UUID specification use cryptographic hash
values (MD5 or SHA-1, respectively) to combine namespace-specific seed values with names.

Several well-known namespaces, identified by predefined UUID values, are available for
working with DNS, URLs, ISO OIDs, and X.500 Distinguished Names.

New applicationspecific
namespaces can be defined by generating and saving UUID values.

"""


import uuid
hostnames = ['www.doughellmann.com', 'blog.doughellmann.com']
for name in hostnames:
    print(name)
    print(' MD5(uuid3)   :', uuid.uuid3(uuid.NAMESPACE_DNS, name))
    print(' SHA-1(uuid5) :', uuid.uuid5(uuid.NAMESPACE_DNS, name))
    print()