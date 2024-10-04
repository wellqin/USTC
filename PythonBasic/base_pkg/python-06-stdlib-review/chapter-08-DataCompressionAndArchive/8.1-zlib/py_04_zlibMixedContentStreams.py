import sys, zlib
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zlib_mixed():
    lorem = open(r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt', 'rb').read()
    compressed = zlib.compress(lorem)
    combined = compressed + lorem

    decompressor = zlib.decompressobj()
    decompressed = decompressor.decompress(combined)
    decompressed_matches = decompressed == lorem
    print('Decompressed matches lorem:', decompressed_matches)
    unused_matches = decompressor.unused_data == lorem
    print('Unused data matches lorem :', unused_matches)
    pass

if __name__ == "__main__":
    # so far, all things `zlib` does is in memory.
    # htf do i store the compressed data to hd?
    # it's not practical at all
    # i dont like this shit
    zlib_mixed()