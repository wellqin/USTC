import sys, bz2
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def bz2_mixed():
    file  = r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt'
    lorem = open(file, 'rt').read().encode('utf8')
    compressed = bz2.compress(lorem)
    combined   = compressed + lorem

    decompressor = bz2.BZ2Decompressor()
    decompressed = decompressor.decompress(combined)

    decompressed_matches = decompressed == lorem
    print('Decompressed matches lorem:', decompressed_matches)

    unused_matches = decompressor.unused_data == lorem
    print('Unused data matches lorem :', unused_matches)
    
    pass


if __name__ == "__main__":
    bz2_mixed()