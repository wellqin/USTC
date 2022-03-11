import sys, gzip
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def gzip_write():
    import io, os
    out_fn = 'example.txt.gz'
    # embeded `open()` function. 69 nice
    with gzip.open(out_fn, 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf8') as enc:
            enc.write('contents of the example file go here. \n')
    print(out_fn, 'contains', os.stat(out_fn).st_size, 'bytes')
    # os.system('file -b --mine {}'.format(out_fn)) # this line is unix-like system cmd
    pass

@addBreaker
def gzip_compresslevel():
    import io, os, hashlib
    def get_hash(data):
        return hashlib.md5(data).hexdigest()
    
    lorem = r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt'
    data  = open(lorem, 'r').read() * 1024
    cksum = get_hash(data.encode('utf8'))
    print('Level Size Checksum')
    print('----- ---------- ---------------------------------')
    print('data {:>10} {}'.format(len(data), cksum))
    for i in range(0, 10):
        filename = 'compress-level-{}.gz'.format(i)
        with gzip.open(filename, 'wb', compresslevel=i) as output:
            with io.TextIOWrapper(output, encoding='utf-8') as enc:
                enc.write(data)
        size = os.stat(filename).st_size
        cksum = get_hash(open(filename, 'rb').read())
        print('{:>5d} {:>10d} {}'.format(i, size, cksum))
    pass

@addBreaker
def gzip_writelines():
    import io, os, itertools

    out_fn = 'example_lines.txt.gz'
    with gzip.open(out_fn, 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf8') as enc:
            enc.writelines(itertools.repeat('the same line, over and over.\n', 10))
    # os.system('gzcat example_lines.txt.gz')
    pass

if __name__ == "__main__":
    # by default, compresslevel from 0 to 9.
    # lower value means compression less, proceessing fast
    # higher value means compressing more, processing slow
    gzip_write()
    gzip_compresslevel()
    # also includes writelines() method to write a sequence of strings
    gzip_writelines()
