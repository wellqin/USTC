import sys, bz2
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def bz2_incremental():
    import binascii, io
    compressor = bz2.BZ2Compressor()

    lorem = r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt'
    with open(lorem, 'rb') as _input:
        while True:
            # when remaining data is not enough ..
            block = _input.read(64)
            if not block:
                break
            print('block size:', len(block))
            compressed = compressor.compress(block)
            if compressed:
                print('Compressed: {}'.format(binascii.hexlify(compressed)))
            else:
                print('buffering...')
        remaining = compressor.flush()
        print('remaining block size: ', len(remaining))
        print('Flushed: {}'.format(binascii.hexlify(remaining)))
    pass


if __name__ == "__main__":
    # the compressor maintains an internal buffer of compressed data.
    # compression algorithm depends on `checksums` and `minimum block size`,
    # the compressor may not be ready to return data each time it receives more input.
    # if it does not have an entire compressed block ready, it returns an empty string
    # ! when all of the data is fed in, the `flush()` method forces the compressor to close the final block
    # ! and return the result of compressed data
    bz2_incremental()