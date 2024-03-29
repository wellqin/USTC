"""
A simple way to encode a MyObj instance is 
to define a function to convert an unknown type to a known type. 

This function does not need to do the encoding; 
it should simply convert one type of object to another.

"""
# import sys
# sys.path.append('.')
import json_myobj
import json

obj = json_myobj.MyObj('instance value goes here')
print('First attempt')
try:
    print(json.dumps(obj))
except TypeError as err:
    print('ERROR:', err)

def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    # Convert objects to a dictionary of their representation.
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d
    
print()
print('With default')
print(json.dumps(obj, default=convert_to_builtin_type))