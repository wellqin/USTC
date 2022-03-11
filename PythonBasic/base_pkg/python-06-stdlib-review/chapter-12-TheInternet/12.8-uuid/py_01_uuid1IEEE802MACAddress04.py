"""
Because each computer has a different MAC address, 
running the example program on different systems will produce entirely different values. 

The next example passes explicit
node IDs to simulate running on different hosts.

"""

import uuid
for node in [0x1ec200d9e0, 0x1e5274040e]:
    print(uuid.uuid1(node), hex(node))