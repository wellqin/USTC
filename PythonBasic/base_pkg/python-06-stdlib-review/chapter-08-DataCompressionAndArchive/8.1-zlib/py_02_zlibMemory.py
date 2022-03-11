import sys, zlib
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zlib_memory():
    import binascii
    od      = b'This is the original text.'
    comp    = zlib.compress(od)
    decomp  = zlib.decompress(comp)

    print('original     :', len(od), od)
    print('comp         :', len(comp), binascii.hexlify(comp))
    print('decomp       :', len(decomp), decomp)
    pass

@addBreaker
def zlib_lengths():
    original_data = b'This is the original text.'
    template = '{:>15} {:>15}'
    print(template.format('len(data)', 'len(compressed)'))
    print(template.format('-' * 15, '-' * 15))
    for i in range(5):
        data = original_data * i
        compressed = zlib.compress(data)
        highlight = '*' if len(data) < len(compressed) else ''
        print(template.format(len(data), len(compressed)), highlight)

    pass

@addBreaker
def zlib_compresslevel():
    input_data = b'Some repeated text.\n' * 1024
    template = '{:>5} {:>5}'
    print(template.format('Level', 'Size'))
    print(template.format('-----', '----'))
    for i in range(0, 10):
        data = zlib.compress(input_data, i)
        print(template.format(i, len(data)))
    pass


if __name__ == "__main__":
    zlib_memory()
    # Space diff btwn comp > uncompressed
    zlib_lengths()
    # user defined compress leve
    zlib_compresslevel()