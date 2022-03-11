import struct, sys, os, binascii
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) # isn't this stupid? but..
from pkg.breaker import addBreaker

@addBreaker
def struct_endianness():
    values = (1, 'ab'.encode('utf8'), 2.7)
    print('Original values: ', values)
    endianness = [
        ('@', 'native, native'),
        ('=', 'native, standard'),
        ('<', 'little-endian'),
        ('>', 'big-endian'),
        ('!', 'network'),
    ]

    for code, desc in endianness:
        s       = struct.Struct(code + ' I 2s f')
        pack_d  = s.pack(*values)
        print()
        print('Format string    :', s.format, 'for', desc)
        print('Uses             :', s.size, 'bytes')
        print('Packed value     :', binascii.hexlify(pack_d))
        print('Unpacked value   :', s.unpack(pack_d))


if __name__ == "__main__":
    struct_endianness()