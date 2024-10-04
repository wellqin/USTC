import sys, mmap
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def mmap_read():
    with open('chapter-06-FileSystem\\6.9-mmp\\lorem.txt', 'r') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            # 'consume' concept
            print('First 10 bytes via read  :', m.read(10))
            print('First 10 bytes via slice :', m[:10])
            print('2nd   10 bytes via read  :', m.read(10))


if __name__ == "__main__":
    mmap_read()