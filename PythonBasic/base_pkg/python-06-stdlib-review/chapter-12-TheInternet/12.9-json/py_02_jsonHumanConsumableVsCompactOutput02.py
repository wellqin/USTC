import json
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))
"""
For highly nested data structures, 
specify a value for indent so the output is formatted nicely as well.
"""
print('NORMAL:', json.dumps(data, sort_keys=True))
print('INDENT:', json.dumps(data, sort_keys=True, indent=2))