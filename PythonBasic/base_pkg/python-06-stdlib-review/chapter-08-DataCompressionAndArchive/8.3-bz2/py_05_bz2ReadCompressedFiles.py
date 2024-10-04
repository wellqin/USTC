import sys, bz2
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def bz2_file_read():
    import io
    fn = r'example.bz2'
    with bz2.BZ2File(fn, 'rb') as _input:
        with io.TextIOWrapper(_input, encoding='utf8') as dec:
            print(dec.read())
    pass

@addBreaker
def bz2_file_seek():
    with bz2.BZ2File('example.bz2', 'rb') as _input:
        print('Entire file:')
        all_data = _input.read()
        print(all_data)
        expected = all_data[5:15]
        # rewind to beginning
        _input.seek(0)
        # move ahead 5 bytes
        _input.seek(5)
        print('Starting at position 5 for 10 bytes:')
        partial = _input.read(10)
        print(partial)
        print()
        print(expected == partial)
    pass


if __name__ == "__main__":
    bz2_file_read()
    # just like usual file operations
    # open(), close(), write(), read(), writelines(), readlines() etc.
    # seek()