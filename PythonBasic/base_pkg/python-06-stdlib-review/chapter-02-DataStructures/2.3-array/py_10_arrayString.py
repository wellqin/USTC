"""

Table of Type codes for array members.
(Int, short, long, long long, float, double)

+---------+-------------------+-----------------------+
| Code    | Type              | Minimum Size (Bytes)  |
+=========+===================+=======================+
| b       | Int               | 1                     |
+---------+-------------------+-----------------------+
| B       | Int               | 1                     |
+---------+-------------------+-----------------------+
| h       | Signed short      | 2                     |
+---------+-------------------+-----------------------+
| H       | Unsigned short    | 2                     |
+---------+-------------------+-----------------------+
| i       | Signed int        | 2                     |
+---------+-------------------+-----------------------+
| I       | Usigned int       | 2                     |
+---------+-------------------+-----------------------+
| l       | Signed long       | 4                     |
+---------+-------------------+-----------------------+
| L       | Unsigned long     | 4                     |
+---------+-------------------+-----------------------+
| q       | Signed long long  | 8                     |
+---------+-------------------+-----------------------+
| Q       | Unsigned longlong | 8                     |
+---------+-------------------+-----------------------+
| f       | float             | 4                     |
+---------+-------------------+-----------------------+
| d       | double            | 8                     |
+---------+-------------------+-----------------------+

"""


import array, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def array_string():
    import binascii
    s = b'This is the array.'
    a = array.array('b', s)
    print('As byte string:', s)
    print('As array      :', a)
    print('As hex        :', binascii.hexlify(a))

@addBreaker
def array_string_to_array():
    import binascii
    s = 'This is the array.'
    a = array.array('b')
    a.fromstring(s)
    print('As string     :', s)
    print('As array      :', a)
    print('As hex        :', binascii.hexlify(a))   

@addBreaker
def array_sequence():
    a = array.array('i', range(3))
    print('inital  :', a)
    a.extend(range(3))
    print('extend  :', a)
    print('slice   :', a[2:5])
    print('iterator:', end=' ')
    print(list(enumerate(a)))

@addBreaker
def array_file():
    import binascii
    a = array.array('i', range(5))
    print('a1           :', a)

    # write the array of numbers to a temporary file
    output = os.path.join(os.path.dirname(__file__), 'tmp')
    with open(output, 'wb') as f:
        a.tofile(f)

    # read the raw data
    with open(output, 'rb') as input:
        raw_data = input.read()
        print('Raw Contents :', binascii.hexlify(raw_data))
        # read the data into an array
        input.seek(0)
        a2 = array.array('i')
        a2.fromfile(input, len(a))
        print('a2           :', a2)

@addBreaker
def array_tobytes():
    import binascii
    a = array.array('i', range(5))
    print('A1   :', a)
    as_bytes = a.tobytes()
    print('Bytes:', binascii.hexlify(as_bytes))
    a2 = array.array('i')
    a2.frombytes(as_bytes)
    print('A2   :', a2)

@addBreaker
def array_byteswap():
    import binascii
    def to_hex(a):
        chars_per_item = a.itemsize * 2 # 2 hex digits
        hex_version    = binascii.hexlify(a)
        num_chunks     = len(hex_version) // chars_per_item
        for i in range(num_chunks):
            start = i * chars_per_item
            end   = start + chars_per_item
            yield hex_version[start:end]
    start = int('0x12345678', 16)
    end   = start + 5
    a1    = array.array('i', range(start, end))
    a2    = array.array('i', range(start, end))
    a2.byteswap()
    fmt   = '{:>12} {:>12} {:>12} {:>12}'
    print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
    print(fmt.format('-'*12, '-'*12, '-'*12, '-'*12))
    fmt   = '{!r:>12} {:>12} {!r:>12} {:>12}'
    for values in zip(to_hex(a1), a1, to_hex(a2), a2):
        print(fmt.format(*values))

def main():
    # array string -> bytes -> hex
    array_string()
    array_string_to_array()
    # extend an array just like other python sequences
    array_sequence()
    # write array into file vise-versa
    array_file()
    # array <-> bytes
    array_tobytes()
    # if data in the array is not the native byte order, 
    # or if the data needs to be swapped before being sent to a system with a different byte order (or over the network)
    # it's possible to convert the entire array w/o iterating over the elements from Python. using array.byteswap()
    array_byteswap()

if __name__ == "__main__":
    main()