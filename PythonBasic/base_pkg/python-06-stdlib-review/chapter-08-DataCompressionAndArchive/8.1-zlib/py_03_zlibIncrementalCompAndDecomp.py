import sys, zlib
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zlib_incremental():
    import binascii
    compressor = zlib.compressobj(1)
    with open(r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt', 'rb') as src:
        while True:
            block = src.read(64)
            if not block:
                break
            compressed = compressor.compress(block)
            if compressed:
                print('Compressed: {}'.format(
                    binascii.hexlify(compressed)))
            else:
                print('buffering...')
        remaining = compressor.flush()
        print('Flushed: {}'.format(binascii.hexlify(remaining)))

    pass

if __name__ == "__main__":
    # instead of using zlib in memory, 
    # practical approaches are to use zlib `compressobj` and `decompressobj` to handle real life data
    zlib_incremental()