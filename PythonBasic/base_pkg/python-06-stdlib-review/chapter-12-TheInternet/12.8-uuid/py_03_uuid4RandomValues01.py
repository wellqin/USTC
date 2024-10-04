"""
Sometimes host-based and namespace-based UUID values are not “different enough.” 

For example, in cases where the UUID is intended to be used as a hash key, a more random
sequence of values with more differentiation is desirable to avoid collisions in the hash table.

Having values with fewer common digits also makes it easier to find them in log files. 

To add greater differentiation in UUIDs, use uuid4() to generate them using random input
values.

"""

import uuid
for i in range(3):
    print(uuid.uuid4())