import sys, codecs, random
sys.path.append('.')
from pkg.breaker import addBreaker
from codecs_to_hex import to_hex

@addBreaker
def codecs_open_write():
    encoding = random.choice(['utf8', 'utf16', 'utf32'])
    filename = encoding + '.txt'
    print('Writing to', filename)
    # `codecs` provides the simplest interface is an alternative to the built-in `open()` function
    with codecs.open(filename, mode='w', encoding=encoding) as f:
        f.write('français')
    nbytes = {
        'utf8': 1,
        'utf16': 2,
        'utf32': 4,
    }.get(encoding, 1)
    print('File contents:')
    with open(filename, mode='rb') as f:
        print(to_hex(f.read(), nbytes))
    pass

@addBreaker
def codecs_open_read():
    encoding = random.choice(['utf8', 'utf16', 'utf32'])
    filename = encoding + '.txt'
    print('Reading from', filename)
    with codecs.open(filename, mode='r', encoding=encoding) as f:
        print(repr(f.read()))


if __name__ == "__main__":
    # codecs write
    codecs_open_write()
    # codecs read
    codecs_open_read()
    