"""
? wait a second, wtf is buffer in struct?
# A: tl;dr buffer is a block of area which stores tracking data in a device
# if u wanna read data faster, use Buffer; if u wanna store data longer, use Cache

? what is *format* in struct?
# A: https://docs.python.org/3/library/struct.html

+-----------+---------------------+---------------------+---------------+
| Format    | C Type              | Python Type         | Standard size |
+===========+=====================+=====================+===============+
| x         | pad byte            | no value            |               |  
+-----------+---------------------+---------------------+---------------+
| c         | char                | bytes of lenght 1   | 1             |
+-----------+---------------------+---------------------+---------------+
| b         | signed char         | integer             | 1             |
+-----------+---------------------+---------------------+---------------+
| B         | unsigned char       | integer             | 1             |
+-----------+---------------------+---------------------+---------------+
| ?         | _Bool               | bool                | 1             |
+-----------+---------------------+---------------------+---------------+
| h         | unsigned short      | integer             | 2             |
+-----------+---------------------+---------------------+---------------+
| H         | signed short        | integer             | 2             |
+-----------+---------------------+---------------------+---------------+
| i         | int                 | integer             | 4             |
+-----------+---------------------+---------------------+---------------+
| I         | unsigned int        | integer             | 4             |
+-----------+---------------------+---------------------+---------------+
| l         | long                | integer             | 4             |
+-----------+---------------------+---------------------+---------------+
| L         | unsigned long       | integer             | 4             |
+-----------+---------------------+---------------------+---------------+
| q         | long long           | integer             | 8             |
+-----------+---------------------+---------------------+---------------+
| Q         | unsigned long long  | integer             | 8             |
+-----------+---------------------+---------------------+---------------+
| n         | ssize_t             | integer             |               |
+-----------+---------------------+---------------------+---------------+
| N         | size_t              | integer             |               |
+-----------+---------------------+---------------------+---------------+
| e         | (6)                 | float               | 2             |
+-----------+---------------------+---------------------+---------------+
| f         | float               | float               | 4             |
+-----------+---------------------+---------------------+---------------+
| d         | double              | float               | 8             |
+-----------+---------------------+---------------------+---------------+
| s         | char[]              | bytes               |               |
+-----------+---------------------+---------------------+---------------+
| p         | char[]              | bytes               |               |
+-----------+---------------------+---------------------+---------------+
| P         | void *              | integer             |               |
+-----------+---------------------+---------------------+---------------+


"""

import struct, sys, os, binascii, ctypes, array
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def struct_buffers():
    values = (1, 'ab'.encode('utf8'), 3.8)
    s = struct.Struct('I 2s f')
    print('Original :', values)
    print()
    print('ctypes string buffer')
    # buffer
    b = ctypes.create_string_buffer(s.size)
    print('Before   :', binascii.hexlify(b.raw))
    # pack values into ctypes.create_string_buffer
    s.pack_into(b, 0, *values)
    print('After    :', binascii.hexlify(b.raw))
    print('Unpacked :', s.unpack_from(b, 0))
    print()
    print('array.array')
    a = array.array('b', b'\0' * s.size)
    print('Before   :', binascii.hexlify(a))
    # pack values into array.array
    s.pack_into(a, 0, *values)
    print('After    :', binascii.hexlify(a))
    print('Unpacked :', s.unpack_from(a, 0))

if __name__ == "__main__":
    struct_buffers()