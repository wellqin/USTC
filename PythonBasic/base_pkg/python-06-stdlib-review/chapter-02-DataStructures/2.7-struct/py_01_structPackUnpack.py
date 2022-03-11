"""
P117-P120 struct: Binary Data Structures

! what is struct?
# the **struct** module includes functions for converting between strings of bytes and native Python data types such as numbers and strings
# hmm, it's similar with array, binascii

! why struct?
another alternative
more altertives more happiness

! how to use?
(20200808, findings: VSCode global hotkeys/shortcuts conflict with other app[NetEasy YunYinyue in my case])

struct
|-- Functions vs Struct class
|-- Packing and unpacking
|-- Endianness
|-- Buffers

Table of Byte Order Specifiers for Struct

+--------+----------------------+
| Code   | Meaning              |
+========+======================+
| @      | Native order         | 
+--------+----------------------+
| =      | Native standard      | 
+--------+----------------------+
| <      | Little-endian        | 
+--------+----------------------+
| >      | Big-endian           | 
+--------+----------------------+
| !      | Network order        | 
+--------+----------------------+

# ? what the hell is endian(little-endian, big-endian), ELI56?
# A: https://linoxide.com/how-tos/programs/system-endianness-structure-padding-c-examples/
# endianness exists because of different machines have different value-storing method. 
# a sequence of values is stored in order of small->big(increment, aka big-endian); ie. IBM and DEC machines
# a sequence of values is stored in order of big->small(decrement, aka little-endian); ie. Sun and Motorola machines
# little endian is opposite of big endian
# as a programmer, u have to make sure data is read correctly from different machines.

"""


import struct, binascii, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pkg.breaker import addBreaker

@addBreaker
def struct_pack():
    values = (1, 'ab'.encode('utf-8'), 2.7)
    s      = struct.Struct('I 2s f') # ? wtf is this *format* argument
    pack_d = s.pack(*values)
    print('Original values:', values)
    print('Format string  :', s.format) # ? what? # A: return Struct's format which is from the Struct *format* argument
    print('uses           :', s.size, 'bytes')
    print('packed value   :', binascii.hexlify(pack_d))

@addBreaker
def struct_unpack():
    pack_d = binascii.unhexlify(b'0100000061620000cdcc2c40')
    s      = struct.Struct('I 2s f')
    print('unpacked values:', s.unpack(pack_d))

def main():
    # pack data
    struct_pack()
    # unpack
    struct_unpack()

if __name__ == "__main__":
    main()