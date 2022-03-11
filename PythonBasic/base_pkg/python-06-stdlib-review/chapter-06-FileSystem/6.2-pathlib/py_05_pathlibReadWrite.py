import pathlib, sys
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def pathlib_read_write():
    f = pathlib.Path('example.txt')
    f.write_bytes('This is the content'.encode('utf8'))
    with f.open('r', encoding='utf8') as handle:
        print('read from open(): {!r}'.format(handle.read()))
    print('read_text(): {!r}'.format(f.read_text('utf8')))
    return

if __name__ == "__main__":
    pathlib_read_write()