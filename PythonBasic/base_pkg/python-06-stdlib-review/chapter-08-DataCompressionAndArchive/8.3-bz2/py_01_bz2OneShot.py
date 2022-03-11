import sys, bz2
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def bz2_memory():
    import binascii
    original_data = b'This is the original text.'
    print('Original     : {} bytes'.format(len(original_data)))
    print(original_data)
    print()
    compressed = bz2.compress(original_data)
    print('Compressed   : {} bytes'.format(len(compressed)))
    hex_version = binascii.hexlify(compressed)
    for i in range(len(hex_version) // 40 + 1):
        print(hex_version[i * 40:(i + 1) * 40])
    print()
    decompressed = bz2.decompress(compressed)
    print('Decompressed : {} bytes'.format(len(decompressed)))
    print(decompressed)
    pass

@addBreaker
def bz2_lengths():
    original_data = b'This is the original text.'
    fmt = '{:>15} {:>15}'
    print(fmt.format('len(data)', 'len(compressed)'))
    print(fmt.format('-' * 15, '-' * 15))
    for i in range(5):
        data = original_data * i
        compressed = bz2.compress(data)
        print(fmt.format(len(data), len(compressed)), end='')
        print('*' if len(data) < len(compressed) else '')
    pass

if __name__ == "__main__":
    # same names: compress() vs decompress(). nice 69
    bz2_memory()
    # compression effect
    bz2_lengths()