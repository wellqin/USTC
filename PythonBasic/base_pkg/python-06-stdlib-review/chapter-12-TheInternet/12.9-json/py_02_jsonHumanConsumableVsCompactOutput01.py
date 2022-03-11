"""

Table: json vs pickle
+---------------+-------------------------------------------+----------------------------------+
| item          | json                                      | pickle                           |
+===============+===========================================+==================================+
| what          | json obj                                  | pickle obj                       |
+---------------+-------------------------------------------+----------------------------------+
| why           | "protocol" or serialization               | serialization                    |
+---------------+-------------------------------------------+----------------------------------+
| how           | dumps(), loads()                          | dump(), load(), dumps(), loads() |
+---------------+-------------------------------------------+----------------------------------+
| benefit 1     | json has the benefit of having            | no such benefit                  |
|               | implementations in many languages.        |                                  |
|               | cuz it's most used for communicating      |                                  |
|               | btwn web server and client,               |                                  |
|               | but also help meet other interapplication |                                  |
|               | communication needs.                      |                                  |
+---------------+-------------------------------------------+----------------------------------+
| benefit 2     | json produces human-readable results      | n/a                              |
+---------------+-------------------------------------------+----------------------------------+


"""

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

unsorted = json.dumps(data)
print('JSON:', json.dumps(data))
print('SORT:', json.dumps(data, sort_keys=True))

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('UNSORTED MATCH   :', unsorted == first)
print('SORTED MATCH     :', first == second)