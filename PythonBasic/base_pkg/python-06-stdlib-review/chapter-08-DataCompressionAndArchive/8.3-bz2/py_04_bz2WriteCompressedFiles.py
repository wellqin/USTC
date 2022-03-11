import sys, bz2
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def bz2_file_write():
    import io, os
    data = 'contents of the example file go here. \n'
    with bz2.BZ2File('example.bz2', 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf8') as enc:
            enc.write(data)
    # no work on winos
    # os.system('file example.bz2')    
    pass

@addBreaker
def bz2_file_compresslevel():
    import io, os
    lorem = r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt'
    data = open(lorem, 'r', encoding='utf-8').read() * 1024
    print('Input contains {} bytes'.format(
    len(data.encode('utf-8'))))
    for i in range(1, 10):
        filename = 'compress-level-{}.bz2'.format(i)
        with bz2.BZ2File(filename, 'wb', compresslevel=i) as output:
            with io.TextIOWrapper(output, encoding='utf-8') as enc:
                enc.write(data)
        # os.system('cksum {}'.format(filename))
        print('cksum: {}, compress-level-{}'.format(os.stat(filename).st_size, i))
    pass

@addBreaker
def bz2_file_writelines():
    import io, os, itertools
    data = 'The same line, over and over.\n'
    with bz2.BZ2File('example.bz2', 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf8') as enc:
            enc.write(data)    
    pass

@addBreaker
def bz2_BZ2File_compresslevel():
    import io, os
    lorem = r'chapter-08-DataCompressionAndArchive\8.1-zlib\lorem.txt'
    data = open(lorem, 'r', encoding='utf8').read() * 1024
    print('Input contains {} bytes'.format(len(data.encode('utf8'))))
    for i in range(1, 10):
        filename = 'compress-level-{}.bz'.format(i)
        with bz2.BZ2File(filename, 'wb', compresslevel=i) as output:
            with io.TextIOWrapper(output, encoding='utf8') as enc:
                enc.write(data)
                print('cksum {}, {}'.format(os.stat(filename).st_size, filename))
    pass

@addBreaker
def bz2_BZ2File_writelines():
    import io, os, itertools
    data = 'the same line, over and over.\n'
    with bz2.BZ2File('line.bz2', 'wb') as output:
        with io.TextIOWrapper(output, encoding='utf8') as enc:
            enc.writelines(itertools.repeat(data, 10))   
    pass

if __name__ == "__main__":
    # by default
    bz2_file_write()
    # user-defined compresslevel
    bz2_file_compresslevel()
    # bz2.BZ2File() works like the usual methods for writing and reading data
    bz2_file_write()
    # user-defined compresslevel
    bz2_BZ2File_compresslevel()
    # writelines()
    bz2_BZ2File_writelines()